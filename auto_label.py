"""
Auto-label new issues by keyword:
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for GitHub automation:
# This function can be called in a GitHub Action or webhook handler
# to automatically apply labels to new issues.

if __name__ == "__main__":
    # Test cases from project requirements
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for title in test_cases:
        print(f"{title!r} -> {get_labels(title)}")
