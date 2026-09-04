"""
Auto-label script for GitHub issues.
Labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if it contains "add"
Case-insensitive substring match.
"""
def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in test_cases:
        print(f"{t!r} -> {get_labels(t)}")
