# Auto-label Issues Script
# This script automatically labels GitHub issues based on keywords
# Label "bug" if issue contains "error"
# Label "feature" if issue contains "add"

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
test_cases = [
    "error test",
    "feature adding requirements",
    "email feature adding error"
]

for case in test_cases:
    print(f"Title: {case} -> Labels: {get_labels(case)}")
