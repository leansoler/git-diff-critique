import sys

from git_diff_critique_agent.agent import critique_git_diff


def main() -> None:
    """
    CLI entrypoint for git-diff-critique.
    Reads git diff from stdin and prints recommendations.
    """
    diff = sys.stdin.read()
    if not diff.strip():
        print(
            "Error: No git diff input detected. "
            "Pipe a git diff to this command.",
            file=sys.stderr,
        )
        sys.exit(1)
    result = critique_git_diff(diff)
    if result.get("status") == "success":
        print("Recommendations:")
        for rec in result.get("recommendations", []):
            print(f"- {rec}")
    else:
        print(
            f"Error: {result.get('error_message', 'Unknown error')}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
