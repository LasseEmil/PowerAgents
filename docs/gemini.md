# Google Gemini CLI

Google's Gemini CLI appeared in 2024 as an open-source project that embeds Gemini models in your editor. Instructions reside in a `GEMINI.md` file and user credentials live in `.gemini/settings.json`.

During a run, Gemini may call built-in shell commands or any MCP tools you register. It streams results back to the chat, loops on failing tests, and can open GitHub pull requests when work is complete.

**Dependencies**

- Python 3.10+
- Git and a valid Google Cloud account

**Limitations & Pricing**

- The CLI is Apache-2 licensed, but Gemini API usage requires billing
- Some features (like GitHub PR integration) need additional permissions
