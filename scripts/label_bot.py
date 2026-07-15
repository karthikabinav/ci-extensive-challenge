#!/usr/bin/env python3
"""
Auto Label Bot for CI Extensive Challenge
Labels issues based on keywords:
- "bug" if title/body contains "error"
- "feature" if title/body contains "add"
"""

def get_labels(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for t in test_cases:
        print(f"Title: {t} -> Labels: {get_labels(t)}")
