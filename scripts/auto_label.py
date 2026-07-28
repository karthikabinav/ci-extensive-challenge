"""
Auto Label Script for GitHub Issues
Labels issues based on keywords:
- "bug" if title or body contains "error"
- "feature" if title or body contains "add"
"""
import os
import sys

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def main():
    # Example usage for GitHub Actions
    # Expects ISSUE_TITLE and ISSUE_BODY env vars, and GITHUB_TOKEN for API calls
    title = os.getenv("ISSUE_TITLE", "")
    body = os.getenv("ISSUE_BODY", "")
    if not title:
        if len(sys.argv) > 1:
            title = sys.argv[1]
        if len(sys.argv) > 2:
            body = sys.argv[2]
    labels = get_labels(title, body)
    print(f"Title: {title}")
    print(f"Labels to apply: {labels}")
    # In GitHub Action, you would call GitHub API here to add labels
    # github.rest.issues.addLabels(...)
    return labels

if __name__ == "__main__":
    main()
