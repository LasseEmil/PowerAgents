# Anthropic Claude Code

Anthropic released Claude Code to provide an agentic development experience powered by Claude models. The agent reads layered `CLAUDE.md` files and settings from `.claude/settings.json` to understand your project's boundaries.

Claude Code encourages an explore-plan-code workflow and can run reusable commands stored in `.claude/commands/`. Tool permissions are managed through the settings file, keeping automated changes safe and auditable.

**Dependencies**

- Go or Python runtime (depending on your project)
- Git and access to Anthropic's API

**Limitations & Pricing**

- Claude Code is currently closed-source
- Requires a paid Anthropic API plan
