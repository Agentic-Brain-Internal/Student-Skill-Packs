# Canvas Design

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design). Licence: Apache-2.0.

Core skills · Design

## What it does

Makes one-page visual pieces as PNG or PDF: posters, flyers, simple graphics. It picks a design direction first, then builds the piece to match, with a set of fonts included.

## When to use it

- You need a poster for the staff room or a flyer for an open day.
- You want a simple graphic without opening a design tool.

## Try it

```
Design an A4 poster for our trade open day on 14 March, 7am to 11am, free breakfast.
```

## How to get it

**Claude app (chat and Cowork)**

- First look in **Customize > Skills** for it under the skills from Anthropic. If it's there, switch it on and you're done.
- Otherwise ask Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `canvas-design.zip`; upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.
- Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `OWNER/claude-skill-pack`, then install **canvas-design**.

**Claude Code**

```
claude plugin marketplace add https://github.com/OWNER/claude-skill-pack.git
claude plugin install canvas-design@agentic-brain-skill-pack
```

## Good to know

It's the largest download in the pack because of the fonts it carries.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/canvas-design).
