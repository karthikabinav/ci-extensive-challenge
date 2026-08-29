"""
Auto-label issues by keyword.
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
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
