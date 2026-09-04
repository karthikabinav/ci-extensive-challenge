"""
Auto-label script for GitHub issues.
Labels new issues by keyword using safe word-boundary matching:
- label "bug" if the issue contains whole word "error" (case-insensitive)
- label "feature" if it contains whole word "add" (case-insensitive)

This avoids false positives from substring matching (e.g. "adding" should NOT
trigger "add", "terror" should NOT trigger "error").
"""
import re

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}"
    labels = []
    if re.search(r"\berror\b", text, re.IGNORECASE):
        labels.append("bug")
    if re.search(r"\badd\b", text, re.IGNORECASE):
        labels.append("feature")
    return labels

if __name__ == "__main__":
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in tests:
        print(f"{t!r} -> {get_labels(t)}")
