"""
Auto-label issues by keyword.
- label "bug" if issue title/body contains "error"
- label "feature" if issue title/body contains "add"
Matching is case-insensitive substring search.
"""

def get_labels_for_issue(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

def label_issue(owner, repo, issue_number, title, body=""):
    # Example placeholder for GitHub API integration
    # In workflow context, this would call GitHub API to add labels
    labels = get_labels_for_issue(title, body)
    print(f"Issue #{issue_number} [{title}] -> labels: {labels}")
    return labels

if __name__ == "__main__":
    # Simple manual test
    tests = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for t, b in tests:
        print(t, "=>", get_labels_for_issue(t, b))
