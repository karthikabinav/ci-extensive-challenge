# Auto Label Script
# Automatically labels issues by keyword
# label "bug" if issue contains "error"
# label "feature" if issue contains "add"

def get_labels(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Test cases
if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(t, "->", get_labels(t))
