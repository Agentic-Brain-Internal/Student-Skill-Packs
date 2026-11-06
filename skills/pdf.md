# PDF files

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/pdf](https://github.com/anthropics/skills/tree/main/skills/pdf). Licence: Proprietary (source-available).

Already in Claude · Documents

## What it does

How Claude reads, splits, merges and fills in PDFs, and pulls text and tables out of them. Already on in the Claude app.

## When to use it

- You need the tables out of a supplier PDF and into a spreadsheet.
- You want PDFs merged, split or a form filled in.

## Try it

```
Pull the price table out of this PDF catalogue and put it in a spreadsheet.
```

## How to get it

**Claude app (chat and Cowork)**

- Nothing to do. It's built in and loads by itself when you ask for this kind of file. **Settings > Capabilities > Code execution and file creation** must be on (it is by default).

**Claude Code**

```
claude plugin marketplace add https://github.com/anthropics/skills.git
claude plugin install document-skills@anthropic-agent-skills
```
That installs Anthropic's Word, Excel, PowerPoint and PDF skills together.

## Good to know

Same licence as the Word skill: use it inside Claude, don't copy it.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/pdf).
