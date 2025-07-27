# git-diff-critique

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Ruff Lint](https://img.shields.io/badge/linting-ruff-%2332a852)](https://docs.astral.sh/ruff/)

This project provides an agent that reviews git diffs and offers actionable, senior-level code review recommendations. It uses Google ADK for agent development and Ruff for linting.

## Requirements
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management
- Google API key (see `.env` setup)

## Setup
1. **Create and activate a virtual environment:**
   ```sh
   uv venv
   source .venv/bin/activate
   ```
2. **Install dependencies:**
   ```sh
   uv add google-adk ruff
   ```
3. **Configure your API key:**
   - Edit `git_diff_critique_agent/.env` and set your Google API key and region.

## Usage

### As a CLI tool
You can pipe a git diff directly to the agent for review:

```sh
git diff | python main.py
```

If no input is detected, an error message will be shown.

### As a Web Agent (ADK UI)
You can also run the agent in a web UI for interactive use:

```sh
adk web
```
Then open the provided URL in your browser and select the agent.

## Linting
Run Ruff to check code style:
```sh
uv run ruff check .
```

## Testing
Run the test suite with:
```sh
uv run pytest
```

This will discover and run all tests in the `tests/` directory. Ensure your virtual environment is activated and dependencies are installed.

## Contributing
- Follow the coding and review guidelines in `.gemini/context.md`.
- Use `uv` for all dependency management.
- Ensure all code passes Ruff linting before submitting.

---
For more details, see the inline documentation and Copilot instructions.
