# Platform Format Reference

Reference documentation for supported AI platform skill/prompt formats.

## Claude Skills

### Input Format (SKILL.md)

```markdown
---
name: skill-name
description: One-line description
---

# Skill Name

Detailed description...

## Core Principles

- Principle 1
- Principle 2

## Workflow

### Step 1: Name
Instructions...

### Step 2: Name
Instructions...
```

### Output Format

```
output/
├── CLAUDE.md.fragment    # Add to project CLAUDE.md
├── session.yaml          # Session config
├── SKILL.md              # Optimized skill
├── scripts/
│   ├── check_coverage.sh
│   └── validate_tests.py
└── report.json
```

---

## OpenAI GPTs

### Input Format (JSON)

```json
{
  "name": "GPT Name",
  "description": "Description",
  "instructions": "Full instructions here...",
  "actions": [
    {
      "name": "action_name",
      "description": "What it does"
    }
  ]
}
```

### Output Format

```
output/
├── gpt-config.json       # Optimized config
├── functions/
│   └── function_name.py  # Function implementations
└── report.json
```

---

## Cursor (.cursorrules)

### Input Format (.cursorrules)

```
# Line-based rules
Always use TypeScript for new files
Never commit directly to main
Ask user before running destructive commands
```

### Output Format

```
output/
├── .cursorrules          # Optimized rules
├── .vscode/
│   └── tasks.json        # VSCode tasks
└── report.json
```

---

## GitHub Copilot

### Input Format (.copilot-instructions)

```
# Project Instructions

## Coding Standards
- Use 4 space indentation
- Follow functional patterns

## Workflow
1. Write tests first
2. Implement feature
3. Run linting
```

### Output Format

```
output/
├── .copilot-instructions-optimized
├── .github/
│   └── workflows/        # CI/CD scripts
└── report.json
```

---

## Universal Format

For cross-platform compatibility, skills can be defined in universal YAML:

```yaml
name: universal-skill
description: Works across platforms

principles:
  - Core principle 1
  - Core principle 2

rules:
  - name: rule_name
    check: executable
    script: |
      #!/bin/bash
      echo "Checking..."

decisions:
  - prompt: "What framework?"
    options: [React, Vue, Svelte]
    default: React

workflow:
  - step: setup
    action: initialize_project
  - step: implement
    action: write_code
```
