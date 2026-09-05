# Auto-label script for issues
# Labels: "bug" if issue contains whole word "error", "feature" if contains whole word "add"
# Uses word boundaries to avoid false positives (e.g., "adding" should not trigger "add")

import re

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if re.search(r"\berror\b", text):
        labels.append("bug")
    if re.search(r"\badd\b", text):
        labels.append("feature")
    return labels

def main():
    # Example usage for testing
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in test_cases:
        print(f"{t!r} -> {get_labels(t)}")

if __name__ == "__main__":
    main()
