"""
Auto-label new issues by keyword.
- label "bug" if the issue title/body contains "error"
- label "feature" if the issue title/body contains "add"
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
    # In real automation, this would call update_issue with computed labels
    labels = get_labels_for_issue(title, body)
    print(f"Issue #{issue_number} [{title}] -> labels: {labels}")
    return labels


if __name__ == "__main__":
    # Simple test harness
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in test_cases:
        print(f"{title!r} => {get_labels_for_issue(title, body)}")
