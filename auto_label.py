#!/usr/bin/env python3
"""Automatically label issues by keyword.

Rules:
- label "bug" if the issue title contains "error"
- label "feature" if the issue title contains "add"
"""

def labels_for_title(title: str):
    lower = title.lower()
    labels = []
    if "error" in lower:
        labels.append("bug")
    if "add" in lower:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for title in ["error test", "feature adding requirements", "email feature adding error"]:
        print(title, labels_for_title(title))
