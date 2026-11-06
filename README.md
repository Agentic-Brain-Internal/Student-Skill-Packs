# Claude Skill Pack

A hand-picked set of public Claude skills for students of the Agentic Brain Claude course, with a short guide to each one in plain English.

Nothing in here is a copy of someone else's skill. This repo is a list of links plus our own notes. When you ask Claude to get the skills, it downloads each one straight from the person who made it, with their licence, and the [credits](CREDITS.md) name every author.

## Get the skills

Paste this into Claude:

```
Get all the skills from https://github.com/OWNER/claude-skill-pack and set them up for me. Follow the instructions in its INSTALL-FOR-CLAUDE.md.
```

What happens next depends on where you ask.

**Claude Code.** Claude installs everything for you. Start a new session afterwards and the skills are ready.

**Cowork.** Pick a folder for the task first. Claude downloads each skill and saves it as a zip in that folder. Then upload the zips yourself:

1. Open **Customize > Skills**.
2. Click **+ > Create skill > Upload a skill** and choose one zip.
3. Switch the skill on. Repeat for each zip.

**Claude chat (claude.ai or the desktop app).** Same as Cowork: Claude makes the zips and gives them to you to download, then you upload them. Claude needs to be able to reach GitHub for this. If it says it can't, use Cowork, or ask whoever runs your company's Claude account to allow github.com (Organization settings > Capabilities).

**Another way: install as plugins.** In the Claude app, open **Customize > Plugins > Add > Add marketplace** and enter `OWNER/claude-skill-pack`. Each skill in the core list is there as its own plugin, which installs straight from its author's repo. Install the ones you want.

Uploading skills needs **Code execution and file creation** switched on in **Settings > Capabilities**. It's on by default.

### Only want some?

Name them:

```
Get the humanizer and stop-slop skills from https://github.com/OWNER/claude-skill-pack and set them up for me.
```

## The skills

<!-- skills:start -->

### Core skills

Writing, marketing and everyday skills. When you ask Claude to get all the skills, these are the ones it gets.

| Skill | What it's for | By | Licence |
|---|---|---|---|
| [Humanizer](skills/humanizer.md) | Rewrites text that sounds like AI wrote it so it reads like a person wrote it, without changing what it says. | [Siqi Chen](https://github.com/blader/humanizer) | MIT |
| [Stop Slop](skills/stop-slop.md) | A short, strict set of rules for writing that doesn't sound machine-made: cut filler, use active voice, name specific things, vary sentence length, no em dashes. | [Hardik Pandya](https://github.com/hardikpandya/stop-slop) | MIT |
| [Prompt Master](skills/prompt-master.md) | Writes a tight, ready-to-paste prompt for another AI tool: ChatGPT, Gemini, Midjourney, an image or video tool, and so on. | [Nidhin Joseph Nelson](https://github.com/nidhinjs/prompt-master) | MIT |
| [Copywriting](skills/copywriting.md) | Writes marketing copy for web pages: home page, landing page, pricing, product and about pages. | [Corey Haines](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) | MIT |
| [Copy Editing](skills/copy-editing.md) | Edits copy you already have instead of starting over. | [Corey Haines](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copy-editing) | MIT |
| [Email Sequences](skills/emails.md) | Plans and writes a series of emails: welcome emails, follow-ups after a quote, win-back emails for lapsed customers. | [Corey Haines](https://github.com/coreyhaines31/marketingskills/tree/main/skills/emails) | MIT |
| [Social Media](skills/social.md) | Writes and plans posts for LinkedIn, X, Instagram, TikTok and Facebook. | [Corey Haines](https://github.com/coreyhaines31/marketingskills/tree/main/skills/social) | MIT |
| [Customer Research](skills/customer-research.md) | Turns raw customer material into findings: interview notes, survey answers, reviews, support tickets. | [Corey Haines](https://github.com/coreyhaines31/marketingskills/tree/main/skills/customer-research) | MIT |
| [Internal Comms](skills/internal-comms.md) | Writes the messages that go around a company: status reports, leadership updates, project updates, newsletters, FAQs and incident reports. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/internal-comms) | Apache-2.0 |
| [Theme Factory](skills/theme-factory.md) | Gives decks, documents and pages a consistent look. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | Apache-2.0 |
| [Canvas Design](skills/canvas-design.md) | Makes one-page visual pieces as PNG or PDF: posters, flyers, simple graphics. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Apache-2.0 |
| [Discernment Nudge](skills/discernment-nudge.md) | After Claude gives you an answer you might act on (advice, a plan, numbers, a claim), it adds two or three short questions to help you check it: what to verify, where the reasoning could be weak, what context it might be missing. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge) | Apache-2.0 |

### Already in Claude

Anthropic's skills that come with the Claude app. In the app there's nothing to download: they're on already, or you switch them on. In Claude Code, Claude installs them for you.

| Skill | What it's for | By | Licence |
|---|---|---|---|
| [Skill Creator](skills/skill-creator.md) | Builds new skills with you, and tests and improves the ones you have. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Apache-2.0 |
| [Word documents](skills/docx.md) | How Claude makes and edits Word files: headings, tables, page numbers, tracked changes, letterheads. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/docx) | Proprietary (source-available) |
| [Excel spreadsheets](skills/xlsx.md) | How Claude reads, cleans and builds spreadsheets with working formulas, formatting and charts. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Proprietary (source-available) |
| [PowerPoint decks](skills/pptx.md) | How Claude makes and edits PowerPoint decks, including working from your own template. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/pptx) | Proprietary (source-available) |
| [PDF files](skills/pdf.md) | How Claude reads, splits, merges and fills in PDFs, and pulls text and tables out of them. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/pdf) | Proprietary (source-available) |

### Role packs (optional)

Anthropic plugins for a whole job: a set of skills, sometimes with connectors. Pick the one for your role.

| Skill | What it's for | By | Licence |
|---|---|---|---|
| [Productivity (plugin)](skills/kwp-productivity.md) | Helps you plan the day, keep a task list and build up notes about your work that Claude remembers between sessions. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/productivity) | Apache-2.0 |
| [Brand Voice (plugin)](skills/kwp-brand-voice.md) | Works out your company's voice from documents you already have (past emails, proposals, call notes), writes brand guidelines from them, then checks new writing against those guidelines. | [Tribe AI](https://github.com/anthropics/knowledge-work-plugins/tree/main/partner-built/brand-voice) | Apache-2.0 |
| [Marketing (plugin)](skills/kwp-marketing.md) | Campaign plans, content drafts, email sequences, competitor briefs, SEO checks and performance reports, plus a brand review of anything before it goes out. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing) | Apache-2.0 |
| [Sales (plugin)](skills/kwp-sales.md) | Account research, call prep, call summaries with follow-up emails, pipeline and deal reviews, and outreach drafts. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales) | Apache-2.0 |
| [Customer Support (plugin)](skills/kwp-customer-support.md) | Sorts and prioritises tickets, drafts replies, writes escalation notes and turns solved problems into help articles. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support) | Apache-2.0 |
| [Operations (plugin)](skills/kwp-operations.md) | Process write-ups, status reports, risk assessments, vendor reviews, change requests and capacity plans. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/operations) | Apache-2.0 |
| [Human Resources (plugin)](skills/kwp-human-resources.md) | Job offers, interview plans, onboarding plans, performance review drafts, policy look-ups and people reports. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/human-resources) | Apache-2.0 |
| [Finance (plugin)](skills/kwp-finance.md) | Month-end close, reconciliations, journal entries, variance analysis and financial statements, for in-house finance teams. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance) | Apache-2.0 |
| [Legal (plugin)](skills/kwp-legal.md) | Contract review, NDA triage, compliance checks and meeting briefings, for in-house legal teams. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) | Apache-2.0 |
| [Small Business (plugin)](skills/kwp-small-business.md) | Everyday jobs for owners of small firms: chasing invoices, cash-flow snapshots, proposals, job adverts, review replies, month-end prep and a Monday briefing. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business) | Apache-2.0 |
| [Product Management (plugin)](skills/kwp-product-management.md) | Feature specs, roadmap updates, stakeholder updates, competitor briefs and summaries of user research. | [Anthropic](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) | Apache-2.0 |

<!-- skills:end -->

## Using a skill

Same as in Lesson 7. Ask for the task in plain words and the right skill kicks in, or type `/` and pick the skill by name to make sure it's used.

A few skills in this pack do similar jobs: humanizer and stop-slop both clean up AI-sounding writing, and Corey Haines's marketing skills overlap with Anthropic's marketing plugin. If Claude picks the wrong one, name the one you want, or switch one off.

## Keeping them up to date

Authors improve their skills over time.

- **Plugins** update from **Customize > Plugins** (or `claude plugin marketplace update` in Claude Code).
- **Uploaded zips** don't update by themselves. Ask Claude to get the skills again, then upload the new zip over the old skill.

## Before you rely on a skill

A skill is a set of instructions Claude follows, and some include small scripts. We checked the source and licence of each one before listing it. Skills come straight from their authors, so they can change after we checked them. Read a skill before you lean on it for real work, as you would any template from the internet. If your company has rules about adding tools, check with whoever runs your Claude account first.

## Credits

Every skill belongs to its author. See [CREDITS.md](CREDITS.md) for who made what and under which licence. The descriptions in [skills/](skills/) are our own.

Made by [Agentic Brain](https://agenticbrain.com) for the Claude course.
