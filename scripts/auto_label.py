"""
Auto-label issues by keyword.
- label bug if issue title/body contains error (case-insensitive)
- label feature if issue title/body contains add (case-insensitive)
This logic mirrors .github/workflows/auto-label.yml
"""

def get_labels_for_issue(title, body=""):
    text = ((title or "") + " " + (body or "")).lower()
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
        print(repr(s) + " -> " + str(get_labels_for_issue(s)))
