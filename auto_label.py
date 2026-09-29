#!/usr/bin/env python3
"""
Automatically label GitHub issues based on keywords.
- If issue contains "error" -> label "bug"
- If issue contains "add" -> label "feature"
Matching is case-insensitive and substring-based, so "adding"
contains "add". An issue can receive both labels.
"""

def determine_labels(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    import sys
    print(determine_labels(sys.argv[1] if len(sys.argv) > 1 else "", sys.argv[2] if len(sys.argv) > 2 else ""))
