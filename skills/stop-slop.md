# Stop Slop

By **[Hardik Pandya](https://hvpandya.com)**. Source: [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop). Licence: MIT.

Core skills · Writing

## What it does

A short, strict set of rules for writing that doesn't sound machine-made: cut filler, use active voice, name specific things, vary sentence length, no em dashes. It comes with lists of phrases and sentence shapes to avoid, and scores a draft before handing it back.

## When to use it

- You want Claude to write in a plain, direct voice from the start, not fix it afterwards.
- You're editing a draft and want a checklist-style pass.

## Try it

```
Write a two-paragraph update to the team about the new delivery schedule. Use the stop-slop rules.
```

## How to get it

**Claude app (chat and Cowork)**

- Ask Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `stop-slop.zip`; upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.
- Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `Agentic-Brain-Internal/claude-skill-pack`, then install **stop-slop**.

**Claude Code**

```
claude plugin marketplace add https://github.com/Agentic-Brain-Internal/claude-skill-pack.git
claude plugin install stop-slop@agentic-brain-skill-pack
```

## Good to know

Overlaps with humanizer. Stop-slop is stricter and shorter; humanizer explains more.

---

This page is our own description. The skill belongs to Hardik Pandya; get it from [the source](https://github.com/hardikpandya/stop-slop).
