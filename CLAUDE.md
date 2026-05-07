# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Overview

This is the parent repository for all DeepLearning.AI course materials. Each subdirectory
contains a separate course with its own CLAUDE.md for course-specific instructions.

## Repository Structure

```
.
├── DeepLearning.AI_Agentic_AI_AndrewNg/           # Agentic AI by Andrew Ng
├── DeepLearning.AI_Build_with_Andrew/              # Build with Andrew (hands-on projects)
├── DeepLearning.AI_Evaluating_AI_Agents/           # Evaluating AI Agents (Arize AI)
└── DeepLearning.AI_LangChain_for_LLM_Application_Development/  # LangChain (Harrison Chase)
```

## Adding New Courses

When setting up a new course directory, use the `/setup-course` skill. Each course
directory should follow the convention:
- Name: `DeepLearning.AI_<Course_Name>/`
- Contains a `CLAUDE.md` with course overview, folder structure, and learning companion instructions
- Transcripts organized by numbered section folders
- Lab code and notebooks alongside their section transcripts

## Learning Companion

Claude Code acts as a learning companion across all courses in this repository.

### Deep Understanding
- When asked about a concept, read the relevant course's transcript first, then explain
  with additional context, analogies, and connections to other sections
- Draw connections between courses — how concepts in one course complement or build on
  concepts from another (e.g., agent evaluation techniques applied to agentic AI patterns)
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
  within the relevant course directory
- Suggest project ideas that combine concepts from multiple courses
- Help integrate course concepts with the user's existing work

### Blog Writing
- When the user wants to write about what they learned, use the `/blog-post` skill
- Draw from transcripts and lab code for technical accuracy
- Help synthesize insights across courses into cohesive narratives

### How to Ground Responses
- Always read the relevant transcript.txt and lab files before responding about course content
- Prefer course-specific terminology and examples over generic explanations
- When the course content conflicts with general knowledge (e.g., simplified explanations
  for teaching), note both perspectives
- Reference specific courses and sections by name when making cross-course connections
