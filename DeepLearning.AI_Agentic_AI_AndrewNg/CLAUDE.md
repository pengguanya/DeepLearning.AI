# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains course materials from DeepLearning.AI's "Agentic AI" course by Andrew Ng. Currently includes Module 5: "Patterns for Highly Autonomous Agents" which covers planning workflows and multi-agent systems.

## Running the Labs

The lab files are converted Jupyter notebooks (`.py` format with cell markers). They require:
- OpenAI API key in `.env` file (`OPENAI_API_KEY`)
- For Lab 02: Tavily API key (`TAVILY_API_KEY`)

External utility modules referenced but not included locally:
- `utils` - Helper functions for prompting/printing
- `inv_utils` - Inventory/transaction database utilities (TinyDB-based)
- `tools` - Tool definitions for multi-agent workflows

## Module 5 Architecture

### Lab 01: Customer Service Agent (Planning with Code Execution)
Demonstrates the "code-as-plan" pattern where LLM generates executable Python instead of JSON plans:
1. LLM receives schema block describing TinyDB tables (inventory, transactions)
2. Generates Python code wrapped in `<execute_python>` tags
3. Code executes in sandboxed namespace with limited globals
4. Must set `answer_text` (customer-facing) and `STATUS` variables

Key pattern: Plans expressed as code are more flexible than JSON-based tool chains. Code becomes both documentation and execution.

### Lab 02: Market Research Team (Multi-Agent Pipeline)
Four specialized agents orchestrated sequentially:
1. **Market Research Agent** - Uses `tavily_search_tool` and `product_catalog_tool` to identify trends
2. **Graphic Designer Agent** - Generates image prompts via LLM, then calls DALL-E 3 directly
3. **Copywriter Agent** - Multimodal agent that takes image + trend summary to create campaign quotes
4. **Packaging Agent** - Compiles all artifacts into executive-ready markdown report

Uses `aisuite` library for unified model access. Each agent follows pattern: loop with tool calls until content response.

## Key Dependencies

- `openai` - Direct API access and via aisuite
- `aisuite` - Multi-provider LLM abstraction
- `tinydb` - Lightweight document database for Lab 01
- `PIL/Pillow` - Image handling in Lab 02
- `tavily` - Web search API for Lab 02
