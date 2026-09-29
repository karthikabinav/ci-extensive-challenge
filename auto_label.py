"""
Auto-label script: labels new issues by keyword.
- if title/body contains "error" -> add label "bug"
- if title/body contains "add" -> add label "feature"
Matching is case-insensitive substring and both labels can apply.
"""

def labels_for_issue(title: str, body: str = "") -> list:
    text = ((title or "") + " " + (body or "")).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels


if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(f"{t!r} -> {labels_for_issue(t)}")
