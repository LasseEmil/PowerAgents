"""Simple benchmark harness for agent samples."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

sys.path.append(str(ROOT / "cli-agent-examples" / "openai"))
sys.path.append(str(ROOT / "cli-agent-examples" / "gemini"))
sys.path.append(str(ROOT / "cli-agent-examples" / "claude"))

from openai_sample import send_prompt as openai_send  # type: ignore
from gemini_sample import send_prompt as gemini_send  # type: ignore
from claude_sample import send_prompt as claude_send  # type: ignore

PROMPTS = [
    line.strip()
    for line in (ROOT / "benchmark-tests" / "prompts.txt").read_text().splitlines()
    if line and not line.startswith("#")
]


def run() -> None:
    results_dir = ROOT / "benchmark-tests" / "results"
    results_dir.mkdir(exist_ok=True)
    out = []
    for prompt in PROMPTS:
        out.append(f"OpenAI: {openai_send(prompt)}")
        out.append(f"Gemini: {gemini_send(prompt)}")
        out.append(f"Claude: {claude_send(prompt)}")
    (results_dir / "latest.txt").write_text("\n".join(out))
    print("Benchmarks complete")


if __name__ == "__main__":
    run()
