# Script to automatically label new issues by keyword
# - label "bug" if the issue title/text contains "error"
# - label "feature" if the issue title/text contains "add"

def get_labels(title):
    title_lower = title.lower()
    labels = []
    if "error" in title_lower:
        labels.append("bug")
    if "add" in title_lower:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    test_titles = ["error test", "feature adding requirements", "email feature adding error"]
    for t in test_titles:
        print(t, get_labels(t))
