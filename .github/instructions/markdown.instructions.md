---
description: "Use when creating or editing Markdown files. Enforces clear structure, pedagogical documentation style, and consistent cross-referencing patterns."
tools: ['codebase', 'editFiles', 'search', 'usages']
applyTo: "**/*.md"
---

# Instructions for Markdown Files

## Content Approach

- Write in formal, technical English with pedagogical clarity.
- Explain decisions and trade-offs, not just mechanical steps.
- When citing sources, prioritize official documentation and link to existing repo resources.

## Recommended Style

- Use short, logically progressive headings and sections.
- Use lists for criteria, requirements, and checklists.
- Avoid redundancy — do not duplicate content already present in other guides.

## Rules for Customization Documentation

- When documenting instructions, prompts, skills, agents, or hooks, always include:
  - What the primitive does.
  - When to use it and when NOT to use it.
  - Reasonable alternatives in the context of this project.

## Internal References

- `doc/capas.md` — architecture overview
- `doc/justificacion.md` — primitive decision rationale
