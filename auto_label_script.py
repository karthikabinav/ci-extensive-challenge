import re

def label_issue(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage:
# label_issue("error test") => ["bug"]
# label_issue("feature adding requirements") => ["feature"]
# label_issue("email feature adding error") => ["bug", "feature"]
