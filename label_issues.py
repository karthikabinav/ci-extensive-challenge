"""
Auto-label issues by keyword.
- label "bug" if title/body contains "error" (case-insensitive substring)
- label "feature" if title/body contains "add" (case-insensitive substring)
This script is intended for demonstration / CI use.
"""

def get_labels_for_issue(title: str, body: str = "") -> list[str]:
    text = f"{title or ""} {body or ""}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels


if __name__ == "__main__":
    # Example usage for testing
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in tests:
        print(f"{t!r} -> {get_labels_for_issue(t)}")
