# Auto Label Issues by Keyword
# label "bug" if issue contains "error", and "feature" if contains "add"

def get_labels(title, body=""):
    content = (title + " " + body).lower()
    labels = []
    if "error" in content:
        labels.append("bug")
    if "add" in content:
        labels.append("feature")
    return labels

# Test cases
if __name__ == "__main__":
    tests = [
        "error test",
        "feature adding requirements",
        "email feature adding error"
    ]
    for t in tests:
        print(f"{t} -> {get_labels(t)}")
