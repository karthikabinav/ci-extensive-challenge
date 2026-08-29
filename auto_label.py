"""
Auto-label issues by keyword.
- label "bug" if issue title/body contains "error"
- label "feature" if issue title/body contains "add"
Case-insensitive substring matching.
"""

def get_labels(text: str):
    text_lower = text.lower()
    labels = []
    if "error" in text_lower:
        labels.append("bug")
    if "add" in text_lower:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    import sys
    title = sys.argv[1] if len(sys.argv) > 1 else ""
    print(get_labels(title))
