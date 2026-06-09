---
name: spec-a-tareas
description: "Use when converting a specification document into an ordered implementation and validation task list. Applies a simplified Spec-Driven Development methodology. Invoke with: /spec-a-tareas, spec to tasks, implement spec, sdd, specification driven, break down spec."
argument-hint: "Path to the specification file (e.g. doc/spec.md)"
user-invocable: true
---

# Skill: spec-a-tareas

Convert a specification document into a structured, ordered implementation and validation plan.

## Steps

### 1. Read the Specification
- Open the file at the provided path.
- Identify sections that describe: features, behaviours, inputs/outputs, constraints.
- Note any explicit acceptance criteria or "must" / "should" / "may" language.

### 2. Check Completeness
Work through the completeness checklist in [`assets/spec-template.md`](./assets/spec-template.md). Flag any missing sections as blockers before generating a plan.

### 3. Generate the Task List
- For each requirement in the spec, generate:
  - One **implementation task** (what code to write).
  - One **validation task** (how to verify it works).
- Order tasks by dependency (a task cannot be validated before it is implemented).
- Assign effort: Small / Medium / Large.

### 4. Write the Plan
- Use the template at [`assets/plan-template.md`](./assets/plan-template.md).
- Save the plan to `doc/plan_<spec-name>.md`.

### 5. Cross-Reference
- Search the codebase for any existing implementations that already satisfy spec requirements.
- Mark those tasks as **Already Done** in the plan.

## Output

A `doc/plan_*.md` file with an ordered task list plus a chat summary of total tasks and estimated effort.
