# Auto Label Script for CI Extensive Challenge
# Labels issues by keyword:
# - "bug" if title/body contains "error"
# - "feature" if title/body contains "add"

def get_labels(title, body=""):
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    test_cases = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for title in test_cases:
        print(f"{title} => {get_labels(title)}")
