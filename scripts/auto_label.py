"""
Auto-label issues by keyword.
- label "bug" if issue title/body contains "error"
- label "feature" if issue title/body contains "add"
Case-insensitive matching.
"""

def get_labels_for_issue(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage for testing
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in test_cases:
        print(f"{title!r} -> {get_labels_for_issue(title, body)}")
