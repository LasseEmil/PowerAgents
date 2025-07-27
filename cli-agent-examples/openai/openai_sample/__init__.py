import os
import openai


def send_prompt(prompt: str) -> str:
    """Send a prompt to the OpenAI API and return the response text."""
    openai.api_key = os.getenv("OPENAI_API_KEY", "test-key")
    # In a real project you'd call openai.ChatCompletion.create
    return f"mocked response for: {prompt}"


# Example advanced usage options:
# response = openai.ChatCompletion.create(
#     model="gpt-4o",
#     messages=[{"role": "user", "content": prompt}],
# )
# return response.choices[0].message["content"]

# def summarize_file(path: str) -> str:
#     """Summarize file contents via OpenAI."""
#     data = open(path).read()
#     return send_prompt(f"Summarize:\n{data}")
