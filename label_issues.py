"""
Auto-label script for GitHub issues.
Labels new issues by keyword:
- label "bug" if issue title/body contains "error"
- label "feature" if issue title/body contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    """Return list of labels based on keywords in title/body."""
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels


if __name__ == "__main__":
    # Example usage / test cases
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for title in test_cases:
        print(f"{title!r} -> {get_labels(title)}")
