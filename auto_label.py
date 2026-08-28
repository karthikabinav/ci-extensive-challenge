"""
Auto-label script for GitHub issues.
Labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if it contains "add"
Case-insensitive substring matching on title and body.
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels


def label_issue(owner, repo, issue_number, title, body=""):
    # Example placeholder for GitHub API call
    # In production, this would call the GitHub API to add labels
    labels = get_labels(title, body)
    print(f"Issue #{issue_number} ({title!r}) -> labels: {labels}")
    return labels


if __name__ == "__main__":
    # Simple test harness
    tests = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in tests:
        print(f"{title!r} => {get_labels(title, body)}")
