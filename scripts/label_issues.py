#!/usr/bin/env python3
"""
Automation script to label GitHub issues by keyword.
- label "bug" if the issue contains "error"
- label "feature" if the issue contains "add"

This script is designed to be used in a GitHub Actions workflow
using github-script or as a standalone Python action.

Usage in workflow:
  on:
    issues:
      types: [opened]
  jobs:
    label:
      runs-on: ubuntu-latest
      permissions:
        issues: write
      steps:
        - uses: actions/github-script@v7
          with:
            script: |
              const title = (context.payload.issue.title || "").toLowerCase();
              const body = (context.payload.issue.body || "").toLowerCase();
              const text = `${title} ${body}`;
              const labels = [];
              if (text.includes("error")) labels.push("bug");
              if (text.includes("add")) labels.push("feature");
              if (labels.length > 0) {
                await github.rest.issues.addLabels({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: context.payload.issue.number,
                  labels
                });
              }
"""
import re

def get_labels_for_issue(title: str, body: str = "") -> list:
    """Determine labels based on keywords in title/body."""
    text = f"{title or ""} {body or ""}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def main():
    # Example usage / local testing
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", "This contains error and add keywords"),
    ]
    for title, body in test_cases:
        labels = get_labels_for_issue(title, body)
        print(f"Title: {title!r} => Labels: {labels}")

    # In GitHub Actions, environment variables provide context
    # This part would be extended to call GitHub API using PyGithub or REST
    # For now, the core labeling logic is above and can be imported.

if __name__ == "__main__":
    main()
