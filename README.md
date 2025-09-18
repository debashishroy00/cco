# CCOM v0.1 - Claude Code Orchestrator and Memory

**One-command memory for Claude Code. Ships in 200 lines.**

## One-Command Install

```bash
# Install once
pip install ccom

# Use in any project
cd my-project
ccom init

# Test it immediately
ccom status
ccom remember "auth system"
ccom remember "auth system"  # ⚠️ Duplicate detected!

# Or install from GitHub (latest)
pip install git+https://github.com/debashishroy00/cco.git