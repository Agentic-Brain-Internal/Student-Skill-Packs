# Discernment Nudge

By **[Anthropic](https://www.anthropic.com)**. Source: [anthropics/skills/skills/discernment-nudge](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge). Licence: Apache-2.0.

Core skills · Thinking

## What it does

After Claude gives you an answer you might act on (advice, a plan, numbers, a claim), it adds two or three short questions to help you check it: what to verify, where the reasoning could be weak, what context it might be missing.

## When to use it

- You use Claude for decisions, estimates or facts you'll repeat to others.
- You're new to AI and want help building the habit of checking its work.

## Try it

```
Estimate how many extra delivery drivers we need if orders go up 20% in spring.
```

## How to get it

**Claude app (chat and Cowork)**

- First look in **Customize > Skills** for it under the skills from Anthropic. If it's there, switch it on and you're done.
- Otherwise ask Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `discernment-nudge.zip`; upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.
- Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `Agentic-Brain-Internal/Student-Skill-Packs`, then install **discernment-nudge**.

**Claude Code**

```
claude plugin marketplace add https://github.com/Agentic-Brain-Internal/Student-Skill-Packs.git
claude plugin install discernment-nudge@agentic-brain-skill-pack
```

## Good to know

It runs by itself after big answers. Switch it off if you find the questions get in the way.

---

This page is our own description. The skill belongs to Anthropic; get it from [the source](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge).
