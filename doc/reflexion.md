# Primitive Reflection

## 1. Why are `applyTo`-based instructions better than a single global instruction?

`applyTo` keeps the context narrow. In this repository, the global rules in
[.github/copilot-instructions.md](../.github/copilot-instructions.md) only hold
cross-cutting policies such as language and reproducibility. File-specific
requirements live in
[.github/instructions/python.instructions.md](../.github/instructions/python.instructions.md)
and
[.github/instructions/notebooks.instructions.md](../.github/instructions/notebooks.instructions.md),
so Python rules load for `.py` work and notebook rules load for `.ipynb` work.
That separation is better than a single global instruction because it avoids
injecting irrelevant style rules into every interaction. In a heterogeneous
repository, loading notebook-output rules while editing a Python script or
loading PEP 8 rules while discussing documentation wastes context and makes the
guidance less precise.

## 2. What is the structural difference between a prompt and a skill?

A prompt is a reusable text macro, while a skill is a packaged workflow with
supporting assets. The prompt
[.github/prompts/arch-review.prompt.md](../.github/prompts/arch-review.prompt.md)
is a single focused review instruction: it tells Copilot how to evaluate
architecture, but it does not carry external files. By contrast,
[.github/skills/csv-eda-basica/SKILL.md](../.github/skills/csv-eda-basica/SKILL.md)
depends on a checklist in
[.github/skills/csv-eda-basica/references/eda-checklist.md](../.github/skills/csv-eda-basica/references/eda-checklist.md)
and a notebook template in
[.github/skills/csv-eda-basica/assets/notebook-template.md](../.github/skills/csv-eda-basica/assets/notebook-template.md).
That extra structure is the key difference: a skill packages a stable
procedure, not just an instruction string.

## 3. Why can the `tutor` agent not edit code even if the user asks it to?

The restriction is structural, not merely rhetorical. In
[.github/agents/tutor.agent.md](../.github/agents/tutor.agent.md) the frontmatter
only grants `codebase`, `search`, and `usages`. It does **not** grant
`editFiles`. That means the agent may inspect the repository and discuss it, but
it has no editing capability available in the first place. The body text then
reinforces the same rule by stating that the tutor must guide the user with
questions rather than writing solutions directly. Even a very explicit user
request cannot grant a tool that the agent configuration does not expose.

## 4. Could `notebook-guardian` be implemented as an instruction?

No, because the requirement is deterministic enforcement rather than advice. The
hook configuration in
[.github/hooks/notebook-guardian.json](../.github/hooks/notebook-guardian.json)
registers a `PreToolUse` interceptor, and the implementation in
[.github/hooks/scripts/notebook-guardian.py](../.github/hooks/scripts/notebook-guardian.py)
examines the incoming tool payload before `read_file` executes. If the target is
a notebook, the script returns a deny decision outside the model's normal text
generation loop. An instruction could only say "do not read dirty notebooks,"
but the model could still ignore or misapply that advice. A hook is different:
it is executed by the runtime and its decision is enforced regardless of how the
user phrases the request.
