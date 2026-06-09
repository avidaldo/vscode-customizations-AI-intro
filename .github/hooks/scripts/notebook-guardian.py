#!/usr/bin/env python3
"""
notebook-guardian.py -- PreToolUse hook for Copilot notebook reads.

Purpose
-------
Intercept ``read_file`` calls targeting ``.ipynb`` files.
Notebook JSON can contain large embedded outputs that waste context and make
review harder. This hook blocks direct notebook reads and, when possible,
produces a cleaned temporary copy with outputs removed.

Compatibility
-------------
The repository activity describes a simplified legacy contract using
``{"tool": ..., "input": {"file": ...}}`` and ``{"action": ...}`` outputs.
Current VS Code hooks use ``tool_name``, ``tool_input``, and
``hookSpecificOutput.permissionDecision``. This script accepts both input
formats. It emits the modern response shape for real hook execution and keeps
the legacy output for the manual activity smoke tests.
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


PRE_TOOL_USE_EVENT = "PreToolUse"


def _emit_json(payload: dict[str, object], exit_code: int = 0) -> None:
    """Write a JSON response to stdout and exit.

    Parameters
    ----------
    payload : dict[str, object]
        JSON-serializable response payload.
    exit_code : int, default=0
        Process exit code to return after writing the payload.
    """
    print(json.dumps(payload))
    sys.exit(exit_code)


def _allow(legacy_mode: bool) -> None:
    """Emit an allow response for the active hook contract.

    Parameters
    ----------
    legacy_mode : bool
        Whether the incoming payload used the simplified activity contract.
    """
    if legacy_mode:
        _emit_json({"action": "allow"})

    _emit_json(
        {
            "hookSpecificOutput": {
                "hookEventName": PRE_TOOL_USE_EVENT,
                "permissionDecision": "allow",
            }
        }
    )


def _deny(message: str, legacy_mode: bool, additional_context: str | None) -> None:
    """Emit a deny response for the active hook contract.

    Parameters
    ----------
    message : str
        User-visible reason for denying the tool call.
    legacy_mode : bool
        Whether the incoming payload used the simplified activity contract.
    additional_context : str | None
        Extra guidance for the current VS Code hook contract.
    """
    if legacy_mode:
        _emit_json({"action": "deny", "message": message}, exit_code=2)

    response: dict[str, object] = {
        "hookSpecificOutput": {
            "hookEventName": PRE_TOOL_USE_EVENT,
            "permissionDecision": "deny",
            "permissionDecisionReason": message,
        }
    }
    if additional_context:
        response["hookSpecificOutput"]["additionalContext"] = additional_context

    _emit_json(response)


def _extract_tool_payload(
    payload: dict[str, object],
) -> tuple[bool, str, dict[str, object]]:
    """Return compatibility mode, tool name, and tool input.

    Parameters
    ----------
    payload : dict[str, object]
        Hook payload read from stdin.

    Returns
    -------
    tuple[bool, str, dict[str, object]]
        ``(legacy_mode, tool_name, tool_input)``.
    """
    legacy_mode = "tool" in payload or "input" in payload
    tool_name = str(payload.get("tool_name") or payload.get("tool") or "")

    raw_tool_input = payload.get("tool_input") or payload.get("input") or {}
    if isinstance(raw_tool_input, dict):
        tool_input = raw_tool_input
    else:
        tool_input = {}

    return legacy_mode, tool_name, tool_input


def _resolve_path(path_value: str, workspace_root: Path) -> Path:
    """Resolve a possibly relative path against the workspace root.

    Parameters
    ----------
    path_value : str
        Path extracted from the tool input.
    workspace_root : Path
        Workspace root from the hook payload, or the current working directory.

    Returns
    -------
    Path
        Absolute path candidate.
    """
    candidate = Path(path_value)
    if candidate.is_absolute():
        return candidate
    return workspace_root / candidate


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
    """Read stdin, apply the notebook policy, and emit a hook response."""
    try:
        raw = sys.stdin.read()
        payload: dict[str, object] = json.loads(raw)
    except (json.JSONDecodeError, ValueError) as exc:
        # Malformed input should not block unrelated tool calls.
        sys.stderr.write(f"notebook-guardian: could not parse stdin: {exc}\n")
        _allow(legacy_mode=False)

    legacy_mode, tool_name, tool_input = _extract_tool_payload(payload)
    workspace_root = Path(str(payload.get("cwd") or Path.cwd()))

    if tool_name != "read_file":
        _allow(legacy_mode)

    file_arg = str(
        tool_input.get("filePath")
        or tool_input.get("file")
        or tool_input.get("path")
        or ""
    )
    if not file_arg:
        _allow(legacy_mode)

    notebook_path = _resolve_path(file_arg, workspace_root)
    if notebook_path.suffix.lower() != ".ipynb":
        _allow(legacy_mode)

    if not notebook_path.exists():
        _allow(legacy_mode)

    message = (
        f"Direct read of {notebook_path.name} was blocked to avoid loading "
        "embedded notebook outputs into the agent context."
    )
    additional_context = (
        "Clear notebook outputs before reading it, or ask for a cleaned copy."
    )
    try:
        clean_path = _strip_outputs(notebook_path)
    except RuntimeError as exc:
        message = (
            f"{message} Automatic output stripping failed: {exc}. "
            "Please clear outputs manually before retrying."
        )
    else:
        message = (
            f"{message} A cleaned copy is available at: {clean_path}."
        )
        additional_context = (
            f"Read the cleaned notebook copy at {clean_path} instead of the "
            "original notebook path."
        )

    _deny(message, legacy_mode=legacy_mode, additional_context=additional_context)


if __name__ == "__main__":
    main()
