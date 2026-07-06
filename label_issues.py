"""
Automatic issue labeling script.
Labels issues by keyword:
  - "bug" if issue title/body contains "error"
  - "feature" if issue title/body contains "add"
"""
import sys

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for GitHub Actions or local testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in test_cases:
        print(f"Title: {t!r} -> Labels: {get_labels(t)}")

    # If called with arguments, label a single issue
    if len(sys.argv) > 1:
        title = sys.argv[1]
        body = sys.argv[2] if len(sys.argv) > 2 else ""
        print(get_labels(title, body))
