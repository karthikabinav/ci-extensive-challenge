"""
Auto-label issues by keyword.
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
"""

def get_labels(title, body=""):
    text = (title + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage with MCP tools:
# For each new issue, call get_labels(issue_title, issue_body)
# then use update_issue with the returned labels to apply them.
