---
name: todo-a-plan
description: "Use when converting scattered TODO comments into a structured, prioritised backlog. Reads all TODOs in the project, estimates effort, identifies dependencies, and outputs a planning document. Invoke with: /todo-a-plan, convert todos, make plan from todos, backlog, prioritise tasks."
argument-hint: "Optional: path to scope the search (e.g. src/). Defaults to the whole project."
user-invocable: true
---

# Skill: todo-a-plan

Convert all TODO comments in the codebase into a prioritised, actionable backlog.

## Steps

### 1. Collect TODOs
- Search for `TODO`, `FIXME`, `HACK`, and `NOTE` tags in all files under the given scope (or entire project).
- Record: file path, line number, tag type, comment text.

### 2. Classify Each Item
For each TODO, assign:
- **Priority**: High (blocks other work or is core functionality) / Medium / Low (nice-to-have).
- **Effort**: Small (<1 h) / Medium (1–4 h) / Large (>4 h).
- **Type**: Feature / Bug / Refactor / Documentation / Test.

### 3. Identify Dependencies
- If one TODO references another, or logically must come after it, record the dependency.

### 4. Generate the Backlog
- Use the template at [`assets/backlog-template.md`](./assets/backlog-template.md).
- Write the result to `doc/backlog.md`.

### 5. Recommend Next Action
- After the table, add a "Recommended Next" section: the single highest-value task to start now and why.

## Output

A `doc/backlog.md` file plus a chat summary of the total TODO count and top priorities.
