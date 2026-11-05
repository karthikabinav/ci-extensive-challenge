"""
Auto-label issues by keyword:
- label "bug" if issue title/body contains "error"
- label "feature" if contains "add"
"""

def get_labels(title: str, body: str = ""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for GitHub automation (e.g., in Actions or webhook):
# labels = get_labels(issue_title, issue_body)
# then apply labels via GitHub API

if __name__ == "__main__":
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in tests:
        print(f"{t!r} -> {get_labels(t)}")
