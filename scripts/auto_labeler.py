#!/usr/bin/env python3
"""
Auto Label Script for GitHub Issues
Labels "bug" if issue contains "error",
Labels "feature" if issue contains "add"
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

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else ""
    body = sys.argv[2] if len(sys.argv) > 2 else ""
    print(",".join(get_labels(title, body)))
