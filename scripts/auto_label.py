"""
Safe auto-label script for issues.
Labels:
  - "bug" if issue title/body contains whole word "error" (case-insensitive)
  - "feature" if contains whole word "add" (case-insensitive)
Uses word boundaries to avoid false positives like "adding" matching "add".
"""
import re

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}"
    labels = []
    if re.search(r"\berror\b", text, flags=re.IGNORECASE):
        labels.append("bug")
    if re.search(r"\badd\b", text, flags=re.IGNORECASE):
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
