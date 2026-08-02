import re

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage for GitHub automation
    # This script is intended to be used in a GitHub Action to label issues
    import os
    title = os.getenv("ISSUE_TITLE", "")
    body = os.getenv("ISSUE_BODY", "")
    print(get_labels(title, body))
