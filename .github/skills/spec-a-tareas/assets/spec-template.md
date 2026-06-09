# Specification Template

> Use this template to write a specification that the `spec-a-tareas` skill can process reliably.

---

## 1. Overview

<!-- One paragraph: what does this component or feature do, and why? -->

## 2. Goals

<!-- Bullet list of outcomes this implementation must achieve. Use "must", "should", "may". -->

- Must: ...
- Should: ...
- May: ...

## 3. Inputs and Outputs

| Item | Type | Description |
|------|------|-------------|
| Input: `<name>` | `<type>` | What the function/module receives |
| Output: `<name>` | `<type>` | What it returns |

## 4. Constraints

<!-- Non-functional requirements: performance, reproducibility, portability, etc. -->
- Reproducibility: seed must be fixed before any stochastic operation.
- Device portability: must run on both `cpu` and `cuda` without code changes.

## 5. Acceptance Criteria

<!-- List of specific, verifiable conditions that define "done". -->
- [ ] Unit test passes with seed=42 and expected output X.
- [ ] No `torch.cuda.*` calls that hard-code the device.
- [ ] Docstring present and follows NumPy style.

## 6. Open Questions

<!-- Decisions not yet made. Must be resolved before implementation starts. -->
- <!-- TODO: fill in -->

## Completeness Checklist

- [ ] Section 1 (Overview) is present and non-trivial.
- [ ] At least one "must" goal is defined.
- [ ] All inputs and outputs are typed.
- [ ] At least two acceptance criteria exist.
- [ ] No open questions remain unresolved.
