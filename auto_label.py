"""
Automatic issue labeling script for ci-extensive-challenge

Labels new issues by keyword:
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

# Example tests:
# "error test" -> ["bug"]
# "feature adding requirements" -> ["feature"]
# "email feature adding error" -> ["bug", "feature"]

if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for t in test_cases:
        print(f"{t!r} -> {get_labels(t)}")
