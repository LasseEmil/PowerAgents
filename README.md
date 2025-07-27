# PowerAgents

This repository collects scaffolds and documentation for multiple LLM-driven development tools. Each scaffold mirrors the folder and instruction layout that the tool expects.

## Directory Structure

```text
.
├── docs/                # high-level background for each agent
│   ├── claude.md        # intro to Anthropic Claude Code
│   ├── codex.md         # intro to OpenAI Codex CLI
│   ├── gemini.md        # intro to Google Gemini CLI
│   ├── general-agent.md # notes on the generic pattern
│   └── kiro.md          # overview of AWS Kiro
├── scaffolds/           # example project layouts
│   ├── claude/          # sample Claude setup
│   ├── codex/           # sample Codex setup
│   ├── gemini/          # sample Gemini setup
│   ├── general-agent/   # minimal scaffold
│   └── kiro/            # Kiro spec-first files
├── examples/            # API demo projects
│   ├── claude/          # Python call to Claude API
│   ├── gemini/          # Python call to Gemini API
│   ├── openai/          # Python call to OpenAI API
│   ├── general-agent/   # barebones generic example
│   └── kiro/            # spec-first demo for Kiro
└── README.md            # repository overview
```

## Scaffolds Explained

| Directory                  | Tool                      | Notes                                                        |
| -------------------------- | ------------------------- | ------------------------------------------------------------ |
| `scaffolds/codex/`         | **OpenAI Codex CLI**      | Contains `AGENTS.md` and a sample `.codex/config.toml`.      |
| `scaffolds/gemini/`        | **Google Gemini CLI**     | Includes `GEMINI.md` and `.gemini/settings.json`.            |
| `scaffolds/claude/`        | **Anthropic Claude Code** | Provides `CLAUDE.md`, settings, and a command example.       |
| `scaffolds/kiro/`          | **AWS Kiro**              | Demonstrates `requirements.md`, `design.md`, and `tasks.md`. |
| `scaffolds/general-agent/` | Generic                   | Minimal setup for experimenting with new agents.             |

Additional background on each tool can be found in the `docs/` directory.
Detailed listings of the demo projects live in [examples.md](examples.md).

## Example Projects

The `examples/` folder contains small API demos for each LLM provider.

```
examples/
├── claude/          # Python call to Claude API
├── gemini/          # Python call to Gemini API
├── openai/          # Python call to OpenAI API
├── general-agent/   # Minimal layout for experiments
└── kiro/            # Spec-first AWS Kiro demo
```

Other ideas you could explore:

- **Django + Gemini** – run Gemini against a full-stack Django app.
- **FastAPI + OpenAI** – build an API layer that prompts OpenAI models.
- **Flask + Claude** – let Claude automate Flask app refactoring.
