# Frontmatter Examples and Anti-patterns

Reference for the `frontmatter-designer` skill. Shows correct frontmatter for each primitive type plus common mistakes.

## Instructions (`.instructions.md`)

```yaml
---
description: "Use when creating or editing Python files. Enforces PEP 8, type hints, and NumPy docstrings."
applyTo: "**/*.py"
---
```

- `applyTo` is a glob: auto-attaches for every matching file.
- Without `applyTo`, the instruction is on-demand (loaded when `description` matches the task).
- Do NOT use `applyTo: "**"` unless the rule truly applies to every file — it wastes context.

## Prompt (`.prompt.md`)

```yaml
---
description: "Review staged git diff and propose a Conventional Commits message."
name: "Commit Message"
argument-hint: "Paste git diff --staged output here"
tools:
  - codebase
---
```

- `name` defaults to the filename if omitted.
- `agent` can redirect to a custom agent: `agent: tutor`.
- `tools` here restrict what the prompt can use (overrides current mode defaults).

## Skill (`SKILL.md`)

```yaml
---
name: csv-eda-basica
description: "Use when starting exploratory data analysis on a CSV file. Detects columns, types, missing values, and distributions. Invoke with: /csv-eda-basica, eda, explore dataset."
argument-hint: "Path to the CSV file to analyse"
user-invocable: true
---
```

- `name` **must** match the folder name exactly (case-sensitive).
- `description` is the primary discovery surface — make it keyword-rich.
- `user-invocable: true` allows `/skill-name` slash command (default is true).
- `disable-model-invocation: true` prevents the model from auto-invoking this skill without explicit user request.

## Custom Agent (`.agent.md`)

```yaml
---
description: "Socratic teaching assistant. Use when you want guided learning: code review, concept explanation, debugging hints. Never writes code."
name: "tutor"
tools:
  - codebase
  - search
  - usages
---
```

- Tools listed here are ALL the tools available to this agent.
- Omitting `editFiles` makes the agent constitutionally read-only.
- `description` drives discovery in the agent picker — use trigger phrases.

## Hook (`.json`)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "python .github/hooks/scripts/notebook-guardian.py",
        "timeout": 15
      }
    ]
  }
}
```

- `type` must be `"command"` (the only supported type).
- Exit code 0 → allow. Exit code 2 → block (error message from stdout shown to user). Other → warn.
- Hook scripts read tool call JSON from stdin and write a response JSON to stdout.

## Common Anti-patterns

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| `description: Use when: doing X` | Unquoted colon breaks YAML | Wrap in quotes: `description: "Use when: doing X"` |
| `applyTo: "**"` on a specific-purpose instruction | Loads into every interaction | Use a specific glob: `"**/*.py"` |
| `name: My Skill` (spaces, uppercase) | Silent failure — does not match folder | Use `name: my-skill` |
| Vague description: `"Helps with code"` | Agent cannot discover it | Add trigger phrases and specific use cases |
| Listing all possible tools for an agent | Gives agent unnecessary capabilities | List only the tools the agent's role actually needs |
