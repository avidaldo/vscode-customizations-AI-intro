# Conventional Commit Examples

Reference examples for each commit type. Based on the [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) specification.

## feat — New Feature

```
feat(data): add load_data() with normalisation

Centralises CSV loading and applies zero-mean, unit-variance normalisation
so callers do not need to pre-process separately.
```

```
feat: add --device argument to train_model.py
```

## fix — Bug Fix

```
fix(train): correct label tensor dtype from float32 to long

CrossEntropyLoss requires LongTensor targets. Using float32 caused a
RuntimeError on CUDA devices.
```

```
fix: remove hardcoded path in DATA_PATH constant
```

## docs — Documentation Only

```
docs: translate copilot-instructions.md to English
```

```
docs(notebooks): add interpretation cell after pairplot
```

## style — Formatting

```
style: apply Black formatting to src/train_model.py
```

## refactor — No Behaviour Change

```
refactor(model): extract IrisClassifier into separate module

No change to model architecture or training logic.
```

## test — Tests

```
test: add determinism test for set_seed()
```

## chore — Tooling / Config

```
chore: add .gitignore entry for __pycache__ and .ipynb_checkpoints
```

```
chore(hooks): add notebook-guardian PreToolUse hook
```

## Breaking Change

```
feat(api)!: rename load_data() to load_iris_csv()

BREAKING CHANGE: Any caller of load_data() must update to load_iris_csv().
```

## Anti-patterns to Avoid

| Bad | Good |
|-----|------|
| `update files` | `docs: update README with install instructions` |
| `fix bug` | `fix(train): handle missing device argument` |
| `wip` | `feat: add partial implementation of validation loop` |
| `changes` | `refactor: simplify train() by extracting evaluate()` |
