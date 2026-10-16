def get_labels(title, body=""):
    text = (str(title) + " " + str(body)).lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    for title in ["error test", "feature adding requirements", "email feature adding error"]:
        print(title, get_labels(title))
