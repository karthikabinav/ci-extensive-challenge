"""Script to automatically label new issues by keyword.

Labels:
- "bug" if the issue contains "error"
- "feature" if the issue contains "add"
"""

def get_labels(text):
    text = text.lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels


def label_issue(issue_title, issue_body=""):
    text = f"{issue_title} {issue_body or ''}"
    labels = get_labels(text)
    return labels


if __name__ == "__main__":
    # Example usage
    examples = ["error test", "feature adding requirements", "email feature adding error"]
    for title in examples:
        print(title, "->", label_issue(title))
