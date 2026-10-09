# Auto-label issues by keyword
# Rules: "error" -> "bug", "add" -> "feature"

def labels_for_issue(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    print(labels_for_issue("error test"))  # ["bug"]
    print(labels_for_issue("feature adding requirements"))  # ["feature"]
    print(labels_for_issue("email feature adding error"))  # ["bug", "feature"]
