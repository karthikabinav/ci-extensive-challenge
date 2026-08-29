# Auto-label script
# Labels new issues by keyword: "bug" if contains "error", "feature" if contains "add"

def get_labels(title: str, body: str = ""):
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
