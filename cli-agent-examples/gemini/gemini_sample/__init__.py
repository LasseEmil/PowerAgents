import os
import google.generativeai as genai


def send_prompt(prompt: str) -> str:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY", "test-key"))
    # Actual call would be genai.GenerativeModel(...)
    return f"gemini mock: {prompt}"
  
# Additional options for Gemini users:
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# response = chat.send_message(prompt)
# return response.text

# def classify_intent(text: str) -> str:
#     """Example classification use case."""
#     # return model.classify_text(text)
#     return "intent"
