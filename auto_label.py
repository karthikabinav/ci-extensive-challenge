"""
Auto-label script for GitHub issues.
Labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if it contains "add"
Matching is case-insensitive and checks title and body.
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
    """Example helper that would call GitHub API to apply labels."""
    labels = get_labels(title, body)
    print(f"Issue #{issue_number} ({title!r}) -> labels: {labels}")
    return labels


if __name__ == "__main__":
    # Simple self-test
    tests = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for t, b in tests:
        print(f"{t!r} => {get_labels(t, b)}")
