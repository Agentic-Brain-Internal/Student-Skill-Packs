# Word documents

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx). Licence: Proprietary (source-available).

Already in Claude · Documents

## What it does

How Claude makes and edits Word files: headings, tables, page numbers, tracked changes, letterheads. In the Claude app it's already on and loads by itself whenever you ask for a Word document.

## When to use it

- You ask for a report, letter, policy or proposal as a .docx.
- You upload a Word file and want it edited, with changes tracked.

## Try it

```
Make this into a two-page Word document with a title page and a table of contents.
```

## How to get it

**Claude app (chat and Cowork)**

- Nothing to do. It's built in and loads by itself when you ask for this kind of file. **Settings > Capabilities > Code execution and file creation** must be on. It usually is; if you can't switch it on, ask whoever runs your company's Claude account.

**Claude Code**

```
claude plugin marketplace add https://github.com/anthropics/skills.git
claude plugin install document-skills@anthropic-agent-skills
```
That installs Anthropic's Word, Excel, PowerPoint and PDF skills together. On Windows, if the first line fails with "Filename too long", run `git config --global core.longpaths true` and try again.

## Good to know

Anthropic's licence for this skill does not allow copies outside Claude. Don't download or re-share it; use it where Anthropic provides it.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/docx).
