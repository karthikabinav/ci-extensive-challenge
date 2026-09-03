"""
Auto-label issues by keyword:
- label "bug" if text contains "error"
- label "feature" if text contains "add"
"""
def get_labels(title: str, body: str = "") -> list:
    text = (title + " " + body).lower()
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
        print(f"{t!r} -> {get_labels(t)}")
