# Auto-label issues by keyword:
# label "bug" if issue contains "error", and "feature" if it contains "add"

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for title in ["error test", "feature adding requirements", "email feature adding error"]:
        print(title, get_labels(title))
