# Auto-label script for GitHub issues
# Labels new issues by keyword: "bug" if contains "error", "feature" if contains "add"

def get_labels(title: str, body: str = ""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage with GitHub API (pseudo):
# for issue in new_issues:
#     labels = get_labels(issue.title, issue.body)
#     if labels:
#         update_issue(issue.number, labels=labels)
