"""Automatically label issues by keyword: error -> bug, add -> feature."""

def labels_for_issue(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for title in ["error test", "feature adding requirements", "email feature adding error"]:
        print(title, labels_for_issue(title))
