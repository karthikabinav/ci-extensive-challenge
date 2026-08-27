"""
Auto-label script for GitHub issues.
Labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if it contains "add"
"""

def get_labels_for_issue(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage:
# labels = get_labels_for_issue(issue_title, issue_body)
# then apply via GitHub API: update_issue with labels

if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in test_cases:
        print(f"{t!r} -> {get_labels_for_issue(t)}")
