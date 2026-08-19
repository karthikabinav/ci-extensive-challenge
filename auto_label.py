import os
import sys

def get_labels(title, body=""):
    text = (title + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def label_issue(owner, repo, issue_number, labels):
    # This function would use GitHub API to add labels
    # For automation, used in GitHub Actions workflow
    print(f"Labeling issue #{issue_number} in {owner}/{repo} with labels: {labels}")
    return labels

if __name__ == "__main__":
    # Example usage for testing
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", "")
    ]
    for title, body in test_cases:
        print(f"Title: {title} => Labels: {get_labels(title, body)}")
