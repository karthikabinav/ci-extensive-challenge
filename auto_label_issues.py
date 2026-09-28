"""Automatically label new issues by keyword.

Label bug if the issue title/body contains error.
Label feature if the issue title/body contains add.
"""

def labels_for_issue(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels
