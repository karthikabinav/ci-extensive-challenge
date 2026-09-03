# Auto-label issues by keyword
# Labels new issues: "bug" if title/body contains "error", "feature" if contains "add"

def get_labels(title: str, body: str = ""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage with GitHub API:
# for each new issue, call get_labels(issue_title, issue_body) and apply labels via API
if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(t, "->", get_labels(t))
