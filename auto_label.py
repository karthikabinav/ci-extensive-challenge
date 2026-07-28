"""
Auto-label GitHub issues by keyword.
- label "bug" if the issue contains "error"
- label "feature" if it contains "add"
"""

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example GitHub Actions integration (using github-script style logic)
# This function would be called by the workflow when a new issue is opened.
# In real automation, you would use:
#   github.rest.issues.addLabels({
#       owner: context.repo.owner,
#       repo: context.repo.repo,
#       issue_number: context.issue.number,
#       labels: get_labels(issue.title, issue.body)
#   })

if __name__ == "__main__":
    # Simple test with the three sample issues
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for title in test_cases:
        print(f"{title}: {get_labels(title)}")
