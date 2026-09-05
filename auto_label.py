"""
Auto-label issues by keyword.
- label "bug" if issue text contains "error"
- label "feature" if issue text contains "add"
"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    samples = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for s in samples:
        print(f"{s!r} -> {get_labels(s)}")
