from pathlib import Path
import subprocess

WORKSPACE = None

EXCLUDED_DIRS = {
    ".git",
    "venv",
    ".venv",
    "__pycache__",
    "node_modules"
}


# ============================================================
# WORKSPACE
# ============================================================

def set_workspace(workspace: str):

    global WORKSPACE

    workspace_path = Path(workspace).resolve()

    if not workspace_path.exists():
        raise ValueError(
            f"Workspace does not exist: {workspace}"
        )

    if not workspace_path.is_dir():
        raise ValueError(
            f"Workspace is not a directory: {workspace}"
        )

    WORKSPACE = workspace_path


def resolve_path(path: str) -> Path:

    if WORKSPACE is None:
        raise ValueError(
            "Workspace not configured"
        )

    full_path = (WORKSPACE / path).resolve()

    try:
        full_path.relative_to(WORKSPACE)

    except ValueError:
        raise ValueError(
            "Access outside workspace denied"
        )

    return full_path


# ============================================================
# FILE TOOLS
# ============================================================

def list_files(path="."):

    directory = resolve_path(path)

    files = []

    for item in directory.rglob("*"):

        if any(
            part in EXCLUDED_DIRS
            for part in item.parts
        ):
            continue

        if item.is_file():
            files.append(
                str(item.relative_to(WORKSPACE))
            )

    return files


def find_file(filename: str):

    matches = []

    for item in WORKSPACE.rglob("*"):

        if any(
            part in EXCLUDED_DIRS
            for part in item.parts
        ):
            continue

        if item.is_file():

            if item.name.lower() == filename.lower():

                matches.append(
                    str(item.relative_to(WORKSPACE))
                )

    return matches


def search_files(query: str):

    matches = []

    query = query.lower()

    for item in WORKSPACE.rglob("*"):

        if any(
            part in EXCLUDED_DIRS
            for part in item.parts
        ):
            continue

        if not item.is_file():
            continue

        try:

            text = item.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if query in text.lower():

                matches.append(
                    str(item.relative_to(WORKSPACE))
                )

        except Exception:
            pass

    return matches


def read_file(path: str):

    try:

        file_path = resolve_path(path)

        if not file_path.exists():
            return (
                f"ERROR: File does not exist: {path}"
            )

        return file_path.read_text(
            encoding="utf-8"
        )

    except Exception as e:
        return f"ERROR: {e}"


def create_file(path: str, content: str):

    try:

        file_path = resolve_path(path)

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path.write_text(
            content,
            encoding="utf-8"
        )

        return (
            f"Successfully created {path}"
        )

    except Exception as e:
        return f"ERROR: {e}"


def edit_file(path: str, content: str):

    try:

        file_path = resolve_path(path)

        if not file_path.exists():

            return (
                f"ERROR: File does not exist: {path}"
            )

        file_path.write_text(
            content,
            encoding="utf-8"
        )

        return (
            f"Successfully edited {path}"
        )

    except Exception as e:
        return f"ERROR: {e}"


def replace_text(
    path: str,
    old_text: str,
    new_text: str
):

    try:

        file_path = resolve_path(path)

        if not file_path.exists():

            return (
                f"ERROR: File does not exist: {path}"
            )

        content = file_path.read_text(
            encoding="utf-8"
        )

        if old_text not in content:

            return (
                f"ERROR: Could not find text in {path}"
            )

        updated = content.replace(
            old_text,
            new_text,
            1
        )

        file_path.write_text(
            updated,
            encoding="utf-8"
        )

        return (
            f"Successfully replaced text in {path}"
        )

    except Exception as e:
        return f"ERROR: {e}"


# ============================================================
# COMMANDS
# ============================================================

def run_command(command: str):

    try:

        result = subprocess.run(
            command,
            shell=True,
            cwd=WORKSPACE,
            capture_output=True,
            text=True,
            timeout=30
        )

        return (
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}\n\n"
            f"RETURN CODE: {result.returncode}"
        )

    except subprocess.TimeoutExpired:

        return (
            "ERROR: Command timed out after 30 seconds."
        )

    except Exception as e:

        return f"ERROR: {e}"


# ============================================================
# TOOLS
# ============================================================

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List project files.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_file",
            "description": "Find file by filename.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string"
                    }
                },
                "required": ["filename"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_files",
            "description": "Search files for text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    }
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Create file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": [
                    "path",
                    "content"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": "Edit file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": [
                    "path",
                    "content"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "replace_text",
            "description": "Replace text inside a file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string"
                    },
                    "old_text": {
                        "type": "string"
                    },
                    "new_text": {
                        "type": "string"
                    }
                },
                "required": [
                    "path",
                    "old_text",
                    "new_text"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Run shell command.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string"
                    }
                },
                "required": ["command"]
            }
        }
    }
]


# ============================================================
# EXECUTOR
# ============================================================

def execute_tool(name, arguments):

    if name == "list_files":
        return list_files()

    if name == "find_file":
        return find_file(
            arguments["filename"]
        )

    if name == "search_files":
        return search_files(
            arguments["query"]
        )

    if name == "read_file":
        return read_file(
            arguments["path"]
        )

    if name == "create_file":
        return create_file(
            arguments["path"],
            arguments["content"]
        )

    if name == "edit_file":
        return edit_file(
            arguments["path"],
            arguments["content"]
        )

    if name == "replace_text":
        return replace_text(
            arguments["path"],
            arguments["old_text"],
            arguments["new_text"]
        )

    if name == "run_command":
        return run_command(
            arguments["command"]
        )

    return f"Unknown tool: {name}"