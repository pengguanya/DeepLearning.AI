# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains Jupyter notebooks and transcripts from the [DeepLearning.AI "LangChain for LLM Application Development"](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) short course by Harrison Chase and Andrew Ng.

## Folder Structure

```
├── course_materials/          # Original course content (read-only reference)
│   ├── notebooks/             # L*-*.ipynb lesson notebooks
│   └── transcripts/           # Transcript_*.txt files
├── my_work/                   # Hands-on experiments & practice
│   ├── 01_models_prompts_parsers/
│   ├── 02_memory/
│   ├── 03_chains/
│   ├── 04_qna/
│   ├── 05_evaluation/
│   ├── 06_agents/
│   └── projects/              # Cross-lesson experiments
├── shared/                    # Reusable helpers
│   └── config.py              # .env loading, get_chat_model() helper
├── pyproject.toml             # uv project config
└── .env                       # OPENAI_API_KEY (gitignored)
```

## Environment & Workflow

- **Package manager:** `uv` (managed via `pyproject.toml`)
- **Run terminal scripts:** `uv run python my_work/01_models_prompts_parsers/practice.py`
- **Run Jupyter:** `uv run jupyter lab`
- **Add packages:** `uv add <package>`
- **Jupyter kernel:** `langchain-course`

## LangChain API Conventions

Use the modern LangChain API in all new code:

```python
# Imports
from langchain_openai import ChatOpenAI          # NOT langchain.chat_models
from langchain_core.messages import HumanMessage  # NOT langchain.schema

# Invocation
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)
response = llm.invoke([HumanMessage(content="Hello")])  # NOT llm(messages)
```

The original course notebooks in `course_materials/` use older APIs — refer to them for concepts, but use modern syntax in `my_work/`.

## Shared Config

Use `shared.config` to avoid boilerplate:

```python
from shared.config import get_chat_model
llm = get_chat_model()  # loads .env, returns ChatOpenAI with defaults
```

Override model via `LLM_MODEL` env var or `get_chat_model(model="gpt-4o")`.

## Key Notes

- Default model is `gpt-3.5-turbo` with `temperature=0.0` for reproducibility.
- `.env` must contain `OPENAI_API_KEY`.
