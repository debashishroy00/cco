# CCO Configuration v0.1

## Memory System
Claude should remember what was built across sessions and prevent duplicates.

```yaml
cco:
  version: "0.1"
  memory:
    enabled: true
    path: ".claude/memory.json"
```

## System Context
You are helping a developer who prefers natural language descriptions.
Always check memory before creating new features to avoid duplicates.

## On Session Start
1. Load memory from `.claude/memory.json`
2. Inject summary of existing features
3. Warn about duplicates when detected

## Memory Format
```json
{
  "project": {
    "name": "MyProject",
    "created": "2025-01-17"
  },
  "features": {
    "feature_name": {
      "created": "2025-01-17",
      "files": ["src/file.js"],
      "description": "What it does"
    }
  }
}
```

## Commands
- When user says "remember this as X" -> Save to memory
- When user says "what have we built?" -> Show memory
- When user says "clear memory" -> Reset memory.json