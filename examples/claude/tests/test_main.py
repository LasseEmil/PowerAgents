from claude_sample import send_prompt

def test_send_prompt():
    assert send_prompt("test") == "claude mock: test"
