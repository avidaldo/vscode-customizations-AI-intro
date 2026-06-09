# Copilot Customization Reference Solution

This folder is a **reference implementation** for a UD01 activity on GitHub Copilot customizations (module: Programación de Inteligencia Artificial, 5073).

Students should use this project as a model answer — every customization primitive is represented with a realistic, justified example from an AI programming context.

## Purpose

Demonstrate, in a working project, how each of the five Copilot customization layers works, when to use it, and how it differs from the alternatives.

## Project Structure

```
solucion/
├── .github/
│   ├── copilot-instructions.md          # Layer 1: Global always-on instructions
│   ├── instructions/
│   │   ├── python.instructions.md       # Layer 1: Rules for .py files (applyTo)
│   │   ├── markdown.instructions.md     # Layer 1: Rules for .md files (applyTo)
│   │   └── notebooks.instructions.md   # Layer 1: Rules for .ipynb files (applyTo)
│   ├── prompts/
│   │   ├── tutor-review.prompt.md       # Layer 2: Code review via tutor agent
│   │   ├── sdd-check.prompt.md          # Layer 2: Spec-driven implementation check
│   │   ├── todo-to-plan.prompt.md       # Layer 2: Scan TODOs → prioritised plan
│   │   └── arch-review.prompt.md        # Layer 2: Architecture review
│   ├── skills/
│   │   ├── csv-eda-basica/              # Layer 3: EDA on a CSV + notebook template
│   │   ├── revision-notebook/           # Layer 3: Notebook quality audit
│   │   ├── dataset-card/                # Layer 3: Dataset documentation card
│   │   ├── debug-python-basico/         # Layer 3: Structured Python debugging
│   │   ├── todo-a-plan/                 # Layer 3: TODOs → backlog
│   │   ├── spec-a-tareas/               # Layer 3: Spec → task list (SDD)
│   │   ├── preparar-practica/           # Layer 3: Design a practice exercise
│   │   ├── conventional-commit/         # Layer 3: Git commit messages
│   │   ├── comparar-primitivas/         # Layer 3: Meta — choose the right primitive
│   │   ├── evaluar-contexto-necesario/  # Layer 3: Meta — what context to attach
│   │   └── frontmatter-designer/        # Layer 3: Meta — design frontmatter
│   ├── agents/
│   │   └── tutor.agent.md               # Layer 4: Socratic teaching agent
│   └── hooks/
│       ├── notebook-guardian.json       # Layer 5: PreToolUse hook config
│       └── scripts/
│           └── notebook-guardian.py     # Layer 5: Hook implementation script
├── data/
│   └── sample.csv                       # Iris sample (40 rows) — targets the skills
├── src/
│   └── train_model.py                   # PyTorch classifier — targets python.instructions.md
├── notebooks/
│   └── 01_eda_example.ipynb             # EDA notebook — targets notebooks.instructions.md
└── doc/
    ├── capas.md                         # Architecture overview with file map
    └── justificacion.md                 # Why each primitive was chosen
```

## How to Use This as a Student

1. **Read `doc/capas.md`** — understand the five layers before looking at the files.
2. **Open each `.github/` subfolder** — read the files in layer order (instructions → prompts → skills → agents → hooks).
3. **Try the slash commands** in VS Code Copilot chat: `/csv-eda-basica`, `/comparar-primitivas`, `/conventional-commit`, etc.
4. **Switch to the `tutor` agent** in the agent picker and ask it to review a function from `src/train_model.py`.
5. **Read `doc/justificacion.md`** to understand why each primitive was chosen over alternatives.

## Prerequisites

- VS Code with the GitHub Copilot extension (agent mode enabled).
- Python 3.10+, `torch`, `pandas`, `matplotlib`, `seaborn` (for running the ML source files).
- `jupyter` (for the hook script to strip notebook outputs): `pip install jupyter`.

## Language

All content in this folder is in English, as required by the activity specification.
