import os
import anthropic

client = anthropic.Client(api_key=os.getenv("CLAUDE_API_KEY", "test-key"))


def send_prompt(prompt: str) -> str:
    # Real code would call client.completions.create
    return f"claude mock: {prompt}"
