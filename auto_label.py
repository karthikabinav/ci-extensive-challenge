def get_labels(text):
    text = text.lower()
    labels = []
    if "error" in text:
        labels.append("bug")
    if "add" in text:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    import sys
    print(get_labels(" ".join(sys.argv[1:])))
