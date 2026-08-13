import re

def get_labels(title, body=""):
    text = (title + " " + body).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage
issues = [
    "error test",
    "feature adding requirements",
    "email feature adding error"
]

for issue in issues:
    print(f"{issue} -> {get_labels(issue)}")
