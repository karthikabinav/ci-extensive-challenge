#!/usr/bin/env python3
"""
Auto-label script for CI Extensive Challenge
Labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if it contains "add"
"""
import os
import sys

def get_labels(title, body=""):
    text = f"{title} {body or ""}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    title = os.environ.get("ISSUE_TITLE", "")
    body = os.environ.get("ISSUE_BODY", "")
    # Also support GitHub event payload
    print(get_labels(title, body))
