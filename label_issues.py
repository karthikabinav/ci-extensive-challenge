"""Automatically label issues by keyword.

Label "bug" if the issue contains "error", and label "feature" if it contains "add".
Both labels are applied independently (using separate if statements, not elif),
so an issue containing both keywords gets both labels.
"""

def get_labels(title, body=""):
    text = f"{title or ""} {body or ""}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for t in ["error test", "feature adding requirements", "email feature adding error"]:
        print(t, "->", get_labels(t))
