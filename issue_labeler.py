#!/usr/bin/env python3
"""
Auto-label script for GitHub issues
Labels issues based on keyword matching:
- Adds bug label if issue contains error
- Adds feature label if issue contains add
"""

import sys

def get_labels(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def main():
    if len(sys.argv) < 2:
        print("Usage: issue_labeler.py <title> [body]")
        sys.exit(1)
    title = sys.argv[1]
    body = sys.argv[2] if len(sys.argv) > 2 else ""
    labels = get_labels(title, body)
    if labels:
        print("Labels to apply: " + ", ".join(labels))
    else:
        print("No matching labels found")

if __name__ == "__main__":
    main()
