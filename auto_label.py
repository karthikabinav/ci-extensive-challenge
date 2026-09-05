# Auto-label script: labels new issues by keyword
# - label "bug" if the issue contains "error"
# - label "feature" if it contains "add"
# Matching is case-insensitive and checks title + body.

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    # Example tests matching the requested samples
    samples = [
        "error test",
        "feature adding requirements",
        "email feature adding error",
    ]
    for s in samples:
        print(f"{s!r} -> {get_labels(s)}")
