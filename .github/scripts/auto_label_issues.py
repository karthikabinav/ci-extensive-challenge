import re

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example usage for GitHub Action context
if __name__ == "__main__":
    # This script would be called by a GitHub workflow
    # It demonstrates the labeling logic required for the project
    test_cases = [
        ("error test", ["bug"]),
        ("feature adding requirements", ["feature"]),
        ("email feature adding error", ["bug", "feature"]),
    ]
    for title, expected in test_cases:
        result = get_labels(title)
        print(f"Title: {title!r} -> Labels: {result} (expected {expected})")
