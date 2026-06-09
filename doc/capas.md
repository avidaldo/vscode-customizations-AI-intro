# Copilot Customization Architecture (2026)

This document maps each primitive layer to its files in this repository.

## Layer 1 — Behavior (Instructions)

Markdown instruction files loaded automatically or on-demand to shape how Copilot writes code and documentation.

- `.github/copilot-instructions.md` — always-on global rules.
- `.github/instructions/python.instructions.md` — auto-applied to `**/*.py`.
- `.github/instructions/markdown.instructions.md` — auto-applied to `**/*.md`.
- `.github/instructions/notebooks.instructions.md` — auto-applied to `**/*.ipynb`.

**Key principle**: Instructions say *how* to write things, not *what* to do. They are injected silently into context.

## Layer 2 — Task Invocation (Prompt Files)

Reusable chat macros that trigger a focused, parameterized action via `/` slash commands.

- `.github/prompts/tutor-review.prompt.md` — code review via the Socratic tutor agent.
- `.github/prompts/sdd-check.prompt.md` — spec-driven check that identifies pending items and implements them.
- `.github/prompts/todo-to-plan.prompt.md` — scan TODOs and generate a prioritized plan.
- `.github/prompts/arch-review.prompt.md` — architecture and best-practices critical review.

**Key principle**: A prompt is a text macro — no bundled assets. If it needs templates or multi-step procedures, it should be a skill.

## Layer 3 — Workflow (Skills)

Self-contained capability packages invoked via `/` slash commands. Each skill includes a `SKILL.md` plus optional scripts, templates, and checklists in the same folder.

- `.github/skills/csv-eda-basica/` — `csv-eda-basica` for data analysis.
- `.github/skills/revision-notebook/` — `revision-notebook` for notebook quality.
- `.github/skills/dataset-card/` — `dataset-card` for dataset documentation.
- `.github/skills/debug-python-basico/` — `debug-python-basico` for Python debugging.
- `.github/skills/todo-a-plan/` — `todo-a-plan` for project planning.
- `.github/skills/spec-a-tareas/` — `spec-a-tareas` for spec-driven development.
- `.github/skills/preparar-practica/` — `preparar-practica` for practice preparation.
- `.github/skills/conventional-commit/` — `conventional-commit` for Git commits.
- `.github/skills/comparar-primitivas/` — `comparar-primitivas` for choosing the right primitive.
- `.github/skills/evaluar-contexto-necesario/` — `evaluar-contexto-necesario` for context evaluation.
- `.github/skills/frontmatter-designer/` — `frontmatter-designer` for frontmatter design.

**Key principle**: A skill becomes worth packaging when it includes bundled assets (templates, checklists, examples) that make its procedure stable and reusable.

## Layer 4 — Persona and Boundaries (Custom Agents)

Agent definition files that specify *who* the AI is and *which tools* it may use. Tool restriction is the defining feature.

- `.github/agents/tutor.agent.md` — Socratic teaching bot with read-only tools and no code editing.

**Key principle**: An agent differs from Ask mode primarily through tool restriction. Removing `editFiles` creates a true read-only guide.

## Layer 5 — Policies (Hooks)

Deterministic shell-command interceptors at agent lifecycle events. They *enforce* behavior rather than *guide* it.

- `.github/hooks/notebook-guardian.json` — `PreToolUse` configuration for notebook read protection.
- `.github/hooks/scripts/notebook-guardian.py` — Python script that denies direct notebook reads and, when possible, points the agent to a cleaned copy.

**Key principle**: Hooks run real shell commands on your machine. They can deterministically allow or deny operations through structured hook output. Instructions cannot — they only guide.

## See Also

- `doc/justificacion.md` — why each primitive was chosen over alternatives
- `README.md` — project overview and usage guide
