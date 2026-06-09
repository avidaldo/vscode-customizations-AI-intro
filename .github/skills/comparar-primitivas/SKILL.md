---
name: comparar-primitivas
description: "Use when deciding which Copilot customization primitive to use for a new requirement. Compares instructions, prompts, skills, agents, and hooks and recommends the best fit. Invoke with: /comparar-primitivas, choose primitive, which primitive, instruction vs prompt, skill vs prompt, agent vs skill."
argument-hint: "Describe the requirement or use case you want to implement"
user-invocable: true
---

# Skill: comparar-primitivas

Recommend the right Copilot customization primitive for a given requirement.

## Steps

### 1. Understand the Requirement
- Restate the requirement in one sentence: "I need Copilot to always X when editing Y files."
- Identify the key properties: always-on vs on-demand, needs assets vs text-only, must enforce vs guide.

### 2. Apply the Decision Table
Use [`references/decision-table.md`](./references/decision-table.md) to systematically evaluate each primitive.

### 3. Recommend with Justification
- State which primitive fits best and why.
- Explicitly say which primitives would NOT work and why.
- If two primitives could both work, explain the trade-off and ask a clarifying question.

### 4. Show the Minimal Example
- Write a minimal frontmatter block for the recommended primitive.
- Point to the relevant file in this project as a concrete example.

## Output

A structured recommendation: chosen primitive → justification → rejected alternatives → minimal example.
