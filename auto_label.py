#!/usr/bin/env python3
"""
Auto-label script for GitHub issues
Labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if the issue contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for testing
if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for title in test_cases:
        print(f"Title: \"{title}\" -> Labels: {get_labels(title)}")
