# Coding Agent

An autonomous coding agent built in Python using NVIDIA Nemotron and tool calling.

The agent can:

- Read files
- Create files
- Edit files
- Search project code
- Run terminal commands
- Analyze project structure
- Make code changes autonomously

The goal of this project is to provide a lightweight AI-powered coding assistant that operates directly inside a local workspace.

---

# Features

## File Operations

The agent can:

- List project files
- Read file contents
- Create new files
- Edit existing files
- Replace text inside files

Example:

> Create a file named hello.py that prints Hello World

The agent will create the file automatically.

---

## Code Search

The agent can locate:

- Classes
- Functions
- Variables
- Imports
- Text patterns

Example:

> Where is the Agent class defined?

The agent searches the project and returns the exact location.

---

## Command Execution

The agent can execute terminal commands inside the current workspace.

Example:

> Run python calculator.py

The agent executes the command and returns the output.

---

## Project Understanding

The agent can inspect project structure and reason about code relationships.

Example:

> Explain what the Agent class does.

The agent reads the relevant files and provides an explanation.

---

# Project Structure

```text
coding_agent/
│
├── .gitignore
├── .env
├── README.md
├── requirements.txt
├── pyproject.toml
│
├── coding_agent/
│   ├── __init__.py
│   ├── agent.py
│   ├── model.py
│   ├── prompt.py
│   └── tools.py
│
└── main.py
```

---

# How It Works

The application consists of four main components.

## 1. model.py

Responsible for:

- Loading environment variables
- Configuring the NVIDIA API client
- Defining the active model

Example:

```python
MODEL = "nvidia/nemotron-3-ultra-550b-a55b"
```

---

## 2. prompt.py

Contains the system prompt used to guide agent behavior.

The prompt teaches the model:

- When to inspect files
- When to execute tools
- How to modify code safely
- How to avoid unnecessary tool calls

---

## 3. tools.py

Provides the agent's capabilities.

Current tools include:

### list_files

Lists files inside the workspace.

### read_file

Reads file contents.

### create_file

Creates new files.

### edit_file

Replaces file contents.

### replace_text

Performs targeted edits.

### search_files

Searches code and text.

### find_file

Finds files by name.

### run_command

Executes terminal commands.

---

## 4. agent.py

The core reasoning loop.

Workflow:

1. User sends request
2. Model decides which tool to use
3. Tool executes
4. Result is returned to the model
5. Model decides next action
6. Final answer is returned

This loop continues until the task is complete.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/coding_agent.git

cd coding_agent
```

---

## Create Virtual Environment

Windows:

```powershell
python -m venv .venv

.\.venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# NVIDIA API Setup

Create a file named:

```text
.env
```

Add:

```env
api_key_nemo=YOUR_NVIDIA_API_KEY
```

Example:

```env
api_key_nemo=nvapi-xxxxxxxxxxxxxxxxxxxxxxxx
```

Never commit this file to GitHub.

---

# Running the Agent

Start the application:

```bash
python main.py
```

Example output:

```text
================================
       CODING AGENT
================================

Workspace: C:\Projects\coding_agent

Type your request.
Type 'exit' to quit.
```

---

# Example Commands

## Create File

```text
Create hello.py that prints Hello World
```

---

## Read Code

```text
Read calculator.py and explain it
```

---

## Find Function

```text
Where is calculate_total defined?
```

---

## Run Program

```text
Run python calculator.py
```

---

## Modify Existing Code

```text
Add a subtract(a, b) function to calculator.py
```

---

## Search Project

```text
Find all references to Agent
```

---

# Safety Features

The agent is restricted to the current workspace.

It cannot:

- Access files outside the workspace
- Modify arbitrary system files
- Escape project boundaries

Path traversal attempts such as:

```text
../../secret.txt
```

are blocked.

---

# Configuration

The active model is defined in:

```python
coding_agent/model.py
```

Example:

```python
MODEL = "nvidia/nemotron-3-ultra-550b-a55b"
```

You can switch models by changing this value.

---

# Requirements

Python:

```text
Python 3.10+
```

Dependencies:

```text
openai
python-dotenv
```

---

# Future Improvements

Potential additions:

- Multi-file planning
- Git integration
- File deletion
- Directory creation
- Code diff previews
- Automatic test generation
- Unit test execution
- Memory and task history
- Streaming responses
- RAG-based project indexing

---

# Known Limitations

- Tool calls depend on model quality.
- Large projects may require multiple search steps.
- Command execution timeout is limited.
- The agent does not yet support parallel tool execution.

---

# License

MIT License

Feel free to modify, extend, and use this project for personal or commercial purposes.

---

# Author

Built by Arav as part of an AI Agent engineering project using NVIDIA Nemotron and Python.