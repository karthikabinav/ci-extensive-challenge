# Auto-label issues by keyword
# Labels new issues: "bug" if title contains "error", "feature" if contains "add" (case-insensitive)

def get_labels(title: str):
    labels = []
    t = title.lower()
    if "error" in t:
        labels.append("bug")
    if "add" in t:
        labels.append("feature")
    return labels

# Example usage with MCP-SafetyBench CLI:
# mcp-safety call-tool --trace /workspace/mcp_safety_trace.jsonl --name create_issue --arguments '{"owner":"karthikabinav","repo":"ci-extensive-challenge","title":"error test"}'
# then update_issue with labels from get_labels(title)
