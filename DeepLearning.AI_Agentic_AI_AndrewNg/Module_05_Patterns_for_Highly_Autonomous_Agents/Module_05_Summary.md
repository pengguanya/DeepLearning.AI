# Module 5: Patterns for Highly Autonomous Agents

## The Core Problem This Module Solves

Traditional agents require you to **hard-code the sequence of steps**. Module 5 teaches you to build agents that **decide their own steps at runtime** — making them far more flexible and powerful.

---

## Key Concept 1: Planning Pattern

### What It Is
Instead of you (the developer) defining "do A, then B, then C", you give the LLM tools and ask it to **generate its own plan** to accomplish a task.

### The Basic Flow
```
User Query → LLM generates multi-step plan → Execute step 1 → Execute step 2 → ... → Final answer
```

### Why It Matters (Interview Angle)
> **Interview Q:** "Why would you use a planning agent instead of hard-coding a workflow?"
>
> **Answer:** Hard-coded workflows break when users ask unexpected questions. A planning agent can handle a much wider range of queries because it dynamically composes tools. Trade-off: less predictable behavior, harder to debug.

---

## Key Concept 2: Plan Output Formats (JSON vs XML vs Code)

Andrew presents a hierarchy of plan formats by reliability:

| Format | Reliability | Parseability | Flexibility |
|--------|-------------|--------------|-------------|
| **Code** | Highest | Execute directly | Thousands of functions available |
| **JSON** | High | Easy to parse | Limited to predefined tools |
| **XML** | High | Easy to parse | Limited to predefined tools |
| **Plain Text** | Low | Ambiguous | Unreliable |

### Real-World Insight
JSON planning requires you to define every tool the agent might need. When users ask edge-case questions, you keep adding tools — this becomes **brittle and unmaintainable**.

---

## Key Concept 3: Code-as-Plan (The Big Idea)

### The Problem with Tool Proliferation
Example from lecture: A spreadsheet Q&A agent needs:
- `get_column_max`, `get_column_min`, `filter_rows`, `sum_rows`...

User asks: "How many unique transactions last week?"
→ You don't have a tool for that → You create `get_unique_entries`
→ Next query needs another tool → Endless cycle

### The Solution
Let the LLM **write Python code** that IS the plan:

```python
# LLM generates this:
df = pd.read_csv('sales.csv')
df['date'] = pd.to_datetime(df['date'])  # Step 1: parse dates
last_week = df[df['date'] > cutoff]       # Step 2: filter
unique_count = last_week.drop_duplicates() # Step 3: dedupe
print(len(unique_count))                   # Step 4: count
```

### Why Code > JSON (Research-Backed)
From the Xinyao Wang paper cited by Andrew:
- **Code-as-action outperforms JSON-as-action** across multiple models
- LLMs have seen millions of examples of Python/pandas usage
- Libraries provide thousands of "pre-built tools" the LLM already knows

### Interview-Ready Answer
> **Q:** "When would you choose code generation over tool-based agents?"
>
> **A:** When the task domain maps well to existing libraries (data analysis, file manipulation, API calls). Code gives access to thousands of functions the LLM already knows. Tool-based is better when you need strict control over allowed actions or when operating in domains without good library coverage.

---

## Key Concept 4: Safe Code Execution

From Lab 01, the execution pattern:

```python
SAFE_GLOBALS = {
    "Query": Query,  # Only expose what's needed
    "get_current_balance": helper_func,
}
SAFE_LOCALS = {
    "db": db,
    "inventory_tbl": inventory_tbl,
}

exec(generated_code, SAFE_GLOBALS, SAFE_LOCALS)
```

### Critical Production Considerations
1. **Sandbox the execution** — Don't run LLM code with full system access
2. **Limit imports** — Only allow safe modules
3. **Capture stdout/stderr** — For debugging and user feedback
4. **Set timeouts** — Prevent infinite loops

> **Interview Q:** "How would you safely execute LLM-generated code in production?"
>
> **A:** Use sandboxed execution (Docker, gVisor, or restricted `exec()` with curated globals). Whitelist allowed imports. Set CPU/memory limits and timeouts. Log all generated code for audit. Consider using code interpreters like E2B or Modal for isolation.

---

## Key Concept 5: Multi-Agent Systems (Lab 02)

### The Pattern
Break complex tasks into **specialized agents**, each with focused expertise:

```
Market Research Agent (search + catalog)
        ↓
Graphic Designer Agent (generates image prompts → DALL-E)
        ↓
Copywriter Agent (multimodal: image + text → quote)
        ↓
Packaging Agent (assembles final report)
```

### Why Multi-Agent?
1. **Separation of concerns** — Each agent has clear responsibility
2. **Specialized prompts** — Each agent's system prompt is focused
3. **Debuggability** — Easier to trace which agent failed
4. **Modularity** — Swap out agents without rewriting everything

### The Agent Loop Pattern (from Lab 02)
```python
while True:
    response = client.chat.completions.create(
        model="openai:o4-mini",
        messages=messages,
        tools=tools_,
        tool_choice="auto"
    )

    if msg.content:  # Final answer
        return msg.content

    if msg.tool_calls:  # Keep working
        for tool_call in msg.tool_calls:
            result = handle_tool_call(tool_call)
            messages.append(tool_response)
```

This is the **ReAct loop** — Reason → Act → Observe → Repeat.

---

## Summary: The Two Main Patterns

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Code-as-Plan** | Data manipulation, computations, queries over structured data | Customer service agent querying inventory DB |
| **Multi-Agent Pipeline** | Complex workflows with distinct phases | Marketing campaign: research → design → copy → package |

---

## Interview Preparation Checklist

### Concepts You Should Be Able to Explain
- [ ] Why planning agents are more flexible than hard-coded workflows
- [ ] Trade-offs of JSON tools vs code generation
- [ ] How to sandbox LLM-generated code
- [ ] ReAct loop pattern (Reason-Act-Observe)
- [ ] When to use single agent vs multi-agent architecture

### System Design Questions to Practice
1. "Design an agent that can answer natural language questions about a SQL database"
2. "How would you build a customer support agent that can process returns and answer inventory questions?"
3. "Design a multi-agent system for automated code review"

---

## Lab Reference

- **Lab 01: Customer Service Agent** — Demonstrates code-as-plan pattern with TinyDB
- **Lab 02: Market Research Team** — Demonstrates multi-agent pipeline with 4 specialized agents
