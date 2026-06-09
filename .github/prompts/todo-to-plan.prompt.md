---
description: "Use when turning scattered TODO comments into a prioritised implementation plan. Scans the project, estimates effort, and produces an actionable backlog document. Invoke with: /todo-to-plan, todo plan, backlog, prioritise todos, task plan."
name: "todo-to-plan"
tools:
  - codebase
  - search
  - editFiles
agent: Plan
---

## Task

Generate a prioritised backlog from all TODO comments in this project.

### Step 1 — Collect TODOs

Search every file in the project for `TODO`, `FIXME`, `HACK`, and `NOTE` comments. For each one, record:
- File path and line number.
- The comment text.
- The type (`TODO` / `FIXME` / `HACK` / `NOTE`).

### Step 2 — Classify and Estimate

For each item, assign:
- **Priority**: High / Medium / Low (based on proximity to core functionality).
- **Effort**: Small (< 1 h) / Medium (1–4 h) / Large (> 4 h).
- **Dependencies**: List other TODOs that must be done first, if any.

### Step 3 — Output the Plan

Write the resulting backlog to `doc/todo-plan.md` using this format:

```markdown
# TODO Backlog — <date>

| # | Priority | Effort | File | Line | Description | Depends on |
|---|----------|--------|------|------|-------------|------------|
| 1 | High     | Small  | src/train_model.py | 42 | Add validation split | — |
...
```

### Step 4 — Suggest Next Action

After the table, add a short paragraph identifying the single highest-value next action and why.

> **Note:** This prompt demonstrates the value of keeping TODOs in code as a lightweight planning tool.
> The agent is the bridge between scattered annotations and a structured, actionable backlog.
