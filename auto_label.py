def get_labels(title: str):
    """Automatically determine labels based on keywords."""
    labels = []
    lowered = title.lower()
    if "error" in lowered:
        labels.append("bug")
    if "add" in lowered:
        labels.append("feature")
    return labels

# Example usage:
# titles = ["error test", "feature adding requirements", "email feature adding error"]
# for t in titles:
#     print(t, "->", get_labels(t))
