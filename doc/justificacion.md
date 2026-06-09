# Customization Primitive Justification

For each primitive used in this project, this document explains:

- How to use it in this repo (command or action, and how to verify it is active).
- Why that primitive was chosen.
- What problems using a different primitive would cause.

---

## Layer 1 — Instructions

### `copilot-instructions.md` (global, always-on)

**How to use:**
No explicit invocation is required. Open any file in the workspace and send a Copilot message; these rules load automatically. To verify, ask Copilot to write content and confirm it responds in English and follows cross-cutting policies.

**Why instructions?**
Global policies — project language (English), cross-cutting references — must apply to every interaction without requiring the user to do anything. Instructions are the only primitive that loads silently and automatically on every turn. Instructions say *how* to write, not *what* to do. The `copilot-instructions.md` file in this project contains only policies (language rule, modular instruction principle, internal links). It deliberately contains no task-specific knowledge.

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
The hook is loaded automatically via `.github/hooks/notebook-guardian.json`. To test it locally from the project root:

```bash
echo '{"tool":"read_file","input":{"file":"test.ipynb"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected: {"action": "deny", ...}

echo '{"tool":"read_file","input":{"file":"README.md"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected: {"action": "allow"}
```

**Why a hook and not an instruction?**
The requirement is deterministic enforcement: every `read_file` call on a `.ipynb` file must be intercepted, the outputs stripped, and the clean file served instead. An instruction saying "always strip notebook outputs before reading" is non-deterministic — the model may follow it or not.

A hook is a shell script that runs before the tool call. It either returns `{"action": "allow"}` or `{"action": "deny"}`. There is no way for the model to override it.

**Why not a skill?**
Skills are invoked by the user. The notebook guardian must run automatically on every `read_file` call, so no explicit invocation is required. Hooks are the only primitive triggered by lifecycle events. "Instructions *guide*. Hooks *enforce*." This distinction is critical when non-compliance has high cost (for example, noisy notebook outputs in context).
