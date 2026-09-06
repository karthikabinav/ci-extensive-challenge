"""
Auto-label issues by keyword.
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
Matching is case-insensitive substring match on title and body.
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
    import sys
    title = sys.argv[1] if len(sys.argv) > 1 else ""
    body = sys.argv[2] if len(sys.argv) > 2 else ""
    print(get_labels(title, body))
