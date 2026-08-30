# Auto-label script for issues
# Labels new issues by keyword:
# - label "bug" if the issue contains "error"
# - label "feature" if the issue contains "add"
# Uses simple substring matching (case-insensitive)

def get_labels(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
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
