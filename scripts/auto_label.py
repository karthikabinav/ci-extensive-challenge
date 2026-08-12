#!/usr/bin/env python3
"""
Auto-label script for GitHub issues
Labels "bug" if issue contains "error"
Labels "feature" if issue contains "add"
"""

import sys
import json

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for t in test_cases:
        print(f"Title: {t} -> Labels: {get_labels(t)}")
