#!/usr/bin/env python3
"""
Auto-label GitHub issues by keyword
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
"""
import os
import re
import sys

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage for testing
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", "")
    ]
    for title, body in test_cases:
        print(title, "->", get_labels(title, body))
