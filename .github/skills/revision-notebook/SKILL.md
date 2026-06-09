---
name: revision-notebook
description: "Use when reviewing the quality of a Jupyter Notebook. Checks whether explanation and code are properly mixed, variable names are clear, and visualisations are justified. Invoke with: /revision-notebook, review notebook, check notebook quality, notebook audit."
argument-hint: "Path to the notebook to review (e.g. notebooks/01_eda_example.ipynb)"
user-invocable: true
---

# Skill: revision-notebook

Audit a Jupyter Notebook for structural quality and pedagogical clarity.

## Steps

### 1. Read the Notebook
- Open the notebook at the path provided.
- Extract all cell types (Markdown vs Code) and their order.

### 2. Structure Check
Work through the checklist in [`references/quality-checklist.md`](./references/quality-checklist.md).

Key rules:
- Each code cell group must be preceded by a Markdown narrative cell.
- No code cell appears before the first Markdown title.
- The notebook ends with a Markdown summary cell.

### 3. Variable Name Audit
- Flag single-letter names not justified by math convention (e.g., `a`, `b`, `tmp`).
- Flag generic names (`data`, `result`, `output`) that could be more descriptive.

### 4. Visualisation Review
- For every plot cell, check whether the following Markdown cell interprets the plot.
- Flag any plot without axes labels or a title.

### 5. Output Hygiene
- Check whether any cell has embedded outputs (JSON `outputs` array is non-empty).
- If outputs are present, warn: "Outputs detected — run `jupyter nbconvert --clear-output --inplace <file>` before committing."

## Output

A numbered list of findings with severity (Warning / Error) and the cell index, plus a summary score (0–10).
