#!/usr/bin/env python3
"""
Automation script to label GitHub issues by keyword.
- label "bug" if the issue contains "error"
- label "feature" if the issue contains "add"
"""

def get_labels_for_issue(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def main():
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", "This contains error and add keywords"),
    ]
    for title, body in test_cases:
        labels = get_labels_for_issue(title, body)
        print(f"Title: {title!r} => Labels: {labels}")

if __name__ == "__main__":
    main()
