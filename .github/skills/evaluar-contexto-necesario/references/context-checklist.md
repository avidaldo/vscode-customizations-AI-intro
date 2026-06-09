# Context Evaluation Checklist

Use before running a complex task to ensure the agent has the right information.

## Task Clarity
- [ ] The task has a single, specific output (a file, a function, a report).
- [ ] The expected format of the output is defined.
- [ ] The scope is bounded (not "improve the whole codebase").

## Specification Context
- [ ] Is there a spec or requirements document? → Attach it.
- [ ] Is there an acceptance criterion or test? → Attach it.
- [ ] Is there a design decision that the agent must respect? → Attach the relevant doc section.

## Code Context
- [ ] Which existing files will the agent read or modify? → Attach them.
- [ ] Are there interfaces or function signatures the agent must match? → Attach the relevant module.
- [ ] Is there an existing similar implementation to use as a pattern? → Attach it.

## Data Context
- [ ] Does the task involve data? → Attach a sample (first 10–20 rows of a CSV, not the full file).
- [ ] Are column names or schema important? → Attach the schema or a `describe()` output.

## Style and Conventions
- [ ] Are coding conventions relevant? → The `python.instructions.md` file is auto-loaded for `.py` files.
- [ ] Is a specific output template required? → Attach it explicitly (e.g., the backlog template).

## Context Size Guard
- [ ] Total attached context is <8 000 tokens (~6 000 words / ~30 KB of code).
- [ ] You are not attaching the entire codebase for a task that touches 2 files.
- [ ] Binary files (images, `.pkl` models) are not attached — describe them instead.

## Common Mistakes
| Mistake | Better approach |
|---------|-----------------|
| Attaching the whole notebook when only one function matters | Attach only the relevant cell or function |
| Not attaching the spec and hoping the agent guesses requirements | Always attach the spec |
| Attaching a 500-row CSV as context | Attach only `df.head(10)` and `df.describe()` output |
| Attaching outdated docs | Verify the file is current before attaching |
