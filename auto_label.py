# Auto-label script for GitHub issues
# Logic per requirements:
# - label "bug" if issue title (or body) contains "error" (substring, case-insensitive)
# - label "feature" if contains "add" (substring, case-insensitive)

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage:
# labels = get_labels(issue_title)
# then apply via GitHub API update_issue
