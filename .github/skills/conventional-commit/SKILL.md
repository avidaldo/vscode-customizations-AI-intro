---
name: conventional-commit
description: "Use when writing a git commit message. Proposes a clear, Conventional Commits-compliant message from the staged changes. Invoke with: /conventional-commit, commit message, write commit, git commit, stage and commit."
argument-hint: "Optional: paste the output of 'git diff --staged' if not already in context"
user-invocable: true
---

# Skill: conventional-commit

Propose a Conventional Commits-compliant commit message from staged changes.

## When Not to Use

- Do not use this skill for unstaged work you have not reviewed yet.
- Do not use this skill when a repository enforces a different commit convention.

## Why This Is a Skill

This workflow is packaged as a skill rather than a plain prompt because it
depends on reusable reference material in
[`references/commit-examples.md`](./references/commit-examples.md). Keeping the
examples outside the main file makes the guidance easier to maintain and keeps
the output more stable across repeated invocations.

## Steps

### 1. Read the Staged Diff
- If a diff is provided in the argument, use it.
- Otherwise, run `git diff --staged` to read the current staged changes.

### 2. Classify the Change
Determine the primary change type from the diff:

| Type | When to use |
|------|-------------|
| `feat` | New feature or capability added |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace — no logic change |
| `refactor` | Code restructure without behaviour change |
| `test` | Adding or fixing tests |
| `chore` | Build system, tooling, configuration |

Refer to [`references/commit-examples.md`](./references/commit-examples.md) for examples.

### 3. Identify the Scope (optional)
- If the change is confined to a specific module or directory, add it as a scope: `feat(train): ...`
- If the change spans the whole project, omit the scope.

### 4. Write the Message
Format:
```
<type>(<scope>): <short description in imperative mood>

[optional body: why this change was made]

[optional footer: BREAKING CHANGE: or Closes #issue]
```

Rules:
- First line ≤ 72 characters.
- Imperative mood: "Add seed parameter" not "Added seed parameter".
- No period at the end of the first line.

### 5. Propose Alternatives
- Offer 2–3 candidate messages ranked by precision.
- Let the user choose or refine.

## Output

2–3 candidate commit messages with a brief justification for the top recommendation.