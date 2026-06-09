# Python Debugging Protocol

A step-by-step guide for diagnosing Python exceptions systematically.

## Step 1 — Read the Full Traceback

Never look at only the last line. The traceback is a call stack — read it top-to-bottom:

```
Traceback (most recent call last):        ← start here
  File "src/train_model.py", line 87, in train
    loss = criterion(logits, y_batch)     ← last user-code frame
  File ".../torch/nn/modules/loss.py", line 1, in forward
    ...
RuntimeError: Expected target size (32,), got torch.Size([32, 1])  ← exception type + message
```

**Key fields to extract:**
- Exception type: `RuntimeError`
- Message: `Expected target size (32,), got torch.Size([32, 1])`
- Last user frame: `src/train_model.py`, line 87

## Step 2 — Identify the Root Cause Category

| Exception Type | Common Causes |
|----------------|---------------|
| `ValueError` | Wrong value passed (shape mismatch, bad range) |
| `TypeError` | Wrong type (e.g., `str` where `int` expected) |
| `AttributeError` | Accessing a non-existent attribute (typo, wrong object) |
| `IndexError` | List/array index out of bounds |
| `KeyError` | Dictionary key not found |
| `RuntimeError` (PyTorch) | Shape mismatch, device mismatch (`cpu` vs `cuda`) |
| `ImportError` | Package not installed or wrong name |

## Step 3 — Narrow the Location

Open the file and line from the traceback. Before the failing line, insert:

```python
# Temporary debug print — remove before committing
print(f"[DEBUG] variable_name type={type(variable_name)}, value={variable_name!r}")
```

For tensors:
```python
print(f"[DEBUG] tensor shape={tensor.shape}, dtype={tensor.dtype}, device={tensor.device}")
```

## Step 4 — Formulate One Hypothesis

Write it explicitly: *"I think the error is caused by X because Y."*

Do not guess multiple causes at once. Test one, then move to the next if wrong.

## Step 5 — Apply the Minimal Fix

- Change only the line(s) necessary.
- Do not refactor, rename, or move code while debugging — that introduces new bugs.
- After fixing, remove all `[DEBUG]` print statements.

## Step 6 — Add a Guard

After fixing, add a boundary check so the bug cannot silently reappear:

```python
assert y_batch.ndim == 1, f"Expected 1D labels, got shape {y_batch.shape}"
```

## Common PyTorch Shape Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Expected target size (N,), got (N, 1)` | `y` has extra dim | `y = y.squeeze(1)` |
| `Expected input batch_size (N) to match target batch_size (M)` | loader shuffled differently | Check `batch_size` in DataLoader |
| `RuntimeError: Expected all tensors to be on the same device` | mixed `cpu`/`cuda` | `x = x.to(device)` before forward pass |
