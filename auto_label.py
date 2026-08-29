"""
Auto-label issues by keyword.
- label "bug" if issue contains word "error"
- label "feature" if issue contains word "add"
Uses case-insensitive whole-word matching with regex word boundaries
to avoid false positives (e.g., "adding" should NOT trigger "add").
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

# Example usage with MCP tools:
# For each new issue, call get_labels(issue_title, issue_body)
# then update_issue with returned labels.

if __name__ == "__main__":
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in test_cases:
        print(f"{title!r} -> {get_labels(title, body)}")
