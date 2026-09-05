# Auto-label issues by keyword
# label "bug" if title contains "error", "feature" if contains "add" (case-insensitive)

def get_labels(title: str):
    t = title.lower()
    labels = []
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

# Example usage:
# labels = get_labels(issue_title)
# then apply via GitHub API: update_issue with labels
