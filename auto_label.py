# Auto-label issues by keyword
# Labels new issues: "bug" if title contains "error", "feature" if contains "add"

def get_labels(title: str):
    labels = []
    title_lower = title.lower()
    if "error" in title_lower:
        labels.append("bug")
    if "add" in title_lower:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage / test
    test_titles = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for t in test_titles:
        print(f"{t!r} -> {get_labels(t)}")
