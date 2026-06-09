---
name: evaluar-contexto-necesario
description: "Use when preparing a complex task for an AI agent. Evaluates what files, examples, or templates should be attached as context to get the best result. Invoke with: /evaluar-contexto-necesario, what context do I need, prepare context, context for agent, attach files."
argument-hint: "Describe the task you are about to run (e.g. 'train a classifier on the Iris dataset')"
user-invocable: true
---

# Skill: evaluar-contexto-necesario

Evaluate and recommend the context that should be attached to a complex AI agent task.

## Steps

### 1. Parse the Task
- Restate the task in one sentence.
- Identify: what code will be created or modified, what data will be used, what output is expected.

### 2. Apply the Context Checklist
Work through [`references/context-checklist.md`](./references/context-checklist.md) for the task.

### 3. Recommend Files to Attach
- List specific files from the project that the agent will need.
- Prioritise: spec > existing implementation > tests > examples.
- Explain *why* each file is needed (not just list them).

### 4. Warn About Context Size
- If the total estimated tokens of recommended files exceeds ~8 000, flag it.
- Suggest pruning: "You need only the `train()` function from `train_model.py`, not the whole file."

### 5. Flag Missing Context
- If the task requires information that does not exist yet (a spec, a schema, an example), say so explicitly: "You should first create `doc/spec.md` using the `spec-a-tareas` skill."

## Output

A prioritised list of files to attach with justifications, plus a warning if context would be too large.
