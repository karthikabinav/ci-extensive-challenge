import re

def get_labels_for_issue(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for GitHub Actions or webhook handler
if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for title in test_cases:
        print(f"Issue: {title} => Labels: {get_labels_for_issue(title)}")