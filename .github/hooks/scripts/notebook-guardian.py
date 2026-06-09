#!/usr/bin/env python3
"""
notebook-guardian.py — PreToolUse hook for GitHub Copilot agents.

Purpose
-------
Intercept any ``read_file`` call targeting a ``.ipynb`` file.
Jupyter notebooks accumulate large binary outputs (plots, tensors, HTML) in
their JSON representation.  Reading a dirty notebook wastes the agent's context
window and can expose sensitive intermediate data.

This script:
  1. Reads a tool-call JSON object from stdin.
  2. If the tool is ``read_file`` and the target file ends in ``.ipynb``:
     a. Creates a temporary copy of the notebook with all outputs stripped
        using ``jupyter nbconvert --clear-output``.
     b. Returns a ``deny`` action so the agent does not read the original file,
        together with a message pointing to the clean copy.
  3. For all other tool calls, returns ``allow`` immediately.

Hook contract
-------------
Input (stdin)::

    {
        "tool": "<tool_name>",
        "input": {
            "file": "<path_to_file>",
            ...
        }
    }

Output (stdout) — allow::

    {"action": "allow"}

Output (stdout) — deny::

    {
        "action": "deny",
        "message": "Outputs stripped. Read the clean notebook at: <tmppath>"
    }

Exit codes
----------
- 0: action written to stdout successfully.
- 2: blocking error (shown to the user as an error message).
- Other non-zero: warning (non-blocking).

Usage
-----
Configured in ``.github/hooks/notebook-guardian.json`` as a ``PreToolUse`` hook.
Can also be tested manually::

    echo '{"tool":"read_file","input":{"file":"notebooks/01_eda_example.ipynb"}}' \\
        | python .github/hooks/scripts/notebook-guardian.py
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def _allow() -> None:
    """Write an allow response to stdout and exit 0."""
    print(json.dumps({"action": "allow"}))
    sys.exit(0)


def _deny(message: str) -> None:
    """Write a deny response to stdout and exit 2 (blocking)."""
    print(json.dumps({"action": "deny", "message": message}))
    sys.exit(2)


def _strip_outputs(notebook_path: Path) -> Path:
    """Return a path to a temporary notebook with all cell outputs stripped.

    Parameters
    ----------
    notebook_path : Path
        Absolute path to the original ``.ipynb`` file.

    Returns
    -------
    Path
        Path to the cleaned notebook in a temporary directory.
        The caller is responsible for cleanup.

    Raises
    ------
    RuntimeError
        If ``jupyter nbconvert`` is not available or exits with an error.
    """
    if not shutil.which("jupyter"):
        raise RuntimeError(
            "jupyter is not installed or not on PATH. "
            "Install it with: pip install jupyter"
        )

    tmp_dir = Path(tempfile.mkdtemp(prefix="copilot-nb-clean-"))
    tmp_notebook = tmp_dir / notebook_path.name

    # Copy the original so nbconvert can write the cleaned version next to it
    shutil.copy2(notebook_path, tmp_notebook)

    result = subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--clear-output",
            "--inplace",
            str(tmp_notebook),
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"jupyter nbconvert failed:\n{result.stderr}"
        )

    return tmp_notebook


def main() -> None:
    """Entry point: read stdin, decide allow/deny."""
    try:
        raw = sys.stdin.read()
        payload: dict = json.loads(raw)
    except (json.JSONDecodeError, ValueError) as exc:
        # Malformed input — allow through and let the agent handle it
        sys.stderr.write(f"notebook-guardian: could not parse stdin: {exc}\n")
        _allow()

    tool_name: str = payload.get("tool", "")
    tool_input: dict = payload.get("input", {})

    # Only intercept read_file calls
    if tool_name != "read_file":
        _allow()

    file_arg: str = tool_input.get("file", "")
    notebook_path = Path(file_arg)

    # Only intercept .ipynb files
    if notebook_path.suffix.lower() != ".ipynb":
        _allow()

    # Resolve to absolute path relative to CWD if not absolute
    if not notebook_path.is_absolute():
        notebook_path = Path.cwd() / notebook_path

    if not notebook_path.exists():
        # File not found — allow through; the agent will handle the missing file error
        _allow()

    try:
        clean_path = _strip_outputs(notebook_path)
    except RuntimeError as exc:
        _deny(
            f"notebook-guardian: could not strip outputs from {notebook_path.name}. "
            f"Error: {exc}. "
            "Please clear outputs manually before the agent reads this notebook."
        )

    _deny(
        f"Direct read of a dirty notebook was blocked. "
        f"A clean copy (outputs stripped) is available at: {clean_path}. "
        f"Please read that path instead."
    )


if __name__ == "__main__":
    main()
