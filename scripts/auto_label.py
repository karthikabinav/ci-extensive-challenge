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

# Example usage for testing:
# test cases from project requirements
if __name__ == "__main__":
    test_issues = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for title in test_issues:
        print(f"{title!r} -> {get_labels_for_issue(title)}")
