# Auto-label script for GitHub issues
# Labels new issues by keyword:
# - label "bug" if the issue contains "error"
# - label "feature" if it contains "add"

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage / test cases
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for title in test_cases:
        print(f"{title!r} -> {get_labels(title)}")
