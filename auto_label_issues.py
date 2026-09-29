"""Auto-label GitHub issues by keyword.

Rules:
    - label `bug`     when issue text contains "error"
    - label `feature` when issue text contains "add"
"""

import os
import sys

try:
    from github import Github
except ImportError:
    Github = None

KEYWORD_LABELS = [("error", "bug"), ("add", "feature")]


def compute_labels(title, body=""):
    """Return labels for an issue based on the keyword rules."""
    text = f"{title} {body}".lower()
    return sorted({label for kw, label in KEYWORD_LABELS if kw in text})


def label_repo_issues(repo_full_name, token):
    """Apply keyword-based labels to all open issues in a repo."""
    if Github is None:
        print("PyGithub is required for live mode", file=sys.stderr)
        sys.exit(1)
    gh = Github(token)
    repo = gh.get_repo(repo_full_name)
    for issue in repo.get_issues(state="open"):
        labels = compute_labels(issue.title, issue.body or "")
        if labels:
            issue.set_labels(*labels)
            print(f"#{issue.number} {issue.title!r} -> {labels}")


if __name__ == "__main__":
    for title in ["error test", "feature adding requirements", "email feature adding error"]:
        print(f"{title!r} -> {compute_labels(title)}")
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        label_repo_issues(os.environ.get("GITHUB_REPOSITORY", "ci-extensive-challenge"), token)
