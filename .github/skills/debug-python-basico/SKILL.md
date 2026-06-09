---
name: debug-python-basico
description: "Use when a Python script raises an exception or produces unexpected output. Follows a structured protocol: read the traceback, locate the line, isolate a hypothesis, propose the minimal fix. Invoke with: /debug-python-basico, debug, fix error, traceback, exception, python error."
argument-hint: "Paste the full traceback or describe the unexpected behaviour"
user-invocable: true
---

# Skill: debug-python-basico

Follow a structured protocol to diagnose and fix a Python error.

## Steps

### 1. Read the Traceback
- If a traceback is provided, identify:
  - The **exception type** (e.g., `ValueError`, `IndexError`, `AttributeError`).
  - The **last frame** — the file and line number where the error was raised.
  - The **root call** — the first frame in user code that initiated the chain.
- If no traceback is provided, ask the user to run the script and paste the full output.

### 2. Locate the Problematic Line
- Open the file at the line indicated by the traceback.
- Read 5 lines before and after for context.
- Refer to the protocol in [`references/debug-protocol.md`](./references/debug-protocol.md).

### 3. Isolate a Hypothesis
- State one specific hypothesis about the cause: "The tensor shape is (N, 1) but the loss function expects (N,)."
- Do not jump to a fix before verifying the hypothesis.

### 4. Verify
- Add a temporary `print` or `assert` statement to confirm the hypothesis before changing logic.
- Example: `print(f"Shape: {tensor.shape}")` before the failing line.

### 5. Propose the Minimal Fix
- Suggest the smallest code change that resolves the issue.
- Do not refactor surrounding code — fix only what is broken.
- Explain why the fix works.

### 6. Prevent Recurrence
- Add a `assert` or type check at the boundary where the bad value enters the function.
- Suggest a test case that would have caught this error.

## Output

A numbered diagnosis (hypothesis → verification → fix) with the exact line to change.
