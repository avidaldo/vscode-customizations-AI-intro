---
name: frontmatter-designer
description: "Use when creating a new Copilot customization file (skill, prompt, agent, or instruction). Proposes the correct frontmatter fields and values. Invoke with: /frontmatter-designer, design frontmatter, write frontmatter, new skill frontmatter, new agent frontmatter."
argument-hint: "Describe the primitive type and its purpose (e.g. 'a skill that reviews Python code for PEP 8')"
user-invocable: true
---

# Skill: frontmatter-designer

Propose correct and complete frontmatter for a new Copilot customization file.

## Steps

### 1. Identify the Primitive Type
From the argument, determine whether the user needs:
- `*.instructions.md` (behaviour rule)
- `*.prompt.md` (task macro)
- `SKILL.md` (workflow package)
- `*.agent.md` (custom agent)
- `*.json` (hook)

### 2. Apply the Frontmatter Template
Refer to [`references/frontmatter-examples.md`](./references/frontmatter-examples.md) for the template for each primitive type.

### 3. Propose the `description` Field
This is the most important field — it is the discovery surface.

Rules:
- Start with "Use when..." to set context.
- Include 3–5 specific trigger keywords that users or the agent would naturally write.
- Mention what the primitive does, not just what it is called.
- Do NOT include colons (`:`) unquoted in YAML values — wrap the whole value in quotes.

### 4. Propose the `name` Field (for Skills)
- Must match the folder name exactly (lowercase, hyphens only).
- 1–64 characters.

### 5. Propose `tools` (for Agents and Instructions)
- List only tools actually needed.
- For read-only workflows: `[codebase, search, usages]`.
- For editing workflows: add `editFiles`.
- For command execution: add `runCommand` (use sparingly).

### 6. Validate
Check every field against the common pitfalls in [`references/frontmatter-examples.md`](./references/frontmatter-examples.md).

## Output

A ready-to-paste YAML frontmatter block with a brief explanation of each field choice.
