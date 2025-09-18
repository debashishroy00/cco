#!/bin/bash
# CCO v0.1 - Quick commit and push to GitHub

echo "Committing CCO v0.1 to GitHub..."
echo

# Check if git repo exists
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
    git remote add origin https://github.com/debashishroy00/cco.git
fi

# Add all files
echo "Adding files..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit."
    exit 0
fi

# Commit with timestamp
timestamp=$(date '+%Y-%m-%d %H:%M')
git commit -m "CCO v0.1 - One-command memory for Claude Code ($timestamp)"

# Push to GitHub
echo "Pushing to GitHub..."
if git push -u origin main; then
    echo
    echo "✅ Successfully pushed to GitHub!"
    echo
    echo "Ready for PyPI:"
    echo "  pip install build twine"
    echo "  python -m build"
    echo "  python -m twine upload dist/*"
    echo
    echo "Test install:"
    echo "  pip install cco"
    echo "  cco init"
else
    echo
    echo "❌ Push failed. Check your GitHub credentials."
fi

echo