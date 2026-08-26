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

# Example usage for GitHub automation (e.g., in Actions or webhook handler):
# labels = get_labels(issue_title, issue_body)
# then apply labels via GitHub API
