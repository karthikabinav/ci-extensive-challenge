# Auto-label issues by keyword
# Labels "bug" if issue contains "error", and "feature" if it contains "add"

import re

def get_labels_for_issue(title: str, body: str = ""):
    text = f"{title}\n{body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for GitHub Actions (using PyGithub or github-script equivalent)
# This function can be integrated into a GitHub Action workflow:
# - On issue opened/edited event
# - Determine labels via get_labels_for_issue()
# - Apply labels via GitHub API

if __name__ == "__main__":
    # Simple local test harness
    tests = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in tests:
        print(f"{title!r} -> {get_labels_for_issue(title, body)}")
