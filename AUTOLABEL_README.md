# Auto Label Script

This script automatically labels new issues by keyword:
- label "bug" if the issue contains "error"
- label "feature" if the issue contains "add"

Implementation uses GitHub Actions with github-script@v7 triggered on issues opened.