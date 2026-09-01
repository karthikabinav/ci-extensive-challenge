"""Auto-label issues by keyword: bug if contains error, feature if contains add."""

def get_labels(title: str, body: str = ""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example usage / test
    tests = [
        ("error test", ""),
        ("feature adding requirements", ""),
        ("email feature adding error", ""),
    ]
    for t, b in tests:
        print(f"{t!r} -> {get_labels(t, b)}")
