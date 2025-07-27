import os
import openai

def send_prompt(prompt: str) -> str:
    """Send a prompt to the OpenAI API and return the response text."""
    openai.api_key = os.getenv("OPENAI_API_KEY", "test-key")
    # In a real project you'd call openai.ChatCompletion.create
    return f"mocked response for: {prompt}"
