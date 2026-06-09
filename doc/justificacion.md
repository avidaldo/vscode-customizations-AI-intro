# Customization Primitive Justification

For each primitive used in this project, this document explains:

- How to use it in this repo (command or action, and how to verify it is active).
- Why that primitive was chosen.
- What problems using a different primitive would cause.

---

## Layer 1 — Instructions

### `copilot-instructions.md` (global, always-on)

**How to use:**
No explicit invocation is required. Open any file in the workspace and send a Copilot message; these rules load automatically. To verify, ask Copilot to write content for a solution file and confirm it responds in English, preserves the special status of `actividade.md`, and keeps reproducibility decisions explicit.

**Why instructions?**
Global policies — project language, reproducibility expectations, and cross-cutting references — must apply to every interaction without requiring the user to do anything. Instructions are the only primitive that loads silently and automatically on every turn. Instructions say *how* to write, not *what* to do. The `copilot-instructions.md` file in this project contains only policies (language rule, seed policy, modular instruction principle, internal links). It deliberately contains no task-specific knowledge.

**Why not a prompt or skill?**
A prompt requires explicit invocation (`/`). A skill requires invocation. If the user forgets to invoke them, the policies are not applied. Instructions cannot be forgotten.

---

### `python.instructions.md`, `markdown.instructions.md`, `notebooks.instructions.md` (file-type, `applyTo`)

**How to use:**
No explicit invocation is required. Open `src/train_model.py` and ask Copilot to add a function; it should produce NumPy-style docstrings, type hints, and `snake_case` because `python.instructions.md` auto-loads via `applyTo`. The same pattern applies to notebooks via `notebooks.instructions.md`.

**Why `applyTo` instead of global?**
If PEP 8 rules were in `copilot-instructions.md`, they would load for every interaction — including when the user is asking about a CSV file or a Markdown document. `applyTo: "**/*.py"` ensures Python rules only load when a `.py` file is being edited. This is the **modular context** principle: pay only for the context you need. Modular instructions reduce context window waste. An `applyTo: "**"` instruction on a project with 10 file types would load 10x more unnecessary context than properly scoped instructions.

**Why not a skill?**
A skill requires explicit invocation. Style rules should be passive, so no explicit invocation is required on every file edit. `applyTo` makes them automatic.

---

### `customizations.instructions.md` (file-type, `applyTo`)

**How to use:**
No explicit invocation is required. Open any `.prompt.md`, `.agent.md`, or `SKILL.md` file and ask Copilot to generate or update frontmatter; the instruction auto-loads via `applyTo`. To verify, open `.github/prompts/arch-review.prompt.md` and ask Copilot to propose frontmatter for a new prompt — the fields it suggests (`mode`, `description`, `tools`) should match the conventions in this file.

**Why a separate instruction and not a skill?**
The `frontmatter-designer` skill provides the *procedure* for drafting frontmatter; this instruction file provides the *rules* that the output must satisfy. Separating policy (instruction) from procedure (skill) lets both be maintained independently. If frontmatter conventions change, only the instruction needs updating; the skill's procedure remains valid.

**Why `applyTo` and not global?**
Frontmatter rules are only relevant when editing a customization file. Loading them while working on `src/train_model.py` or a CSV file would add noise without value.

---

## Layer 2 — Prompts

### `tutor-review.prompt.md`

**How to use:**
In Copilot chat, type `/tutor-review` and attach or paste a code block. The prompt routes to the `tutor` agent automatically. Expected behaviour: the agent asks guiding questions rather than writing code.

**Why a prompt and not a skill?**
The review task is a single focused action: "review this code block and ask guiding questions." There are no templates, no sequential steps, no bundled assets. A prompt is the correct choice for a text macro — it just packages a long instruction into a convenient slash command. A prompt is "just a text expansion." Its power comes from consistency and discoverability, not from logic.

**Why `agent: tutor`?**
The requirement is Socratic feedback, not direct fixes. Routing to the `tutor` agent enforces the tool restriction (no `editFiles`) at the agent level. A plain prompt without `agent: tutor` could still produce direct code edits in default Ask mode.

---

### `sdd-check.prompt.md`, `todo-to-plan.prompt.md`

**How to use:**
In Copilot chat, type `/todo-to-plan` to scan the project for TODO comments and receive a prioritised task list, or `/sdd-check` with a specification attached to detect implementation gaps.

**Why prompts and not skills?**
Both tasks are single-pass: read something, analyse it, produce an output. They do not need bundled templates or multi-step procedures that must remain stable across invocations. If the output format needed to be consistent across many runs, they would become skills. At this level of complexity, a prompt is sufficient and simpler. The threshold between prompt and skill is: "Does this task need a stable, reusable template or a multi-step procedure?" If yes, choose a skill; if no, choose a prompt.

---

### `arch-review.prompt.md`

**How to use:**
In Copilot chat, type `/arch-review` with a source file attached (for example `src/train_model.py`). The response returns a scored table over architecture dimensions.

**Why a prompt?**
Architecture review is a read-only analysis task with a structured but not templated output. The evaluation table in the prompt body is defined inline — not a separate file the model must load. If the project had many reviews and needed consistent formatting, the table format could be extracted into a skill asset.

---

## Layer 3 — Skills

### `csv-eda-basica`

**How to use:**
In Copilot chat, type `/csv-eda-basica data/sample.csv`. The skill loads `references/eda-checklist.md` and `assets/notebook-template.md` automatically and executes the sequence load -> inspect -> statistics -> distributions -> questions.

**Why a skill and not a prompt?**
An EDA workflow requires:

1. A checklist of quality dimensions to check (`references/eda-checklist.md`).
2. A notebook template to populate (`assets/notebook-template.md`).
3. Sequential steps (load → check → stats → plot → questions) that must be followed consistently.

A prompt cannot bundle files. A skill with assets ensures the checklist and template are available every time the skill is invoked, regardless of what the user has in their context.

**Why not an instruction?**
EDA is not a style rule — it is a procedure. Instructions shape *how* Copilot writes; they do not drive multi-step workflows.

---

### `comparar-primitivas`, `evaluar-contexto-necesario`, `frontmatter-designer` (meta-skills)

**How to use:**

- `/comparar-primitivas` — describe a requirement and get a primitive recommendation with trade-offs.
- `/evaluar-contexto-necesario` — describe a complex task and get a context attachment plan.
- `/frontmatter-designer` — describe a customization file and get correct frontmatter YAML.

**Why skills?**
Each of these requires a decision table, a checklist, or a set of examples (`references/decision-table.md`, `references/context-checklist.md`, `references/frontmatter-examples.md`) to produce reliable, consistent output.

Without bundled assets, the model would reason from scratch each time and could produce different — or incorrect — decision criteria. Packaging the reference assets in the skill folder ensures stable, repeatable output.
Meta-skills are a strong entry point for users who want to reason about the customization system itself, not just execute one task.

---

### `revision-notebook`

**How to use:**
In Copilot chat, type `/revision-notebook notebooks/01_eda_example.ipynb`. The skill loads `references/quality-checklist.md` and evaluates structure, variable names, and visualisations. Expected output: a checklist report identifying items that fail the criteria, with specific cell references and suggested improvements.

**Why a skill and not a prompt?**
Consistent review output requires a stable quality checklist. A prompt that defines criteria inline would produce different results as the model paraphrases the rules. Bundling `references/quality-checklist.md` as an asset ensures the same criteria are applied on every invocation.

---

### `conventional-commit`, `todo-a-plan`, `spec-a-tareas` (workflow skills)

**How to use:**

- `/conventional-commit` — stage changes with `git add`, then invoke the skill. Optionally paste the output of `git diff --staged` as context. Expected output: a Conventional Commits-formatted message (`type(scope): description`).
- `/todo-a-plan` — invoke with no argument to scan the whole project, or `/todo-a-plan src/` to scope by directory. Expected output: a prioritised backlog table in the format of `doc/backlog.md`, which was produced by this skill.
- `/spec-a-tareas doc/spec.md` — invoke with the path to a specification file. Expected output: an ordered implementation and validation task list. Use alongside `/sdd-check` (which checks an existing implementation against a spec) for a full Spec-Driven Development cycle.

**Why skills and not prompts?**
Each task depends on reference assets that must be stable across invocations:

- `conventional-commit` bundles `references/commit-examples.md` for consistent message style.
- `todo-a-plan` bundles `assets/backlog-template.md` to produce a reproducible table format.
- `spec-a-tareas` bundles `assets/plan-template.md` and `assets/spec-template.md` to enforce the planning structure.

A prompt cannot bundle files. Without reference assets, each invocation would produce a different output format.

---

### `preparar-practica`, `dataset-card`, `debug-python-basico` (supporting skills)

**How to use:**

- `/preparar-practica` — describe a topic and learning objective. Expected output: a structured practice session with progressive steps, checkpoints, and deliverables.
- `/dataset-card data/sample.csv` — invoke with the path to a dataset. Expected output: a structured card covering origin, variables, known biases, licence, and limitations.
- `/debug-python-basico` — paste a Python traceback or describe the unexpected behaviour. Expected output: a structured diagnosis (hypothesis, root cause, minimal fix) following the protocol in `references/debug-protocol.md`.

**Why skills?**
All three require reference material that must remain stable across invocations: `preparar-practica` loads `references/practice-checklist.md`; `dataset-card` loads `assets/dataset-card-template.md`; `debug-python-basico` loads `references/debug-protocol.md`. A prompt for any of these would produce inconsistent structure because the template lives in the asset, not the prompt body.

---

## Layer 4 — Custom Agent

### `tutor.agent.md`

**How to use:**
Open the Copilot agent picker and select `tutor`. Ask for review or explanation. To verify restrictions, request a direct code fix; the expected behaviour is guidance without file edits.

**Why an agent and not Ask mode?**
The core requirement is: the AI must guide without writing code. In default Ask mode, the model can (and often will) produce direct code solutions even when asked not to. Tool restriction at the agent level is *constitutive* — the agent is structurally incapable of calling `editFiles` because it is not in its tools list.

**Why not an instruction that says "do not write code"?**
Instructions are non-deterministic guidance. A sufficiently specific user request ("fix this function") could override an instruction that says "ask questions." The agent's tool list, by contrast, is enforced at the system level — no prompt override can grant tools not listed.

Tool restriction *is* persona. The tutor agent is Socratic not because of its description (though that helps), but because it structurally cannot modify code. This is the key differentiator between a custom agent and a prompted assistant.

---

## Layer 5 — Hook

### `notebook-guardian`

**How to use:**
The hook is loaded automatically via `.github/hooks/notebook-guardian.json`. The current VS Code runtime contract uses `tool_name`, `tool_input`, and `hookSpecificOutput.permissionDecision`. To test that path locally from the project root:

```bash
printf '%s\n' '{"hookEventName":"PreToolUse","tool_name":"read_file","tool_input":{"filePath":"notebooks/01_eda_example.ipynb"},"cwd":"'$PWD'"}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected: {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", ...}}

printf '%s\n' '{"hookEventName":"PreToolUse","tool_name":"read_file","tool_input":{"filePath":"README.md"},"cwd":"'$PWD'"}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected: {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow"}}
```

The repository also keeps compatibility with the simplified manual test payload used in the activity brief:

```bash
echo '{"tool":"read_file","input":{"file":"test.ipynb"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected: {"action": "deny", ...}

echo '{"tool":"read_file","input":{"file":"README.md"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected: {"action": "allow"}
```

**Why a hook and not an instruction?**
The requirement is deterministic enforcement: every `read_file` call on a `.ipynb` file must be intercepted before the tool runs. When `jupyter` is available, the script additionally creates a cleaned temporary copy and tells the agent where to read it instead. An instruction saying "always strip notebook outputs before reading" is non-deterministic — the model may follow it or not.

A hook is a shell script that runs before the tool call. In the current VS Code contract it returns a structured `permissionDecision`; for the simplified activity smoke test it also supports the older `{"action": ...}` format. In both cases the decision is enforced outside the model, so there is no way for the prompt to override it.

**Why not a skill?**
Skills are invoked by the user. The notebook guardian must run automatically on every `read_file` call, so no explicit invocation is required. Hooks are the only primitive triggered by lifecycle events. "Instructions *guide*. Hooks *enforce*." This distinction is critical when non-compliance has high cost (for example, noisy notebook outputs in context).
