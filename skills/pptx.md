# PowerPoint decks

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx). Licence: Proprietary (source-available).

Already in Claude · Documents

## What it does

How Claude makes and edits PowerPoint decks, including working from your own template. Already on in the Claude app.

## When to use it

- You need a deck from notes, a report or a meeting summary.
- You want an existing deck updated or reworked.

## Try it

```
Turn this quarterly report into a 6-slide PowerPoint for the leadership meeting.
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

Same licence as the Word skill: use it inside Claude, don't copy it.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/pptx).
