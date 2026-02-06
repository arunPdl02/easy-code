# Easy Code — Sandboxed LLM Coding Agent

## Overview
**Easy Code** is a Python-based command-line coding agent that uses the **Gemini API** with **strictly controlled function access** to safely inspect, modify, and execute code inside a bounded project directory.

The core focus of this project is **system safety, constrained execution, and deterministic tooling**, not unrestricted LLM behavior. The agent can only interact with the filesystem and runtime through explicitly defined functions, preventing access outside the permitted working directory.

---

## Key Concepts Demonstrated
- LLM tool/function calling with explicit schemas
- Sandboxed filesystem access using path normalization and validation
- Secure OS-level constraints for file inspection and execution
- Iterative agent loop with bounded model calls
- Defensive programming and error handling
- Test-driven validation of restricted functions

---

## Architecture Overview
```
easy-code/
├── main.py # Main agent loop and Gemini interaction
├── call_function.py # Function routing and execution control
├── functions/ # Allowed tool functions (sandboxed)
│ ├── get_file_content.py
│ ├── get_files_info.py
│ ├── run_python_file.py
│ └── write_file.py
├── calculator/ # Isolated test application (sandbox target)
│ └── ...
├── test_get_file_content.py # Function-level tests
├── test_get_files_info.py # Function-level tests
├── test_run_python.py # Function-level tests
├── test_write_file.py # Function-level tests
├── pyproject.toml
├── prompts.py
├── config.py
```

## How the Agent Works

1. The user provides a prompt via CLI.
2. The agent sends the prompt to Gemini with:
   - A system prompt
   - A **fixed set of allowed tools**
3. The model may:
   - Respond directly **or**
   - Request a function call
4. Function calls are:
   - Validated
   - Executed locally
   - Forced to operate **only inside the sandbox directory**
5. Results are returned to the model and appended to the conversation.
6. The loop continues until a final response is produced or a maximum iteration limit is reached.

The agent is intentionally **not autonomous**. Every capability is explicit, auditable, and constrained.

---

## Security & Sandboxing Design

### Filesystem Isolation
All file operations:
- Resolve absolute paths
- Normalize user-provided paths
- Reject traversal outside the working directory

Example safeguards:
- Prevents `../` directory escape
- Blocks access to system files
- Limits file read size using a max character cap

### Controlled Execution
- Only Python files inside the sandbox directory can be executed
- Execution is mediated through a single allowed function
- No shell access or arbitrary OS commands

---

## Available Functions (Tools)

The LLM can only call the following functions:

| Function | Purpose |
|--------|--------|
| `get_files_info` | List files and directories |
| `get_file_content` | Read file contents with safety checks |
| `write_file` | Create or modify files |
| `run_python_file` | Execute Python scripts in sandbox |

Each function has:
- A strict input schema
- A single responsibility
- Defensive error handling

---

## Testing Strategy

Each tool function is tested independently outside the agent loop.

Example:
- Valid file reads
- Non-existent files
- Attempts to access system paths
- Truncated content handling

This ensures:
- Deterministic behavior
- Predictable failure modes
- Safe integration with LLM calls

---

## Running the Agent

### Requirements
- Python 3.10+
- Gemini API key
- Linux or macOS environment recommended

### Install Dependencies
bash
```
pip install .
```

Set API Key
- Get a free Gemini API key from [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key)
- Create a .env file inside the main directory
- Store your api key as follows, replace your_api_key_here with your actual api key
```
GEMINI_API_KEY='your_api_key_here'
```

Run
```
python main.py "Explain the calculator project"
```

Optional verbose mode:
```
python main.py "Explain the calculator project" --verbose
```

---

### Design Philosophy
- This project intentionally prioritizes:
- Correctness over cleverness
- Safety over autonomy
- Explicit control over implicit behavior

The goal is to explore how LLMs can be integrated into real systems without surrendering control, mirroring constraints found in production, embedded, and safety-critical environments.

---

### Notes
- This project is not a general-purpose coding assistant.
- The LLM cannot access the network, system files, or arbitrary directories.
- Every capability is deliberately scoped and testable.

---

### Future Extensions
- Per-function permission policies
- Read-only vs write-enabled modes
- Execution timeouts and resource limits
- Structured logging for function calls



