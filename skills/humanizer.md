# Humanizer

By **[Siqi Chen](https://github.com/blader)**. Source: [blader/humanizer](https://github.com/blader/humanizer). Licence: MIT.

Core skills · Writing

## What it does

Rewrites text that sounds like AI wrote it so it reads like a person wrote it, without changing what it says. It works from Wikipedia's guide to the signs of AI writing: forced lists of three, 'it's not X, it's Y' lines, puffed-up claims, stock words and one-line closers.

## When to use it

- You drafted an email, post or report with Claude and it sounds like a chatbot.
- You want to check someone else's draft for AI tells before it goes out.

## Try it

```
Use the humanizer skill on this draft. Keep the meaning and the facts exactly as they are.
```

## How to get it

**Claude app (chat and Cowork)**

- Ask Claude to get it for you (see the [README](../README.md#get-the-skills)). Claude makes the file `humanizer.zip`; upload it in **Customize > Skills > + > Create skill > Upload a skill**, then switch it on.
- Or install it as a plugin: **Customize > Plugins > Add > Add marketplace**, enter `OWNER/claude-skill-pack`, then install **humanizer**.

**Claude Code**

```
claude plugin marketplace add https://github.com/OWNER/claude-skill-pack.git
claude plugin install humanizer@agentic-brain-skill-pack
```

## Good to know

Overlaps with stop-slop. Both are good; if Claude picks the wrong one, name the one you want.

---

This page is our own description. The skill belongs to Siqi Chen; get it from [the source](https://github.com/blader/humanizer).
