import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_client() -> OpenAI:
    """Return an OpenAI-compatible client for the configured AI provider."""
    provider = os.getenv("AI_PROVIDER", "groq").strip().lower()

    if provider == "groq":
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY is not configured.")
        return OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
        )

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")
        return OpenAI(api_key=api_key)

    raise RuntimeError(
        f"Unsupported AI_PROVIDER={provider!r}. Use 'groq' or 'openai'."
    )


def ask_ai(prompt: str, instructions: str | None = None) -> str:
    """Send a text prompt through the configured AI provider."""
    provider = os.getenv("AI_PROVIDER", "groq").strip().lower()
    if provider == "groq":
        model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
    else:
        model = os.getenv("OPENAI_MODEL", "gpt-5")

    client = get_client()
    response = client.responses.create(
        model=model,
        instructions=instructions,
        input=prompt,
    )
    return response.output_text
