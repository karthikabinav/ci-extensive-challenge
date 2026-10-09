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
    import sys
    title = sys.argv[1] if len(sys.argv) > 1 else ""
    body = sys.argv[2] if len(sys.argv) > 2 else ""
    print(get_labels(title, body))
