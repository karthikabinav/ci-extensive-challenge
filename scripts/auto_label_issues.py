"""
Auto Label Issues by Keyword
This script automatically labels new GitHub issues based on keywords in title/body.
- If issue contains "error" -> add label "bug"
- If issue contains "add" -> add label "feature"
Usage: intended for GitHub Actions workflow triggered on issues: opened
"""
import os

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for t in tests:
        print(t, "=>", get_labels(t))
