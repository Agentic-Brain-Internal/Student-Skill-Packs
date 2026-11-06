#!/usr/bin/env python3
"""Fetch the skills listed in skills.json from their original GitHub repos.

Nothing in this pack is a copy of anyone's skill. This script downloads each
skill straight from its author's repo, at the moment you run it, and then
either installs it into a skills folder (Claude Code) or packs it as a zip
you can upload in the Claude app (Customize > Skills).

Standard library only. Needs Python 3.8+ and either git or HTTPS access to
github.com / codeload.github.com.

Examples
  python get_skills.py install                      # core skills -> ~/.claude/skills
  python get_skills.py zip --dest ./skill-zips      # core skills -> one zip each
  python get_skills.py install --only humanizer,stop-slop
  python get_skills.py list                         # show what's in the pack

The script never runs anything it downloads.
"""
import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE.parent / "skills.json"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SKIP_DIRS = {".git", ".github"}


def load_manifest(src):
    if re.match(r"^https?://", src):
        with urllib.request.urlopen(src, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    return json.loads(Path(src).read_text(encoding="utf-8"))


def pick(manifest, groups, only):
    skills = manifest["skills"]
    if only:
        wanted = {x.strip() for x in only.split(",") if x.strip()}
        chosen = [s for s in skills if s["id"] in wanted or s["name"] in wanted]
        missing = wanted - {s["id"] for s in chosen} - {s["name"] for s in chosen}
        if missing:
            sys.exit("Not in the pack: " + ", ".join(sorted(missing)))
        return chosen
    return [s for s in skills if s["group"] in groups]


# ---------- downloading ----------

class Fetcher:
    """Downloads only the folders we need, one checkout per repo."""

    def __init__(self, workdir):
        self.workdir = Path(workdir)
        self.git = shutil.which("git")
        self.cache = {}

    def get(self, repo, ref, paths):
        key = (repo, ref)
        if key in self.cache:
            return self.cache[key]
        target = self.workdir / repo.replace("/", "__")
        ok = False
        if self.git:
            ok = self._git(repo, ref, paths, target)
        if not ok:
            if target.exists():
                shutil.rmtree(target, ignore_errors=True)
            self._tarball(repo, ref, paths, target)
        self.cache[key] = target
        return target

    def _run(self, *args, cwd=None):
        return subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, text=True)

    def _git(self, repo, ref, paths, target):
        url = f"https://github.com/{repo}.git"
        r = self._run(self.git, "clone", "--quiet", "--depth", "1", "--filter=blob:none",
                      "--no-checkout", "--branch", ref, url, str(target))
        if r.returncode != 0:
            return False
        # Only check out the skill folders and licence files we need.
        r = self._run(self.git, "sparse-checkout", "set", "--no-cone", *paths, cwd=target)
        if r.returncode != 0:
            return False
        r = self._run(self.git, "checkout", "--quiet", cwd=target)
        return r.returncode == 0

    def _tarball(self, repo, ref, paths, target):
        url = f"https://codeload.github.com/{repo}/tar.gz/{ref}"
        req = urllib.request.Request(url, headers={"User-Agent": "claude-skill-pack"})
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        target.mkdir(parents=True, exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            for m in tar.getmembers():
                parts = m.name.split("/", 1)
                if len(parts) < 2 or not m.isfile():
                    continue
                rel = parts[1]
                if not any(_matches(rel, p) for p in paths):
                    continue
                dest = (target / rel).resolve()
                if not str(dest).startswith(str(target.resolve())):
                    continue  # refuse paths that escape the folder
                dest.parent.mkdir(parents=True, exist_ok=True)
                with tar.extractfile(m) as src, open(dest, "wb") as out:
                    shutil.copyfileobj(src, out)


def _matches(rel, pattern):
    p = pattern.strip("/")
    if p in ("", "*"):
        return True
    if p.endswith("/*"):
        return rel.startswith(p[:-1])
    return rel == p or rel.startswith(p + "/")


def sparse_paths(entries):
    paths = set()
    for s in entries:
        if s["path"]:
            paths.add(s["path"].strip("/") + "/*")
        else:
            paths.add("/*")
        if s.get("license_file"):
            paths.add(s["license_file"])
    return sorted(paths)


# ---------- checking ----------

def frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not m:
        return None
    fm = m.group(1)
    keys = re.findall(r"^([A-Za-z0-9_-]+):", fm, re.M)
    name = re.search(r"^name:\s*['\"]?([^'\"\n]+)['\"]?\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.*?)(?=^[A-Za-z0-9_-]+:|\Z)", fm, re.M | re.S)
    d = desc.group(1).strip() if desc else ""
    if d[:1] in "|>":
        d = d[1:].lstrip("-+")
    d = " ".join(line.strip() for line in d.strip().strip("'\"").splitlines()).strip()
    return {"keys": keys, "name": name.group(1).strip() if name else "", "description": d}


def check(folder, expected):
    problems, warnings = [], []
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return ["no SKILL.md"], warnings
    fm = frontmatter(skill_md.read_text(encoding="utf-8", errors="replace"))
    if fm is None:
        return ["SKILL.md has no frontmatter"], warnings
    if fm["name"] != expected:
        problems.append(f"name in SKILL.md is '{fm['name']}', expected '{expected}'")
    if not NAME_RE.match(fm["name"]) or len(fm["name"]) > 64:
        problems.append("name must be lowercase letters, numbers and hyphens, 64 max")
    if not fm["description"]:
        problems.append("missing description")
    elif len(fm["description"]) > 1024:
        problems.append(f"description is {len(fm['description'])} characters (limit 1024)")
    extra = [k for k in fm["keys"] if k not in SPEC_KEYS]
    if extra:
        warnings.append("extra frontmatter keys: " + ", ".join(extra))
    return problems, warnings


# ---------- building one skill ----------

def build(entry, checkout, out_root):
    src = checkout / entry["path"] if entry["path"] else checkout
    if not (src / "SKILL.md").exists():
        raise RuntimeError(f"SKILL.md not found at {entry['repo']}/{entry['path'] or '(root)'}")
    dest = out_root / entry["name"]
    if dest.exists():
        shutil.rmtree(dest)

    def ignore(d, names):
        return [n for n in names if n in SKIP_DIRS or (n.startswith(".") and Path(d, n).is_dir())]

    shutil.copytree(src, dest, ignore=ignore)
    # Keep the author's licence with the skill. MIT and Apache both ask for this.
    has_licence = any(p.name.upper().startswith("LICENSE") for p in dest.iterdir())
    lf = entry.get("license_file")
    if not has_licence and lf and (checkout / lf).exists():
        shutil.copy2(checkout / lf, dest / "LICENSE.txt")
    return dest


def zip_folder(folder, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(folder.rglob("*")):
            if p.is_file():
                z.write(p, Path(folder.name) / p.relative_to(folder))


def size_of(folder):
    return sum(p.stat().st_size for p in folder.rglob("*") if p.is_file())


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["install", "zip", "list"])
    ap.add_argument("--dest", help="install: skills folder (default ~/.claude/skills). zip: output folder (default ./skill-zips)")
    ap.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="path or URL of skills.json")
    ap.add_argument("--groups", default="core", help="comma list of groups (default: core)")
    ap.add_argument("--only", help="comma list of skill ids or names; overrides --groups")
    ap.add_argument("--update", action="store_true", help="install: replace skills that are already there")
    args = ap.parse_args()

    manifest = load_manifest(args.manifest)
    chosen = pick(manifest, set(args.groups.split(",")), args.only)

    if args.mode == "list":
        for s in manifest["skills"]:
            how = "fetch" if s.get("fetch") else ("plugin" if s["group"] == "role-packs" else "built in")
            print(f"{s['id']:<24} {s['group']:<11} {how:<9} {s['license']:<30} github.com/{s['repo']}/{s['path']}")
        return

    skipped = [s for s in chosen if not s.get("fetch")]
    todo = [s for s in chosen if s.get("fetch")]

    if args.mode == "install":
        dest = Path(args.dest).expanduser() if args.dest else Path.home() / ".claude" / "skills"
    else:
        dest = Path(args.dest).expanduser() if args.dest else Path.cwd() / "skill-zips"
    dest.mkdir(parents=True, exist_ok=True)

    results = []
    with tempfile.TemporaryDirectory(prefix="skillpack-") as tmp:
        tmp = Path(tmp)
        fetcher = Fetcher(tmp / "src")
        staging = tmp / "built"
        staging.mkdir()
        by_repo = {}
        for s in todo:
            by_repo.setdefault((s["repo"], s.get("ref", "main")), []).append(s)
        for (repo, ref), entries in by_repo.items():
            try:
                checkout = fetcher.get(repo, ref, sparse_paths(entries))
            except Exception as e:  # network, auth, missing ref
                for s in entries:
                    results.append((s, "FAILED", f"could not download {repo}: {e}"))
                continue
            for s in entries:
                try:
                    if args.mode == "install" and (dest / s["name"]).exists() and not args.update:
                        results.append((s, "SKIPPED", "already installed (use --update to replace)"))
                        continue
                    built = build(s, checkout, staging)
                    problems, warnings = check(built, s["name"])
                    if problems:
                        results.append((s, "FAILED", "; ".join(problems)))
                        continue
                    note = "; ".join(warnings)
                    kb = size_of(built) // 1024
                    if args.mode == "install":
                        target = dest / s["name"]
                        if target.exists():
                            shutil.rmtree(target)
                        shutil.copytree(built, target)
                        results.append((s, "INSTALLED", f"{target} ({kb} KB){'; ' + note if note else ''}"))
                    else:
                        zp = dest / f"{s['name']}.zip"
                        zip_folder(built, zp)
                        results.append((s, "ZIPPED", f"{zp} ({zp.stat().st_size // 1024} KB zipped){'; ' + note if note else ''}"))
                except Exception as e:
                    results.append((s, "FAILED", str(e)))

    for s in skipped:
        why = "built into the Claude app; in Claude Code use Anthropic's plugin" if s["group"] == "builtin" else "plugin; install from a plugin marketplace"
        results.append((s, "NOT FETCHED", why))

    width = max((len(s["name"]) for s, _, _ in results), default=10)
    for s, status, detail in results:
        print(f"{status:<11} {s['name']:<{width}}  {s['author']} ({s['license']})  {detail}")
    failed = [r for r in results if r[1] == "FAILED"]
    print(f"\n{sum(r[1] in ('INSTALLED', 'ZIPPED') for r in results)} done, "
          f"{sum(r[1] == 'SKIPPED' for r in results)} skipped, {len(failed)} failed.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
