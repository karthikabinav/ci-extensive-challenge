"""Automatically label issues by keyword:\n- label bug if text contains error\n- label feature if text contains add\n"""

def get_labels(title: str, body: str = "") -> list:
    text = f"{title} {body}".lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    tests = ["error test", "feature adding requirements", "email feature adding error"]
    for t in tests:
        print(f"{t!r} -> {get_labels(t)}")
