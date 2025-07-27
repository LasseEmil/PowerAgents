# AWS Kiro

Kiro is Amazon's entrant into the "agentic IDE" space, publicly previewed in mid‑2025. The tool aims to eliminate "vibe coding" by turning every feature request into structured specs: `requirements.md`, `design.md`, and `tasks.md`.

Under the hood Kiro runs on Anthropic's Claude 4 Sonnet via the AgentCore runtime. It can execute multi-step plans, integrate with MCP servers, and keep specs in sync as code evolves. Steering documents in `.kiro/steering/` let teams enforce persistent rules across all sessions.

**Dependencies**

- AWS account with access to Bedrock
- VS Code or JetBrains IDE with the Kiro extension installed

**Limitations & Pricing**

- Free while in public preview
- Will charge for Claude 4 usage once generally available
