#!/usr/bin/env python3
"""
Auto-label script for GitHub issues
Labels issues based on keywords:
- "bug" if issue contains "error"
- "feature" if issue contains "add"
"""

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
    # Example usage for testing
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for title in test_cases:
        labels = get_labels(title)
        print(f"Title: {title!r} -> Labels: {labels}")

if __name__ == "__main__":
    main()
