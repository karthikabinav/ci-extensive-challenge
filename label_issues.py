def get_labels(title):
    labels = []
    lower = title.lower()
    if "error" in lower:
        labels.append("bug")
    if "add" in lower:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for title in ["error test", "feature adding requirements", "email feature adding error"]:
        print(title, get_labels(title))
