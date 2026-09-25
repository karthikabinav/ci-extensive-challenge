"""Automatically label new issues by keyword.

Label bug if the issue contains error, and feature if it contains add.
Used by the Issue Labeler GitHub Actions workflow.
"""

def labels_for_issue(text):
    text = (text or "").lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels
