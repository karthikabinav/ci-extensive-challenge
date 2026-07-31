import re
# Auto-label script for GitHub issues
# Labels "bug" if issue contains "error", "feature" if contains "add"

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage
if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for t in test_cases:
        print(f"{t}: {get_labels(t)}")
