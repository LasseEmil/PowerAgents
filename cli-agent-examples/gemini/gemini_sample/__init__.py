import os
import google.generativeai as genai


def send_prompt(prompt: str) -> str:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY", "test-key"))
    # Actual call would be genai.GenerativeModel(...)
    return f"gemini mock: {prompt}"
