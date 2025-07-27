# PowerAgents

This repository collects scaffolds and documentation for multiple LLM-driven development tools. Each scaffold mirrors the layout that the tool expects.

## Directory Structure

```text
.
├── docs/                      # high-level background for each agent
│   ├── claude.md
│   ├── codex.md
│   ├── cursor.md
│   ├── gemini.md
│   ├── general-agent.md
│   ├── kiro.md
│   └── windsurf.md
├── scaffolds/                 # example project layouts
│   ├── claude/
│   ├── codex/
│   ├── cursor/
│   ├── gemini/
│   ├── general-agent/
│   ├── kiro/
│   └── windsurf/
├── cli-agent-examples/        # CLI oriented samples
│   ├── claude/
│   ├── gemini/
│   ├── general-agent/
│   └── openai/
├── ai-ide-examples/           # IDE based samples
│   ├── cursor/
│   ├── kiro/
│   └── windsurf/
├── tools/
│   ├── tool_template.jinja
│   └── tools.md
├── cli-agent-examples.md      # details for CLI demos
├── ai-ide-examples.md         # details for IDE demos
└── README.md
```

## Scaffolds Explained

| Directory                  | Tool                      | Notes                                                        |
| -------------------------- | ------------------------- | ------------------------------------------------------------ |
| `scaffolds/codex/`         | **OpenAI Codex CLI**      | Contains `AGENTS.md` and a sample config.                    |
| `scaffolds/gemini/`        | **Google Gemini CLI**     | Includes `GEMINI.md` and settings.                           |
| `scaffolds/claude/`        | **Anthropic Claude Code** | Provides `CLAUDE.md` and an example command.                 |
| `scaffolds/kiro/`          | **AWS Kiro**              | Demonstrates `requirements.md`, `design.md`, and `tasks.md`. |
| `scaffolds/cursor/`        | **Cursor IDE**            | Minimal notes for using Cursor's agent mode.                 |
| `scaffolds/windsurf/`      | **Windsurf IDE**          | Shows how to steer the Cascade agent.                        |
| `scaffolds/general-agent/` | Generic                   | Minimal setup for experimenting with new agents.             |

Additional background on each tool can be found in the `docs/` directory. Details about each demo live in [cli-agent-examples.md](cli-agent-examples.md) and [ai-ide-examples.md](ai-ide-examples.md).

## Tool Categories

The tools in this repo fall into two umbrellas.

### Agentic CLI Tools

| Tool          | Notes                                            |
| ------------- | ------------------------------------------------ |
| Codex CLI     | Chat-driven agent that edits code via terminal   |
| Gemini CLI    | Google open-source CLI with built-in MCP support |
| Claude Code   | Anthropic CLI focused on explore-plan-code flows |
| Generic Agent | Placeholder for experimental CLIs                |

### AI-Integrated Development Environments

| Tool     | Notes                                   |
| -------- | --------------------------------------- |
| AWS Kiro | Spec-first IDE powered by Claude 4      |
| Cursor   | VS Code fork with background agent mode |
| Windsurf | Enterprise IDE with cascade agent       |

## Example Projects

The demos are split by category. See the linked markdown files for a tree view of each folder.

```
cli-agent-examples/   # CLI examples
ai-ide-examples/      # IDE examples
```
