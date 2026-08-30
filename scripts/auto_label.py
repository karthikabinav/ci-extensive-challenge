# Auto-label script for issues
# Labels new issues by keyword:
# - label "bug" if issue contains whole word "error" (case-insensitive)
# - label "feature" if issue contains whole word "add" (case-insensitive)
# Uses word boundaries to avoid false positives (e.g., "adding" should NOT match "add")
import re

def get_labels(title: str, body: str = ""):
    text = f"{title or chr(39)+chr(39)} {body or chr(39)+chr(39)}".lower()
    labels = []
    if re.search(r"\\berror\\b", text):
        labels.append("bug")
    if re.search(r"\\badd\\b", text):
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
