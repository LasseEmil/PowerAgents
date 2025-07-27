import os
import anthropic

client = anthropic.Client(api_key=os.getenv("CLAUDE_API_KEY", "test-key"))


def send_prompt(prompt: str) -> str:
    # Real code would call client.completions.create
    return f"claude mock: {prompt}"


# More advanced Claude use cases:
# with client.messages.stream(model="claude-3", messages=[{"role": "user", "content": prompt}]) as resp:
#     for chunk in resp:
#         print(chunk)

# def analyze_log(file_path: str) -> str:
#     data = open(file_path).read()
#     return send_prompt(f"Analyze errors in:\n{data}")
