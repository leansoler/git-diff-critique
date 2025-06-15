import pytest

from git_diff_critique_agent import agent


def test_critique_git_diff_success():
    diff = "diff --git a/foo.py b/foo.py\nindex 123..456 100644\n--- a/foo.py\n+++ b/foo.py\n@@ ..."
    result = agent.critique_git_diff(diff)
    assert result["status"] == "success"
    assert isinstance(result["recommendations"], list)
    assert len(result["recommendations"]) > 0

def test_critique_git_diff_empty():
    result = agent.critique_git_diff("")
    assert result["status"] == "success" or result["status"] == "error"

# Add more tests as the critique logic evolves
