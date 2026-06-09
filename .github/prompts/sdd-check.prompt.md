---
description: "Use when comparing a specification against the codebase and closing the implementation gap. Performs a spec-driven check, identifies missing work, and updates matching files. Invoke with: /sdd-check, spec check, sdd, implement spec, gap analysis."
name: "sdd-check"
argument-hint: "Path to the specification file (e.g. doc/spec.md)"
tools:
  - codebase
  - editFiles
  - search
---

## Task

Perform a spec-driven development (SDD) cycle on the specification file at: **$input**

### Step 1 — Read the Spec

Open and read the specification file. Identify:
- Features or requirements marked as TODO, pending, or not yet implemented.
- Any section with no corresponding code file or function.

### Step 2 — Cross-Reference with Codebase

Search the codebase for implementations of each requirement. Mark each as:
- **Implemented** — code exists and matches the spec.
- **Partial** — code exists but does not fully cover the requirement.
- **Missing** — no implementation found.

### Step 3 — Implement Missing Items

For each **Missing** or **Partial** item:
1. Create or update the relevant source file(s).
2. Follow the conventions in `.github/instructions/python.instructions.md` (type hints, NumPy docstrings, seeds).
3. After implementing, add a brief inline comment referencing the spec section.

### Step 4 — Update the Spec

Mark implemented items in the spec file with a ✅ prefix.

> **Note:** This prompt illustrates Specification-Driven Development: the spec is the single source of truth, and the agent's job is to close the gap between the spec and the codebase.
