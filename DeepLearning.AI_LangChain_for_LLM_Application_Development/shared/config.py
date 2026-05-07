"""Shared configuration for LangChain course work."""

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env from project root
_project_root = Path(__file__).resolve().parent.parent
load_dotenv(_project_root / ".env")


def get_chat_model(
    model: str | None = None,
    temperature: float = 0.0,
    **kwargs,
) -> ChatOpenAI:
    """Return a ChatOpenAI instance with sensible defaults.

    Uses the LLM_MODEL env var if set, otherwise falls back to gpt-3.5-turbo.
    """
    model = model or os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    return ChatOpenAI(model=model, temperature=temperature, **kwargs)
