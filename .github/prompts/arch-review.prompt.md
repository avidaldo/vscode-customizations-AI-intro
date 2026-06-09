---
description: "Critical architecture and best-practices review: assess project structure, design decisions, code quality, and flag anti-patterns with actionable recommendations."
name: "Architecture Review"
tools:
  - codebase 
  - search
  - usages
---

## Task

Perform a critical review of this project's architecture, code quality, and adherence to best practices.

### Step 1 — Map the Structure

Read the project file tree and identify:
- Entry points and main modules.
- Data flow: how data moves from input to output.
- Configuration management: how settings (device, seed, hyperparameters) are handled.

### Step 2 — Evaluate Against Principles

For each of the following dimensions, assign a rating (✅ Good / ⚠️ Needs Improvement / ❌ Problematic) and a one-line justification:

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Reproducibility (seeds, deterministic ops) | | |
| Separation of concerns (data / model / training) | | |
| Type safety (type hints, validated inputs) | | |
| Documentation (docstrings, README accuracy) | | |
| Portability (device-agnostic, no hardcoded paths) | | |
| Testability (pure functions, injectable dependencies) | | |

### Step 3 — Flag Anti-Patterns

List any specific anti-patterns found, with file + line reference and a recommended fix.

### Step 4 — Top 3 Recommendations

Summarise the three highest-impact improvements the team should address first, ordered by impact.

> **Note:** This prompt does not edit code. It produces a structured review document useful for
> code-review sessions, design discussions, or self-assessment activities.
