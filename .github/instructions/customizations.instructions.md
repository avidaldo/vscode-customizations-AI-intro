---
description: "Use when creating or editing Copilot customization files. Enforces consistent frontmatter, description patterns, and asset layout for .prompt.md, .agent.md, and SKILL.md files."
applyTo: "**/*.prompt.md,**/*.agent.md,.github/skills/**/SKILL.md"
---

# Instructions for Copilot Customization Files

Consult [doc/capas.md](../../doc/capas.md) for the canonical purpose and example of each primitive (L1–L5). Consult [doc/justificacion.md](../../doc/justificacion.md) for the rationale behind each choice.

## Frontmatter Rules

- All YAML values that contain a colon must be quoted: `description: "Use when: doing X"`.
- `name` must match the parent folder name (skills) or the file stem without extension (prompts, agents).
- Every file must have a `description` field. It is the primary discovery surface — the agent uses it to decide whether to load the file.

## Description Pattern

All `description` values must follow this structure:

```
Use when [trigger condition]. [One sentence of scope]. Invoke with: /name, keyword1, keyword2.
```

This pattern matches the descriptions used in all 11 existing skills in `.github/skills/`. Deviating from it reduces discoverability.

## Skill Asset Layout

```
.github/skills/<name>/
  SKILL.md          # required — workflow instructions
  assets/           # optional — templates, starter files
  references/       # optional — reference material linked from SKILL.md
```

Do not put reference material in `assets/` or vice versa.

## Scope Guidance

- **Prompts** (`.github/prompts/`) — single focused task with parameterized inputs; no bundled files needed.
- **Skills** (`.github/skills/<name>/SKILL.md`) — multi-step workflow; use when bundled assets add value.
- **Agents** (`.github/agents/`) — use when tool restrictions or context isolation are required; document which tools are disabled and why.

## What to Document

Every customization file body must make clear:

1. What the primitive does.
2. When to use it and when **not** to use it.
3. The alternative primitive and why it was not chosen (link to [doc/justificacion.md](../../doc/justificacion.md)).
