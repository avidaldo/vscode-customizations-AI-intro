# Activity A04 — GitHub Copilot Customizations for Efficient AI Programming

**Module:** MP5073 Programming of Artificial Intelligence  
**Didactic Unit:** UD01 — Programming Ecosystem for AI

---

## Introduction

GitHub Copilot is not only an autocomplete assistant. In VS Code it is a configurable AI system that can adapt to repository context, coding conventions, and concrete development workflows. That adaptation is expressed through **customization primitives** such as instructions, prompts, skills, agents, and hooks.

In this activity you will build a coherent set of Copilot customizations for an AI-oriented repository. This repository is the reference solution. Use it to understand the expected structure and rationale, but reproduce the work in your own submission.

If you need the official wording of the activity, read `actividade.md`, which remains in Galician. This file is the English student-facing brief for the same A04 activity.

---

## Tasks

### Task 1. Global and File-Specific Instructions (Layer 1 — Instructions)

**Objective:** Configure rules that apply across the repository without explicit invocation.

**Instructions:**

Create a `.github/copilot-instructions.md` file with:

1. A short description of the project context.
2. At least two cross-cutting policies, such as documentation language and seed policy for reproducibility.
3. References to the file-specific instruction files created in the next step.

Then create file-specific instructions for at least **two file types** using `applyTo`:

- `.github/instructions/python.instructions.md` — Python style rules such as PEP 8, type hints, and NumPy docstrings.
- `.github/instructions/notebooks.instructions.md` — notebook rules such as narrative structure and clean outputs.

**Hints:**

- Compare what belongs in the global instructions file versus what belongs in an `applyTo` instruction.
- Ask yourself what happens if every rule is loaded globally, even when the user is not editing that file type.

**Self-assessment:**

- [ ] `copilot-instructions.md` exists and contains at least two cross-cutting policies.
- [ ] `python.instructions.md` uses `applyTo: "**/*.py"` in valid YAML frontmatter.
- [ ] `notebooks.instructions.md` uses `applyTo: "**/*.ipynb"` in valid YAML frontmatter.
- [ ] The solution files are written in English.
- [ ] Opening a `.py` file in VS Code causes Copilot to load the Python-specific rules automatically.

---

### Task 2. Stored Prompts (Layer 2 — Prompts)

**Objective:** Create reusable text macros for frequent tasks.

**Instructions:**

Create at least **two prompt files** in `.github/prompts/`:

1. `arch-review.prompt.md` — a prompt that analyses project architecture and reports strengths and weaknesses.
2. `todo-to-plan.prompt.md` — a prompt that scans project `TODO` comments and turns them into a prioritised task list with effort estimates.

**Hints:**

- A prompt is a text expansion. It does not contain packaged assets or its own execution logic.
- Use `$input` if you want the prompt to accept an argument.
- Compare these prompts with the skills in the reference solution and identify the structural difference.

**Self-assessment:**

- [ ] Both prompt files have valid YAML frontmatter.
- [ ] The `description` field clearly explains when each prompt should be used.
- [ ] `/arch-review` is invocable from Copilot chat.
- [ ] The prompt body does not embed long templates or checklists that would justify turning it into a skill.

---

### Task 3. Custom Agent (Layer 4 — Custom Agents)

**Objective:** Create an agent with a clear persona and explicit tool restrictions.

**Instructions:**

Create an agent in `.github/agents/tutor.agent.md` that behaves as a Socratic teaching assistant:

- It answers with guiding questions when appropriate.
- It **never writes code directly**. It explains, guides, and gives hints only.
- It can read the codebase, but it cannot edit files.

The frontmatter must list **only** the tools needed for a read-only assistant. Omitting `editFiles` is enough to make the agent structurally incapable of modifying code.

**Hints:**

- The difference between a custom agent and default Ask mode is not only the instructions; it is also the `tools` list.
- Open the `tutor` agent from the Copilot agent picker and ask it to review `train()` in `src/train_model.py`.
- Consider what would change if you added `editFiles` to the tools list.

**Self-assessment:**

- [ ] `tutor.agent.md` exists in `.github/agents/`.
- [ ] The frontmatter includes at least `codebase` and `search`, but omits `editFiles`.
- [ ] The `description` contains discoverable keywords such as `tutor`, `review`, `explain`, and `guide`.
- [ ] When tested, the agent responds with questions and avoids direct code fixes.

---

### Task 4. Skills (Layer 3 — Skills)

**Objective:** Create at least two skills with packaged assets.

**Instructions:**

Create the following skills in `.github/skills/`:

**Skill A: `csv-eda-basica`**

- `SKILL.md` with the EDA procedure steps: load, quality checks, statistics, distributions, and initial questions.
- A quality checklist in `references/eda-checklist.md`.
- A notebook template in `assets/notebook-template.md`.

**Skill B: `conventional-commit`**

- `SKILL.md` that proposes a commit message from a git diff using the [Conventional Commits](https://www.conventionalcommits.org/) specification.
- Correct commit examples in `references/commit-examples.md`.

**Hints:**

- The `name` field in `SKILL.md` must match the folder name **exactly**.
- Ask yourself why `csv-eda-basica` is a skill rather than a prompt: does it need packaged assets and a stable multi-step workflow?
- Verify that `/csv-eda-basica` appears as a slash command in Copilot chat.

**Self-assessment:**

- [ ] `csv-eda-basica/SKILL.md` has `name: csv-eda-basica`.
- [ ] `conventional-commit/SKILL.md` has `name: conventional-commit`.
- [ ] Both skills include at least one packaged asset or reference file.
- [ ] `/csv-eda-basica data/sample.csv` produces a structured analysis or a notebook proposal.
- [ ] Each skill `description` includes natural trigger phrases that users would actually type.

**Going further (optional):**

Try the additional skills included in this repository, such as `/debug-python-basico`, `/spec-a-tareas`, and `/dataset-card`. As an extension exercise, design a new skill with help from `/frontmatter-designer` and `/comparar-primitivas`.

---

### Task 5. Policy Hook (Layer 5 — Hooks)

**Objective:** Implement a deterministic interceptor for a repository policy.

**Instructions:**

Create a hook in `.github/hooks/` that intercepts `read_file` calls on `.ipynb` files and protects the agent context from embedded notebook outputs:

1. `.github/hooks/notebook-guardian.json` — configure the `PreToolUse` event to execute the Python script.
2. `.github/hooks/scripts/notebook-guardian.py` — a Python script that reads JSON from stdin, detects notebook reads, blocks them deterministically, and allows all other reads.

The simplified manual smoke test used in the classroom activity is:

```bash
echo '{"tool":"read_file","input":{"file":"test.ipynb"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected output: {"action": "deny", "message": "..."}

echo '{"tool":"read_file","input":{"file":"README.md"}}' | python3 .github/hooks/scripts/notebook-guardian.py
# Expected output: {"action": "allow"}
```

The reference solution also supports the current VS Code `PreToolUse` contract used at runtime, where the hook returns `hookSpecificOutput.permissionDecision`.

**Hints:**

- Hooks are the only deterministic primitive in the customization stack.
- A script running before the tool call cannot be ignored by the model.
- This is why the requirement cannot be solved reliably with an instruction that says "do not read dirty notebooks".

**Self-assessment:**

- [ ] `notebook-guardian.json` uses the `{"hooks": {"PreToolUse": [...]}}` structure.
- [ ] The Python script passes the two terminal tests above.
- [ ] The script uses `json.loads(sys.stdin.read())` to read the payload.
- [ ] The deny path and allow path are clearly distinguished and documented.

---

### Task 6. Primitive Reflection

**Objective:** Consolidate your understanding of when to use each primitive.

**Instructions:**

Using the `comparar-primitivas` skill from this repository, write answers in `doc/reflexion.md` to the following questions:

1. Why are `applyTo`-based instructions better than a single global instruction in heterogeneous repositories?
2. What is the key structural difference between a prompt and a skill? Give one repository example of each.
3. Why is the `tutor` agent unable to edit code even if the user explicitly asks it to?
4. Could the `notebook-guardian` hook be implemented as an instruction? Why or why not?

**Self-assessment:**

- [ ] `doc/reflexion.md` answers all four questions.
- [ ] Each answer cites at least one concrete file in the repository as evidence.
- [ ] The document is written entirely in English.

---

## Submission

At minimum, the repository should contain:

- `.github/copilot-instructions.md`
- `.github/instructions/python.instructions.md` and `notebooks.instructions.md`
- `.github/prompts/arch-review.prompt.md` and `todo-to-plan.prompt.md`
- `.github/agents/tutor.agent.md`
- `.github/skills/csv-eda-basica/` and `conventional-commit/`
- `.github/hooks/notebook-guardian.json` and `.github/hooks/scripts/notebook-guardian.py`
- `doc/reflexion.md`

Submit the GitHub repository link through the platform deliverable.

## Resources

- [README.md](README.md) — repository overview and file map.
- [doc/capas.md](doc/capas.md) — layer-by-layer architecture overview.
- [doc/justificacion.md](doc/justificacion.md) — justification for the primitive choices.
- [Official Copilot customization documentation](https://code.visualstudio.com/docs/copilot/copilot-customization).
