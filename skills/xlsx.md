# Excel spreadsheets

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx). Licence: Proprietary (source-available).

Already in Claude · Documents

## What it does

How Claude reads, cleans and builds spreadsheets with working formulas, formatting and charts. Already on in the Claude app.

## When to use it

- You upload a spreadsheet and want it analysed, fixed or reformatted.
- You want a new tracker, budget or price list as a real Excel file.

## Try it

```
Build me an Excel tracker for supplier deliveries with a column for days late that calculates itself.
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

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/xlsx).
