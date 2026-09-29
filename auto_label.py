#!/usr/bin/env python3
"""Automatically label GitHub issues by keyword.
Rules:
- if the issue contains "error" -> label "bug"
- if the issue contains "add" -> label "feature"
Matching is case-insensitive and multiple labels may apply.
"""

def determine_labels(text):
    text_lower = text.lower()
    labels = []
    if "error" in text_lower:
        labels.append("bug")
    if "add" in text_lower:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        print(arg, "->", determine_labels(arg))
