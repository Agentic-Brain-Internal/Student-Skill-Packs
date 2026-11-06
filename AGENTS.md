# Instructions for AI agents

If someone asks you to get, download or install the skills from this repo, follow [INSTALL-FOR-CLAUDE.md](INSTALL-FOR-CLAUDE.md).

If you are editing the repo: `skills.json` is the source of truth. After changing it, run `python tools/build_docs.py` to rebuild `skills/*.md`, the README skill list and `CREDITS.md`, and keep `.claude-plugin/marketplace.json` in step with the core group. Never add skill files from other repos here.
