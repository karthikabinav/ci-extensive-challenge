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

# Example usage with GitHub API (requires PyGithub or gh cli):
# for issue in repo.get_issues(state="open"):
#     labels = get_labels_for_issue(issue.title, issue.body or "")
#     if labels:
#         issue.add_to_labels(*labels)

if __name__ == "__main__":
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in tests:
        print(f"{t!r} -> {get_labels_for_issue(t)}")
