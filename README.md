# CCO - Claude Code Orchestrator

Memory system for Claude Code that actually remembers what you built.

## The Problem
Claude Code forgets everything between sessions, forcing you to rebuild features and re-explain context repeatedly.

## The Solution  
CCO provides persistent memory that:
- Remembers features across sessions
- Prevents duplicate creation
- Injects context automatically

## Quick Start
```bash
# Clone the repo
git clone https://github.com/debashishroy00/cco.git
cd cco

# No installation needed - zero dependencies!

# Test the memory system
node .claude/cco.js status
node .claude/cco.js remember "feature_name" "description"