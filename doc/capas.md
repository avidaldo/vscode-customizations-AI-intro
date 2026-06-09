# Copilot Customization Architecture (2026)

This document maps each primitive layer to its files in this solution project.

## Layer 1 — Behavior (Instructions)

Markdown instruction files loaded automatically or on-demand to shape how Copilot writes code and documentation.

| File | Scope |
|------|-------|
| `.github/copilot-instructions.md` | Always-on global rules |
| `.github/instructions/python.instructions.md` | Auto-applied to `**/*.py` |
| `.github/instructions/markdown.instructions.md` | Auto-applied to `**/*.md` |
| `.github/instructions/notebooks.instructions.md` | Auto-applied to `**/*.ipynb` |

**Key principle**: Instructions say *how* to write things, not *what* to do. They are injected silently into context.

## Layer 2 — Task Invocation (Prompt Files)

Reusable chat macros that trigger a focused, parameterized action via `/` slash commands.

| File | Purpose |
|------|---------|
| `.github/prompts/tutor-review.prompt.md` | Code review via the Socratic tutor agent |
| `.github/prompts/sdd-check.prompt.md` | Spec-driven: identify pending items and implement them |
| `.github/prompts/todo-to-plan.prompt.md` | Scan TODOs and generate a prioritized plan |
| `.github/prompts/arch-review.prompt.md` | Architecture and best-practices critical review |

**Key principle**: A prompt is a text macro — no bundled assets. If it needs templates or multi-step procedures, it should be a skill.

## Layer 3 — Workflow (Skills)

Self-contained capability packages invoked via `/` slash commands. Each skill includes a `SKILL.md` plus optional scripts, templates, and checklists in the same folder.

| Folder | Skill | Domain |
|--------|-------|--------|
| `.github/skills/csv-eda-basica/` | `csv-eda-basica` | Data analysis |
| `.github/skills/revision-notebook/` | `revision-notebook` | Notebook quality |
| `.github/skills/dataset-card/` | `dataset-card` | Dataset documentation |
| `.github/skills/debug-python-basico/` | `debug-python-basico` | Python debugging |
| `.github/skills/todo-a-plan/` | `todo-a-plan` | Project planning |
| `.github/skills/spec-a-tareas/` | `spec-a-tareas` | Spec-driven development |
| `.github/skills/preparar-practica/` | `preparar-practica` | Practice preparation |
| `.github/skills/conventional-commit/` | `conventional-commit` | Git commits |
| `.github/skills/comparar-primitivas/` | `comparar-primitivas` | Meta: choose the right primitive |
| `.github/skills/evaluar-contexto-necesario/` | `evaluar-contexto-necesario` | Meta: context evaluation |
| `.github/skills/frontmatter-designer/` | `frontmatter-designer` | Meta: frontmatter design |

**Key principle**: A skill becomes worth packaging when it includes bundled assets (templates, checklists, examples) that make its procedure stable and reusable.

## Layer 4 — Persona and Boundaries (Custom Agents)

Agent definition files that specify *who* the AI is and *which tools* it may use. Tool restriction is the defining feature.

| File | Role |
|------|------|
| `.github/agents/tutor.agent.md` | Socratic teaching bot — read-only tools, no code editing |

**Key principle**: An agent differs from Ask mode primarily through tool restriction. Removing `editFiles` creates a true read-only guide.

## Layer 5 — Policies (Hooks)

Deterministic shell-command interceptors at agent lifecycle events. They *enforce* behavior rather than *guide* it.

| File | Event | Action |
|------|-------|--------|
| `.github/hooks/notebook-guardian.json` | `PreToolUse` | Block `read_file` on `.ipynb`; serve clean version |
| `.github/hooks/scripts/notebook-guardian.py` | — | Python script implementing the guardian logic |

**Key principle**: Hooks run real shell commands on your machine. They can block operations with a non-zero exit code. Instructions cannot — they only guide.

## See Also

- `doc/justificacion.md` — why each primitive was chosen over alternatives
- `README.md` — project overview and usage guide