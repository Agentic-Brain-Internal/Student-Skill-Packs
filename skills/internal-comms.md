# Internal Comms

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms). Licence: Apache-2.0.

Core skills · Writing

## What it does

Writes the messages that go around a company: status reports, leadership updates, project updates, newsletters, FAQs and incident reports. It comes with example formats, including 'Progress, Plans, Problems' updates.

## When to use it

- You owe your manager a weekly update.
- Something went wrong and you need a clear incident write-up.

## Try it

```
Write this week's project update in Progress, Plans, Problems format from these notes: ...
```

## How to get it

**Claude app (chat and Cowork)**

- First look in **Customize > Skills** for it under the skills from Anthropic. If it's there, switch it on and you're done.
- Otherwise ask Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `internal-comms.zip`; upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.
- Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `Agentic-Brain-Internal/Student-Skill-Packs`, then install **internal-comms**.

**Claude Code**

```
claude plugin marketplace add https://github.com/Agentic-Brain-Internal/Student-Skill-Packs.git
claude plugin install internal-comms@agentic-brain-skill-pack
```

## Good to know

Its examples come from Anthropic's own company. Tell it your format once and it will follow yours.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/internal-comms).
