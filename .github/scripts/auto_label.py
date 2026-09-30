#!/usr/bin/env python3
"""Auto label issues by keyword: error -> bug, add -> feature."""
import os
import sys

KEYWORD_LABELS = {"error": "bug", "add": "feature"}

def determine_labels(text):
    text = (text or "").lower()
    return [label for keyword, label in KEYWORD_LABELS.items() if keyword in text]

if __name__ == "__main__":
    title = os.environ.get("ISSUE_TITLE", "")
    body = os.environ.get("ISSUE_BODY", "")
    combined = title + " " + body
    if len(sys.argv) > 1:
        combined = " ".join(sys.argv[1:])
    print(determine_labels(combined))
