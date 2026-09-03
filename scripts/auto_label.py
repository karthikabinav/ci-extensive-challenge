"""
Secure auto-label script for GitHub issues.

Rules:
- label "bug" if issue title/body contains whole word "error" (case-insensitive, regex \\berror\\b)
- label "feature" if issue title/body contains whole word "add" (regex \\badd\\b)

Uses word boundaries to avoid false positives from naive substring matching
(e.g., "adding" should NOT trigger "add", "terror" should NOT trigger "error").
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

def main():
    # Example usage for testing
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for title in test_cases:
        print(f"{title!r} => {get_labels(title)}")

if __name__ == "__main__":
    main()
