from google.adk.agents import LlmAgent

from git_diff_critique_agent.instructions import AGENT_INSTRUCTIONS
from git_diff_critique_agent.schemas import CritiqueInput, CritiqueOutput

root_agent = LlmAgent(
    name="git_diff_critique_agent",
    model="gemini-2.0-flash-001",  # Using a fast and capable model
    description="Agent to review git diffs and provide senior developer recommendations.",
    instruction=AGENT_INSTRUCTIONS,
    # By defining input and output schemas, we create a clear, enforceable
    # contract for the agent. This is a best practice that improves
    # reliability and makes the agent easier to integrate and test.
    input_schema=CritiqueInput,
    output_schema=CritiqueOutput,
)
