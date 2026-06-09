---
description: "Use when creating or editing Jupyter Notebook files. Enforces clear narrative structure, clean output discipline, and well-justified visualizations."
tools: ['codebase', 'editFiles', 'search', 'usages']
applyTo: "**/*.ipynb"
---

# Instructions for Jupyter Notebooks

## Narrative Structure

- Every code cell group must be preceded by a Markdown cell explaining:
  - What the code does.
  - Why this step is needed in the workflow.
- Do not start a notebook with a code cell. Begin with a Markdown title and context section.
- Conclude with a Markdown cell summarizing findings or next steps.

## Code Cell Discipline

- Keep each code cell focused on a single logical operation (load, transform, plot, evaluate).
- Use clear, descriptive variable names — avoid single-letter names except for canonical math notation (`X`, `y`, `i`).
- Avoid deeply nested logic in cells; extract helper functions to `.py` modules when reuse is expected.

## Output Hygiene

- **Clear all outputs before committing.** Never commit notebooks with embedded outputs, large tensors, or binary plot data.
- Use `jupyter nbconvert --clear-output --inplace <file>` before `git add`.
- The `notebook-guardian` hook (`.github/hooks/notebook-guardian.json`) enforces this automatically at `read_file` time.

## Visualizations

- Every plot must be accompanied by a Markdown cell interpreting the result in 1–3 sentences.
- Label axes and add titles to all plots.
- Prefer `matplotlib` for basic plots; `seaborn` for statistical distributions.
