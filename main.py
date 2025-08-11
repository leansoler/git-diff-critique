import asyncio
import sys
from pathlib import Path

# Import all the necessary components you identified
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from git_diff_critique_agent.agent import root_agent

# Define constants for repeated string literals to improve maintainability.
APP_NAME = "git_diff_critique_app"
USER_ID = "cli_user"
SESSION_ID = "cli_session"


# The main function must now be asynchronous
async def main() -> None:
    """
    CLI entrypoint for git-diff-critique.
    Reads git diff from stdin and sends it to the agent for review.
    """

    env_path = Path(__file__).parent / "git_diff_critique_agent" / ".env"
    load_dotenv(dotenv_path=env_path)

    diff = sys.stdin.read()
    if not diff.strip():
        print(
            "Error: No git diff input detected. Pipe a git diff to this command.",
            file=sys.stderr,
        )
        sys.exit(1)

    # 1. Set up the session service and runner
    session_service = InMemorySessionService()

    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # 2. Prepare the user's message
    user_content = types.Content(role="user", parts=[types.Part(text=diff)])

    print("--- Git Diff Critique ---")
    print("Agent is analyzing the diff...")

    # 3. Run the agent and stream the response
    final_response = "Agent did not provide a final response."
    # The runner returns an async generator that yields events
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_content,
    ):
        # We look for the final response event from the agent
        if event.is_final_response() and event.content:
            # Ensure that event.content.parts is not empty before accessing its elements.
            # This prevents an IndexError if the parts list is empty.
            if event.content.parts:
                final_response = event.content.parts[0].text
            # Once we have the final response, we can stop listening
            break

    print(final_response)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
