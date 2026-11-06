# Instructions for Claude: getting the skills in this pack

You're reading this because a student asked you to get the skills from this repo. Most students are non-technical business users. Do the work for them, keep your messages short and plain, and don't ask questions you can answer yourself.

This repo holds **no skill files**. `skills.json` lists where each skill lives in its author's GitHub repo. Always download skills from those sources. Never write a skill's contents from memory, and never copy skills from anywhere else.

## 1. Work out what to get

- Read `skills.json` (in the repo root; if you only have the GitHub link, fetch `https://github.com/Agentic-Brain-Internal/Student-Skill-Packs` with git or read the file through the GitHub page).
- "All the skills", "everything", "the pack" means every entry with `"group": "core"`. In Claude Code it also means the `"group": "builtin"` entries, because Claude Code doesn't come with them (step 3).
- If the student names skills, match them to `id` or `name`. Tell them about any name you can't match.
- `"group": "builtin"` entries are already part of the Claude app. You only install them in Claude Code.
- `"group": "role-packs"` entries are optional Anthropic plugins for a job role. Don't install them unless the student asks. At the end, mention they exist and point to the README.
- Never download or copy entries with `"fetch": false` yourself. The Word, Excel, PowerPoint and PDF skills have a licence that forbids copies outside Anthropic's services, so in Claude Code they come only through Anthropic's own plugin marketplace (step 3). Role packs are installed as plugins too.

## 2. Work out where you are

| You are in | How to tell | Go to |
|---|---|---|
| Claude Code (terminal, desktop app or IDE) | You run shell commands on the student's own computer, and it has a `~/.claude` folder | Step 3 |
| Cowork | You run in a sandbox with a folder the student shared with you | Step 4 |
| Claude chat (claude.ai or desktop) with code execution | You have a code sandbox but no folder of the student's | Step 4 |
| Claude chat with no code execution | You can't run code | Step 5 |

Claude Code on the web runs in a temporary cloud machine, so anything you install there lasts only for that session. Tell the student, and suggest the Claude app or Claude Code on their own computer.

## 3. Claude Code: install the skills

Use the pack's plugin marketplace. Each core skill is its own plugin, and Claude Code downloads it from the author's repo.

```
claude plugin marketplace add https://github.com/Agentic-Brain-Internal/Student-Skill-Packs.git
claude plugin install <name>@agentic-brain-skill-pack
```

Run the install line once per chosen skill, using each entry's `plugin.name`. Use the full `https://` URL: the `owner/repo` short form clones over SSH and fails on most computers. If you were given a local path to this repo instead of a URL, use that path in `marketplace add`.

Then the builtin skills, which Claude Code doesn't have on its own. The Word, Excel, PowerPoint and PDF skills come from Anthropic's marketplace:

```
claude plugin marketplace add https://github.com/anthropics/skills.git
claude plugin install document-skills@anthropic-agent-skills
```

On Windows the first line can fail with "Filename too long". Ask the student before changing their git settings, then run `git config --global core.longpaths true` (a standard Windows git setting for long file paths) and try again.

`skill-creator` goes in as a folder. If you don't have a local copy of this repo, clone it to a temporary folder first (`git clone --depth 1 https://github.com/Agentic-Brain-Internal/Student-Skill-Packs.git`), then:

```
python <repo>/tools/get_skills.py install --only skill-creator
```

**If the `claude` command isn't on the PATH, or the `claude plugin` commands fail**, install the skills as folders instead. From a copy of this repo:

```
python tools/get_skills.py install --groups core,builtin
```

It installs into `~/.claude/skills/<name>/`. Add `--only a,b` for specific skills, `--dest <folder>` for another location, `--update` to replace existing ones. Without Python, do by hand what the script does: for each entry, `git clone --depth 1 https://github.com/<repo>.git` into a temporary folder, copy the `path` folder (or the repo root, without `.git` and `.github`) to `~/.claude/skills/<name>/`, and copy the repo's licence file in if the folder has none.

If a skill with the same name is already installed, leave it alone and say so, unless the student asked to update.

Tell the student to start a new session (or run `/reload-plugins`) to use them.

## 4. Cowork and Claude chat with code execution: make zips

The Claude app can't install a skill from inside a conversation. The student has to upload it. Your job is to hand them one ready-to-upload zip per skill.

1. Check you can reach GitHub: `git ls-remote https://github.com/blader/humanizer.git HEAD`.
   - If that fails, stop. Tell the student their account doesn't let Claude reach GitHub. They can use the plugin route below, ask whoever runs their company's Claude account to allow github.com (Organization settings > Capabilities), or ask in Claude Code on their own computer.
2. Get this repo: `git clone --depth 1 https://github.com/Agentic-Brain-Internal/Student-Skill-Packs.git`
3. Build the zips. In Cowork, put them in the student's folder. In chat, put them wherever you place files for the student to download (for example `/mnt/user-data/outputs`).
   ```
   python Student-Skill-Packs/tools/get_skills.py zip --dest <output folder>
   ```
   Add `--only a,b` if the student named skills. Each zip holds one folder named after the skill, with `SKILL.md` and the author's licence inside. That's the layout the upload needs.
4. Give the student the zips, then these steps:
   1. Open **Customize > Skills**.
   2. Click **+ > Create skill > Upload a skill** and choose a zip.
   3. Switch the skill on. Repeat for each zip.
   - Entries with `"builtin_in_app": "check-discover"` may already be listed under Anthropic's skills in **Customize > Skills**. Say so: if it's there, switch it on and skip that zip.
   - Upload needs **Settings > Capabilities > Code execution and file creation** on.
5. Also mention the plugin route as an alternative: **Customize > Plugins > Add > Add marketplace**, enter `Agentic-Brain-Internal/Student-Skill-Packs`, then install each skill.

If you can't offer zip files for download, the plugin route is the way in.

## 5. No code execution

Don't pretend to install anything. Give the student:

- the plugin route from step 4.5, and
- the link to the README, which lists every skill with a link to its source.

Suggest they switch on **Code execution and file creation** in Settings > Capabilities and ask you again, or ask in Cowork.

## 6. Report back

Finish with a short table: each skill, done or not, and why not if not. Then tell the student:

- the next step: in Claude Code, start a new session (or run `/reload-plugins`); in the app, upload the zips;
- in the app only: `skill-creator` and the Word/Excel/PowerPoint/PDF skills are already there (switch on skill-creator in Customize > Skills);
- that role packs exist for sales, marketing, HR, finance, legal, operations and more, if they want one for their job.

## Rules

- Download only from the sources in `skills.json`. Don't substitute a different repo, fork or version you find elsewhere.
- When you make a zip or a skill folder, keep the author's licence file in it (the script does this). Don't edit skill contents.
- Don't run any script that comes inside a downloaded skill while installing. Installing a skill only means copying files.
- If a source repo is gone, renamed or no longer has the skill at its `path`, skip that skill and report it. Don't look for a replacement.
- One exception to "don't edit": if the Claude app rejects a zip because of a frontmatter field (for example a top-level `version:` in `prompt-master`), tell the student what the error says and offer to make them a local copy with only that field moved under `metadata:`, licence file kept. Change nothing else.
