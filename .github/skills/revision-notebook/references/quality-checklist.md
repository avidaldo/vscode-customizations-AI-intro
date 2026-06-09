# Notebook Quality Checklist

## Structure
- [ ] First cell is a Markdown title cell (starts with `# `).
- [ ] Every group of code cells is preceded by a Markdown explanation cell.
- [ ] Last cell is a Markdown summary or "Next Steps" cell.
- [ ] No cell is excessively long (>30 lines of code without explanation).

## Variable Names
- [ ] No single-letter variables outside standard math notation (`X`, `y`, `i`, `j`).
- [ ] No overly generic names (`data`, `result`, `temp`, `output`).
- [ ] Tensor/array shapes are documented in a comment when non-obvious.

## Visualisations
- [ ] Every `plt.show()` or `sns.*` call is in a cell preceded by a narrative Markdown cell.
- [ ] Every plot has a title (`plt.title(...)` or `ax.set_title(...)`).
- [ ] All axes are labelled (`xlabel`, `ylabel`).
- [ ] The cell immediately after each plot interprets the result in ≥1 sentence.

## Code Discipline
- [ ] Imports are consolidated in the first code cell.
- [ ] `random.seed`, `np.random.seed`, `torch.manual_seed` are set before any stochastic operation.
- [ ] No `print(df)` — use `display(df)` or `df.head()` to limit output size.

## Output Hygiene
- [ ] All cell outputs are cleared (`outputs: []` in JSON).
- [ ] No binary blobs, large tensors, or base64 images embedded in the file.
- [ ] File size is <100 KB (a sign outputs are clean).
