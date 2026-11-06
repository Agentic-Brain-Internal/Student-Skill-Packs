# PowerPoint Template Creator

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/financial-services/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator). Licence: Apache-2.0.

Core skills · Documents

## What it does

Turns your company's PowerPoint template into a skill of its own. Give it your .pptx or .potx file and it studies the layouts and where everything sits, then builds a skill that makes on-brand decks from that template every time.

## When to use it

- Claude's decks don't match your company look and you want them to.
- You make the same kind of deck often (board packs, client proposals, monthly reviews) and want it on your template without fixing it by hand.

## Try it

```
Use the ppt-template-creator skill to turn this template into a skill for our company decks. [attach your .pptx or .potx]
```

## How to get it

**Claude app (chat and Cowork)**

- Ask Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `ppt-template-creator.zip`; upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.
- Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `Agentic-Brain-Internal/Student-Skill-Packs`, then install **ppt-template-creator**.

**Claude Code**

```
claude plugin marketplace add https://github.com/Agentic-Brain-Internal/Student-Skill-Packs.git
claude plugin install ppt-template-creator@agentic-brain-skill-pack
```

## Good to know

It makes a skill, not a deck. When it's done, upload the new skill like any other (Customize > Skills), then ask for decks as usual. It uses Skill Creator along the way, so switch that on too. It comes from Anthropic's financial-services collection but works for any company template.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/ppt-template-creator).
