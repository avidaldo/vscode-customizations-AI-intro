---
description: "Ask the Socratic tutor agent to review a specific function or class and provide guided feedback."
name: "Tutor Code Review"
argument-hint: "Paste or reference the function/class you want reviewed"
agent: tutor
---

Please review the following code with a Socratic approach. Do not rewrite it — instead:

1. Identify up to three issues or improvement areas.
2. For each, ask a guiding question that leads me to discover the fix myself.
3. If the code follows all best practices defined in `.github/instructions/python.instructions.md`, say so explicitly.

Code to review:

$input
