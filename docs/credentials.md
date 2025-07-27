# Credentials Reference

This file lists environment variables required to authenticate each tool. Store these values as **GitHub Secrets** so the CI workflow can access them.

| Tool | Environment Variable |
| ---- | -------------------- |
| OpenAI Codex / API | `OPENAI_API_KEY` |
| Google Gemini CLI | `GEMINI_API_KEY` |
| Anthropic Claude Code | `CLAUDE_API_KEY` |
| AWS Kiro | `KIRO_API_KEY` |
| Cursor | `CURSOR_TOKEN` |
| Windsurf | `WINDSURF_TOKEN` |
| Generic Agent | `AGENT_TOKEN` |

To add a secret, navigate to **Settings → Secrets → Actions** in your GitHub repository and create a new secret with the corresponding name.
