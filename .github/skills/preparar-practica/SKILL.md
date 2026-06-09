---
name: preparar-practica
description: "Use when designing or preparing a practical exercise with clear steps, checkpoints, and deliverables. Structures a practice session for students or for personal learning. Invoke with: /preparar-practica, prepare exercise, design practice, create lab, practice structure."
argument-hint: "Brief description of the practice topic (e.g. 'training a classifier on Iris data')"
user-invocable: true
---

# Skill: preparar-practica

Design a structured practical exercise from a topic description.

## Steps

### 1. Define Objectives
- Based on the topic argument, write 2–4 specific learning objectives.
- Each objective should be observable and verifiable: "Student can train a PyTorch model without looking at documentation."

### 2. Outline the Steps
- Break the practice into 5–8 sequential steps.
- Each step should take 10–20 minutes at beginner pace.
- Alternate between reading/understanding steps and hands-on coding steps.

### 3. Add Checkpoints
- After every 2–3 steps, define a checkpoint question or mini-task that lets the student (and instructor) verify progress.
- Refer to the checklist in [`references/practice-checklist.md`](./references/practice-checklist.md).

### 4. Define Deliverables
- List the files or outputs the student must produce by the end.
- Specify format: script, notebook, screenshot, written explanation.

### 5. Suggest Extensions
- Add 2–3 optional extension tasks for faster students.

## Output

A Markdown practice guide with objectives, steps, checkpoints, and deliverables. Written directly in chat unless a file path is specified.
