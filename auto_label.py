"""
Auto-label new issues by keyword.
- label "bug" if issue contains "error"
- label "feature" if issue contains "add"
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
    # Example usage / simple test
    test_cases = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for title, body in test_cases:
        print(f"{title!r} -> {get_labels(title, body)}")
