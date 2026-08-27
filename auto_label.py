"""
Auto-label new issues by keyword:
- label "bug" if issue title/body contains "error"
- label "feature" if issue title/body contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage:
# labels = get_labels(issue_title, issue_body)
# then apply labels via GitHub API
