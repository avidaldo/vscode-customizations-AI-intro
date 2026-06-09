# Global Rules for GitHub Copilot

These rules apply across the entire project and are complemented by file-type-specific instructions listed in the **File-Specific Instructions** section below.

## Project Context

- This repository is a reference solution for a UD01 activity on GitHub Copilot customizations.
- Prioritize pedagogical clarity, justified decisions, and paradigmatic examples.
- Do not invent undocumented technical requirements.
- Keep the repository in English, except for `actividade.md`, which remains in Galician as the official brief.
- Prefer reproducible examples: expose a `seed` parameter or keep a fixed seed whenever randomness is involved.

## Instruction Modularity Rule

- Keep file-specific rules in `applyTo` instruction files to minimize unnecessary context loading.
- Use this file only for cross-cutting policies that apply to every interaction.
- Link to existing documents instead of duplicating content.

## File-Specific Instructions

- `.github/instructions/python.instructions.md` — PEP 8, NumPy docstrings, type hints, PyTorch conventions
- `.github/instructions/markdown.instructions.md` — pedagogical documentation style, cross-referencing
- `.github/instructions/notebooks.instructions.md` — narrative structure, clean outputs
- `.github/instructions/customizations.instructions.md` — authoring rules for `.prompt.md`, `.agent.md`, and `SKILL.md` files

## Development Commands

```bash
# Run the training script (all flags are optional)
python src/train_model.py --seed 42 --epochs 30 --device cpu

# Clear notebook outputs before committing
jupyter nbconvert --clear-output --inplace notebooks/*.ipynb
```

## Dataset

`data/sample.csv` — Iris sample dataset, 40 rows, columns: `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `species` (values: `setosa`, `versicolor`, `virginica`). Label map: setosa → 0, versicolor → 1, virginica → 2.

## Internal References

- [doc/capas.md](../doc/capas.md) — architecture overview of each customization layer
- [doc/justificacion.md](../doc/justificacion.md) — rationale for each primitive choice
- [README.md](../README.md) — project overview and file structure map