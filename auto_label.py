#!/usr/bin/env python3
"""Automatically label GitHub issues by keyword.
Rules: label "bug" if the issue contains "error", and "feature" if it contains "add" (case-insensitive).
"""

def determine_labels(text):
    t = text.lower()
    labels = []
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage: determine_labels(issue_title + " " + issue_body)
    pass
