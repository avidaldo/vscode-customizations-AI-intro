# Primitive Decision Table

Use this table when a requirement could be satisfied by more than one primitive.

## Quick Filter

| If you need to... | Use |
|-------------------|-----|
| Apply rules to every interaction silently | **Instructions** (global, no frontmatter) |
| Apply rules only when editing specific file types | **Instructions** (with `applyTo` glob) |
| Run a single focused task with text inputs | **Prompt** |
| Run a multi-step workflow with templates/checklists | **Skill** |
| Give the AI a restricted role and identity | **Custom Agent** |
| Deterministically block or transform tool calls | **Hook** |

## Detailed Comparison

| Dimension | Instructions | Prompt | Skill | Custom Agent | Hook |
|-----------|-------------|--------|-------|--------------|------|
| **Trigger** | Always-on or file match | `/` slash command | `/` slash command | Agent picker | Lifecycle event |
| **Has assets** | No | No | Yes (templates, scripts) | No | Yes (shell script) |
| **Multi-step** | No | Simple | Yes | Yes | No |
| **Tool restriction** | No | Partial | No | Yes | Yes (blocks tools) |
| **Deterministic** | No | No | No | No | **Yes** |
| **Edits files** | Guides edits | Yes | Yes | Depends on tools | Via script |
| **Reusable templates** | No | No | **Yes** | No | No |

## Common Confusions

### Instructions vs Skill
- **Instructions** apply passively and always. They shape *style*, not *workflow*.
- **Skills** are invoked explicitly for a *specific task*. They have bundled assets that make the procedure stable.
- Rule: if it needs a template or a checklist to be reliable → Skill.

### Prompt vs Skill
- Both are invoked via `/` slash commands.
- A **Prompt** is a text macro — no files, no multi-step procedure.
- A **Skill** is a workflow package — has a folder with assets, sequential steps, and stable output format.
- Rule: if you need to reference a template or follow >3 steps consistently → Skill.

### Skill vs Custom Agent
- A **Skill** uses whatever tools are available in the current mode.
- A **Custom Agent** explicitly restricts or grants tools, creating a distinct *persona*.
- Rule: if tool restriction (e.g., read-only) defines the requirement → Custom Agent.

### Instructions vs Hook
- **Instructions** *guide* the model (non-deterministic — it can still ignore them).
- **Hooks** *enforce* behaviour via shell commands at lifecycle events (deterministic).
- Rule: if the requirement is a policy that must never be violated → Hook.

## Examples from This Project

| Primitive | File | Why this choice |
|-----------|------|-----------------|
| Instruction (global) | `.github/copilot-instructions.md` | Always-on project context |
| Instruction (file-type) | `.github/instructions/python.instructions.md` | PEP 8 rules only when editing `.py` files |
| Prompt | `.github/prompts/arch-review.prompt.md` | Single focused review task, no assets needed |
| Skill | `.github/skills/csv-eda-basica/` | Multi-step EDA procedure + notebook template |
| Custom Agent | `.github/agents/tutor.agent.md` | Socratic persona requires removing `editFiles` |
| Hook | `.github/hooks/notebook-guardian.json` | Must block `read_file` on dirty notebooks — cannot be a guideline |
