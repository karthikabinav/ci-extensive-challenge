#!/usr/bin/env python3
"""Automatically label issues by keyword: bug if contains error, feature if contains add."""

def get_labels(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    examples = ["error test", "feature adding requirements", "email feature adding error"]
    for title in examples:
        print(title, "->", get_labels(title))
