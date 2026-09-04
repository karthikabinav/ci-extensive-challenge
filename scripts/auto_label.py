"""
Auto-label issues by keyword with robust word-boundary matching.

Rules:
- label "bug" if issue title/body contains whole word "error" (case-insensitive)
- label "feature" if issue title/body contains whole word "add" (case-insensitive)

Uses regex word boundaries (\\b) to avoid false positives:
- "adding" should NOT trigger "add"
- "errors" should NOT trigger "error" (plural)
- "terror" should NOT trigger "error"
"""
import re

def get_labels(title: str, body: str = "") -> list[str]:
    text = f"{title} {body}"
    labels = []
    if re.search(r"\berror\b", text, re.IGNORECASE):
        labels.append("bug")
    if re.search(r"\badd\b", text, re.IGNORECASE):
        labels.append("feature")
    return labels

def test_examples():
    cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in cases:
        print(f"{title!r} -> {get_labels(title, body)}")

if __name__ == "__main__":
    test_examples()
