#!/usr/bin/env python3
"""Automatically label issues by keyword: bug if contains error, feature if contains add."""

def labels_for_issue(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(t, labels_for_issue(t))
