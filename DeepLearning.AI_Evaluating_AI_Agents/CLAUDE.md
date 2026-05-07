# CLAUDE.md

This file provides guidance to Claude Code when working in this course directory.

## Overview

This directory contains learning materials from the DeepLearning.AI short course
"Evaluating AI Agents" (https://www.deeplearning.ai/short-courses/evaluating-ai-agents/).

This course teaches how to add observability to agent-based applications and use an evaluation-driven development process to efficiently iterate on and improve AI agents. You will learn how to evaluate each component of an agentic workflow -- including routers, tools, and trajectories -- using structured experiments and LLM-as-a-judge techniques. The course is taught by John Gilhuly (Head of Developer Relations) and Aman Khan (Director of Product) at Arize AI, built in partnership with DeepLearning.AI.

## Folder Structure

```
.
├── content.txt
├── 01_Introduction/
│   └── transcript.txt
├── 02_Evaluation_in_the_time_of_LLMs/
│   └── transcript.txt
├── 03_Decomposing_agents/
│   └── transcript.txt
├── 04_Lab_1_Building_your_agent/
│   ├── Lab_01.md
│   └── transcript.txt
├── 05_Tracing_agents/
│   └── transcript.txt
├── 06_Lab_2_Tracing_your_agent/
│   ├── Lab_02.md
│   └── transcript.txt
├── 07_Adding_router_and_skill_evaluations/
│   └── transcript.txt
├── 08_Lab_3_Adding_router_and_skill_evaluations/
│   ├── Lab_03.md
│   └── transcript.txt
├── 09_Adding_trajectory_evaluations/
│   └── transcript.txt
├── 10_Lab_4_Adding_trajectory_evaluations/
│   ├── Lab_04.md
│   └── transcript.txt
├── 11_Adding_structure_to_your_evaluations/
│   └── transcript.txt
├── 12_Lab_5_Adding_structure_to_your_evaluations/
│   ├── Lab_05.md
│   └── transcript.txt
├── 13_Improving_your_LLM-as-a-judge/
│   └── transcript.txt
├── 14_Monitoring_agents/
│   └── transcript.txt
├── 15_Conclusion/
│   └── transcript.txt
├── 16_Quiz/
│   └── content.txt
└── 17_Appendix_-_Resources_Tips_and_Help/
    └── Appendix.md
```

## Course Sections

| # | Section | Type | Has Lab |
|---|---------|------|---------|
| 01 | Introduction | Video | No |
| 02 | Evaluation in the time of LLMs | Video | No |
| 03 | Decomposing agents | Video | No |
| 04 | Lab 1: Building your agent | Video with Code Example | Yes |
| 05 | Tracing agents | Video | No |
| 06 | Lab 2: Tracing your agent | Video with Code Example | Yes |
| 07 | Adding router and skill evaluations | Video | No |
| 08 | Lab 3: Adding router and skill evaluations | Video with Code Example | Yes |
| 09 | Adding trajectory evaluations | Video | No |
| 10 | Lab 4: Adding trajectory evaluations | Video with Code Example | Yes |
| 11 | Adding structure to your evaluations | Video | No |
| 12 | Lab 5: Adding structure to your evaluations | Video with Code Example | Yes |
| 13 | Improving your LLM-as-a-judge | Video | No |
| 14 | Monitoring agents | Video | No |
| 15 | Conclusion | Video | No |
| 16 | Quiz | Graded Quiz | No |
| 17 | Appendix - Resources, Tips and Help | Code Example | Yes |

## Learning Companion

Claude Code should act as a learning companion for this course. When working in this
directory, prioritize these learning activities:

### Deep Understanding
- When asked about a concept, read the relevant section's transcript first, then explain
  with additional context, analogies, and connections to other sections
- Draw connections between sections -- how earlier concepts build toward later ones
- Answer clarifying questions grounded in the actual course content, supplemented by
  broader knowledge when helpful

### Practice & Exercises
- Generate exercises graded from basic (recall/comprehension) to advanced (synthesis/application)
- For sections with labs: suggest modifications and extensions to the lab code
- For lecture-only sections: create coding challenges that implement the discussed concepts
- Provide worked solutions with explanations when asked

### Extend & Build
- Help modify lab examples for new use cases or datasets
- When the user wants to build something, scaffold it in a `projects/` subfolder
- Suggest project ideas that combine concepts from multiple sections
- Help integrate course concepts with the user's existing work and other courses

### Blog Writing
- When the user wants to write about what they learned, use the `/blog-post` skill
- Draw from transcripts and lab code for technical accuracy
- Help synthesize insights across sections into cohesive narratives
- Suggest blog post angles: tutorials, concept explanations, lessons learned, comparisons

### How to Ground Responses
- Always read the relevant transcript.txt and lab files before responding about course content
- Prefer course-specific terminology and examples over generic explanations
- When the course content conflicts with general knowledge (e.g., simplified explanations
  for teaching), note both perspectives
- Reference specific sections by number and title when making connections

## Environment

<!-- Fill in as you set up your coding environment -->
- **Package manager**: [uv / pip / conda]
- **Python version**: [3.x]
- **API keys needed**: [list from lab files]
- **Key dependencies**: [from lab imports]

To set up:
```bash
# TODO: Add setup commands as you configure the environment
```
