from gemini_sample import send_prompt

def test_send_prompt():
    assert send_prompt("test") == "gemini mock: test"
