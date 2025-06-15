# Git Diff Critique Copilot Instructions

## Project Overview
This repository implements an agent using Google ADK that receives a git diff and provides code review recommendations as a Senior Developer. Linting is enforced with Ruff.

## Coding Guidelines
- Use [Google ADK](https://google.github.io/adk-docs/) for agent and tool development.
- All linting must pass with [Ruff](https://docs.astral.sh/ruff/). Follow PEP8 and fix all warnings/errors.
- Write clear, maintainable, and well-documented Python code.
- Use type hints for all function signatures.
- Prefer functional decomposition: keep functions small and focused.
- Add or update tests for new features or bug fixes (if/when a test suite is present).

## Agent Functionality
- The agent receives a git diff as input and returns actionable, senior-level code review feedback.
- Recommendations should focus on code quality, best practices, test coverage, and maintainability.
- If the diff is invalid or incomplete, return a helpful error message.

## Best Practices
- Use descriptive commit messages and comments.
- Ensure code changes follow project style and conventions.
- Suggest improvements, not just point out issues.
- If using external libraries, prefer those already listed in `pyproject.toml`.

## Tooling
- Use `uv` for dependency management (e.g., `uv add <package>`).
- Run `ruff check .` before submitting code.
- Use a virtual environment (see README for setup).

## Example Prompts for the Agent
- "Review this git diff and provide recommendations."
- "What improvements would you suggest for this code change?"

## Additional Notes
- Sensitive credentials (API keys, etc.) must not be committed.
- Update this file if project conventions change.
