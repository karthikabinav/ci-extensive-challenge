import re

def labels_for(text):
    t = (text or "").lower()
    labels = []
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

if __name__ == "__main__":
    import sys
    print(labels_for(sys.argv[1] if len(sys.argv) > 1 else ""))
