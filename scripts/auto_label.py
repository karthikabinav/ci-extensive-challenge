"""
Auto-label issues by keyword:
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
Case-insensitive substring match.
"""

def get_labels(title: str, body: str = ""):
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
        "email feature adding error",
    ]
    for t in tests:
        print(t, "->", get_labels(t))
