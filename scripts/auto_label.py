# Auto-label script for issues
# Labels new issues by keyword:
# - label "bug" if issue contains "error" (case-insensitive, substring)
# - label "feature" if issue contains "add" (case-insensitive, substring)

def get_labels(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for t in ["error test", "feature adding requirements", "email feature adding error"]:
        print(t, get_labels(t))
