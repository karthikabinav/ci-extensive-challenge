# Auto-label script for CI Extensive Challenge
# This script automatically labels new issues by keyword
# - label "bug" if the issue contains "error"
# - label "feature" if the issue contains "add"

def get_labels_for_issue(title, body=""):
    """Determine labels based on keyword matching"""
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Test cases
test_issues = [
    "error test",
    "feature adding requirements",
    "email feature adding error"
]

for issue in test_issues:
    print(f"Issue: {issue} -> Labels: {get_labels_for_issue(issue)}")
