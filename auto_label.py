"""Auto-label issues by keyword: bug if contains error, feature if contains add."""

def get_labels(title: str):
    t = title.lower()
    labels = []
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for title in tests:
        print(f"{title!r} -> {get_labels(title)}")
