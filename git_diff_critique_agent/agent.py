from google.adk.agents import Agent

from git_diff_critique_agent.instructions import AGENT_INSTRUCTIONS

# Placeholder for your git diff critique tool


def critique_git_diff(diff: str) -> dict:
    """Analyzes a git diff and provides senior developer recommendations.

    Args:
        diff (str): The git diff to analyze.

    Returns:
        dict: status and recommendations or error message.
    """
    # TODO: Implement actual critique logic
    return {
        "status": "success",
        "recommendations": [
            "Use descriptive commit messages.",
            "Ensure code follows project style guidelines.",
            "Add or update tests for new functionality.",
        ],
    }


root_agent = Agent(
    name="git_diff_critique_agent",
    model="gemini-2.0-flash",
    description="Agent to review git diffs and provide senior developer recommendations.",
    instruction=AGENT_INSTRUCTIONS,
    tools=[critique_git_diff],
)
