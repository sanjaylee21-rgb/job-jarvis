import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")
    return OpenAI(api_key=api_key)


def ask_ai(prompt: str, instructions: str | None = None) -> str:
    client = get_client()
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        instructions=instructions,
        input=prompt,
    )
    return response.output_text
