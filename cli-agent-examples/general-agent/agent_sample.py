"""Generic API demo."""


def run(prompt: str) -> str:
    return f"echo: {prompt}"


# Future extensions:
# def run_with_memory(prompt: str, history: list[str]) -> str:
#     """Example of keeping conversation context."""
#     return "todo"

# def batch_prompts(prompts: list[str]) -> list[str]:
#     return [run(p) for p in prompts]


if __name__ == "__main__":
    print(run("hello"))
