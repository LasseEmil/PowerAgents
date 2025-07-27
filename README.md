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
│   ├── windsurf.md
│   └── credentials.md       # environment variables
├── scaffolds/                 # example project layouts
│   ├── claude/
│   ├── codex/
│   ├── cursor/
│   ├── gemini/
│   ├── general-agent/
│   ├── kiro/
│   └── windsurf/
├── benchmark-tests/         # prompt benchmarks and results
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


Additional background on each tool can be found in the `docs/` directory. Details about each demo live in [cli-agent-examples.md](cli-agent-examples.md) and [ai-ide-examples.md](ai-ide-examples.md).

## Example Projects

The demos are split by category. See the linked markdown files for a tree view of each folder.

## Credentials

Required API keys are documented in [docs/credentials.md](docs/credentials.md). Store
these values as GitHub Secrets so the workflow can access them during tests.

## Benchmark Tests

The `benchmark-tests/` directory contains a small harness that exercises each
example using prompts from `prompts.txt`. Results are written to
`benchmark-tests/results/latest.txt` by the GitHub Actions workflow.

