#!/usr/bin/env python3
"""Rebuild the per-skill pages, the README skill list and CREDITS.md from skills.json.

Run after editing skills.json:  python tools/build_docs.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
M = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
PACK = M["repo"]
PACK_MKT = "agentic-brain-skill-pack"
GROUP_TITLES = {
    "core": "Core skills",
    "builtin": "Already in Claude",
    "role-packs": "Role packs (optional)",
}
GROUP_BLURB = {
    "core": "Writing, marketing and everyday skills. When you ask Claude to get all the skills, these are the ones it gets.",
    "builtin": "Anthropic's skills that come with the Claude app. In the app there's nothing to download: they're on already, or you switch them on. In Claude Code, Claude installs them for you.",
    "role-packs": "Anthropic plugins for a whole job: a set of skills, sometimes with connectors. Pick the one for your role.",
}


def source_url(s):
    base = f"https://github.com/{s['repo']}"
    return f"{base}/tree/{s['ref']}/{s['path']}" if s["path"] else base


def how_to_get(s):
    g, name = s["group"], s["name"]
    app, code = [], []
    if g == "core":
        if s.get("builtin_in_app") == "check-discover":
            app.append("First look in **Customize > Skills** for it under the skills from Anthropic. If it's there, switch it on and you're done.")
        lead = "Otherwise ask" if app else "Ask"
        app.append(f"{lead} Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `{name}.zip`; "
                   "upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.")
        app.append(f"Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `{PACK}`, then install **{name}**.")
        code.append(f"```\nclaude plugin marketplace add https://github.com/{PACK}.git\nclaude plugin install {name}@{PACK_MKT}\n```")
    elif g == "builtin" and s.get("builtin_in_app") == "automatic":
        app.append("Nothing to do. It's built in and loads by itself when you ask for this kind of file. "
                   "**Settings > Capabilities > Code execution and file creation** must be on (it is by default).")
        code.append("```\nclaude plugin marketplace add https://github.com/anthropics/skills.git\n"
                    "claude plugin install document-skills@anthropic-agent-skills\n```\n"
                    "That installs Anthropic's Word, Excel, PowerPoint and PDF skills together.")
    elif g == "builtin":
        app.append("Open **Customize > Skills**, find it among the skills from Anthropic, and switch it on.")
        code.append("Ask Claude to get all the skills from this pack (it's included in Claude Code), or:\n"
                    "```\nclaude plugin marketplace add https://github.com/anthropics/skills.git\n"
                    "claude plugin install example-skills@anthropic-agent-skills\n```\n"
                    "(`example-skills` brings a dozen of Anthropic's example skills, this one included.)")
    else:
        mkt = s["plugin"]["marketplace"]
        app.append(f"Works in Cowork and the Claude app. Open **Customize > Plugins**, find **{name}** from Anthropic and install it. "
                   f"If it isn't listed, choose **Add > Add marketplace**, enter `{mkt}`, then install **{name}**.")
        code.append(f"```\nclaude plugin marketplace add https://github.com/{mkt}.git\nclaude plugin install {name}@knowledge-work-plugins\n```")
    return app, code


def skill_page(s):
    lines = [f"# {s['title']}", ""]
    lines.append(f"By **[{s['author']}]({s['author_url']})**. Source: [{s['repo']}{'/' + s['path'] if s['path'] else ''}]({source_url(s)}). "
                 f"Licence: {s['license']}.")
    lines.append("")
    lines.append(f"{GROUP_TITLES[s['group']]} · {s['category']}")
    lines += ["", "## What it does", "", s["summary"], "", "## When to use it", ""]
    lines += [f"- {u}" for u in s["use_when"]]
    lines += ["", "## Try it", "", "```", s["try"], "```", "", "## How to get it", ""]
    app, code = how_to_get(s)
    lines.append("**Claude app (chat and Cowork)**")
    lines.append("")
    lines += [f"- {a}" for a in app]
    lines += ["", "**Claude Code**", ""] + code
    if s.get("notes"):
        lines += ["", "## Good to know", "", s["notes"]]
    lines += ["", "---", "",
              f"This page is our own description. The skill belongs to {s['author']}; get it from [the source]({source_url(s)}).", ""]
    return "\n".join(lines)


def readme_list():
    out = []
    for g in ["core", "builtin", "role-packs"]:
        items = [s for s in M["skills"] if s["group"] == g]
        out += [f"### {GROUP_TITLES[g]}", "", GROUP_BLURB[g], "",
                "| Skill | What it's for | By | Licence |", "|---|---|---|---|"]
        for s in items:
            first = s["summary"].split(". ")[0].rstrip(".") + "."
            out.append(f"| [{s['title']}](skills/{s['id']}.md) | {first} | [{s['author'].split(',')[0]}]({source_url(s)}) | {s['license']} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def credits():
    out = ["# Credits", "",
           "Every skill in this pack belongs to the people below. We link to their work and describe it in our own words; "
           "we don't copy or re-host any of it. When Claude fetches a skill for you, it downloads it from the author's repo "
           "and keeps the author's licence file with it.", ""]
    by_author = {}
    for s in M["skills"]:
        by_author.setdefault((s["author"], s["author_url"]), []).append(s)
    for (author, url), items in by_author.items():
        out += [f"## [{author}]({url})", ""]
        for s in items:
            out.append(f"- **{s['title']}**: [{s['repo']}{'/' + s['path'] if s['path'] else ''}]({source_url(s)}), {s['license']}")
        out.append("")
    out += ["## Licences in brief", "",
            "- **MIT** and **Apache-2.0**: free to use, change and share, as long as the copyright and licence notice go with it. That's why every fetched skill keeps its LICENSE file.",
            "- **Anthropic's Word, Excel, PowerPoint and PDF skills** are source-available, not open source. Use them inside Claude, where Anthropic provides them. Don't download or share copies.", ""]
    return "\n".join(out)


def main():
    (ROOT / "skills").mkdir(exist_ok=True)
    for s in M["skills"]:
        (ROOT / "skills" / f"{s['id']}.md").write_text(skill_page(s), encoding="utf-8", newline="\n")
    (ROOT / "CREDITS.md").write_text(credits(), encoding="utf-8", newline="\n")
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    new = re.sub(r"(<!-- skills:start -->\n).*?(<!-- skills:end -->)",
                 lambda m: m.group(1) + "\n" + readme_list() + "\n" + m.group(2), text, flags=re.S)
    readme.write_text(new, encoding="utf-8", newline="\n")
    print(f"Wrote {len(M['skills'])} skill pages, CREDITS.md and the README list.")


if __name__ == "__main__":
    main()
