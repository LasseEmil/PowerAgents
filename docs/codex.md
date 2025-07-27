# OpenAI Codex CLI

OpenAI launched the Codex CLI in 2023 to bring its code-generating models directly into developer workflows. The tool reads `AGENTS.md` files from your repository and merges them with settings from `.codex/config.toml` to give the model persistent guidance.

Codex segments work into a plan, executes shell commands in a sandbox, and offers to commit changes once tests pass. It is designed to keep developers in control while automating repetitive tasks.

**Dependencies**

- Node.js and Git installed locally
- OpenAI API key in your environment

**Limitations & Pricing**

- Codex itself is open source, but it calls the paid OpenAI API
- Requests are billed per token; see OpenAI's pricing page
