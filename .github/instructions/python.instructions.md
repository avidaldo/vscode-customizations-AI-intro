---
description: "Use when creating or editing Python files. Enforces PEP 8, NumPy docstrings, type hints, and AI/ML conventions for reproducibility and portability."
tools: ['codebase', 'editFiles', 'search', 'usages']
applyTo: "**/*.py"
---

# Instructions for Python Files

## Style and Quality

- Use static typing (type hints) in all function and method signatures.
- Use `snake_case` for functions and variables, `PascalCase` for classes.
- Include NumPy-style docstrings in all modules, classes, and public functions.
- Follow PEP 8: 4-space indentation, max 88 chars per line (Black-compatible).

## AI/ML Conventions

- Use PyTorch (`torch`) as the primary framework for neural networks.
- Prefer vectorized operations over Python loops where reasonable.
- Ensure reproducibility: accept a `seed` parameter or fix seeds at training/model initialization.
- Manage device explicitly (`cpu`/`cuda`) for portable execution across machines.

## Pedagogical Focus

- Prefer small but paradigmatic examples that can be explained in class.
- When introducing a technical decision, leave a brief inline justification comment and mention the alternative.
