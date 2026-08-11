#!/usr/bin/env python3
"""
Auto-label script: labels issues based on keywords
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
"""
import os
import sys

try:
    from github import Github
    HAS_PYGH = True
except ImportError:
    HAS_PYGH = False

KEYWORD_LABELS = {
    "error": "bug",
    "add": "feature",
}

def labels_for_issue(title: str, body: str):
    text = f"{title or ""} {body or ""}".lower()
    labels = []
    for keyword, label in KEYWORD_LABELS.items():
        if keyword.lower() in text:
            labels.append(label)
    return labels

def main():
    # Example usage with GitHub API if GITHUB_TOKEN and ISSUE_NUMBER are set
    # This script is intended to be used in GitHub Actions workflow.
    # Workflow example is in .github/workflows/auto-label-extensive.yml
    title = os.environ.get("ISSUE_TITLE", "")
    body = os.environ.get("ISSUE_BODY", "")
    if title or body:
        print(f"Labels: {labels_for_issue(title, body)}")
    else:
        # Demo/test mode
        test_cases = [
            ("error test", ""),
            ("feature adding requirements", ""),
            ("email feature adding error", ""),
        ]
        for t, b in test_cases:
            print(f"Title: {t!r} -> Labels: {labels_for_issue(t,b)}")

if __name__ == "__main__":
    main()
