"""Generic API demo."""

def run(prompt: str) -> str:
    return f"echo: {prompt}"

if __name__ == "__main__":
    print(run("hello"))
