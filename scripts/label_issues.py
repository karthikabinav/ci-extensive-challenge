"""
label_issues.py

Helper script that replicates the auto-labeling rules of
.github/workflows/auto_label.yml so issues can be (re)labeled on demand.

Rules:
  - label "bug"     if the issue title/body contains "error"
  - label "feature" if the issue title/body contains "add"
pip install PyGithub to run.
"""

import os
import sys
from github import Github

REPO = "karthikabinav/ci-extensive-challenge"
RULES = {"error": "bug", "add": "feature"}


def labels_for(text):
    text = text.lower()
    return [label for kw, label in RULES.items() if kw in text]


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("Set GITHUB_TOKEN environment variable")
    gh = Github(token)
    repo = gh.get_repo(REPO)
    target_numbers = [int(n) for n in sys.argv[1:]] or [
        issue.number for issue in repo.get_issues(state="open")
    ]
    for number in target_numbers:
        issue = repo.get_issue(int(number))
        combined = f"{issue.title} {issue.body or ""}"
        labels = labels_for(combined)
        print(f"#{number} ({issue.title!r}) -> {labels or "(no match)"}")
        if labels:
            issue.set_labels(*labels)


if __name__ == "__main__":
    main()
