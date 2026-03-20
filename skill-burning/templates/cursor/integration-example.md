# Cursor Integration Example

Example of burning a skill into .cursorrules with intelligent integration.

## Before Integration

### .cursorrules (Original)

```
# Git
Use feature branches
Clean commit history

# Development
Write clean code
Follow style guide

# Testing
Run tests before commit
```

## Skill to Burn: TDD

### Core Principles
1. Write tests before code
2. Maintain 80% coverage
3. Red-green-refactor cycle

## Analysis

### Project Profile
- **Format**: Categorized (with # headers)
- **Voice**: Imperative
- **Style**: Concise, direct
- **Existing Testing section**: Yes

### Integration Strategy
- Add to existing "Testing" category
- Add to "Development" category (TDD workflow)
- Match imperative voice
- Keep concise

## After Integration

### .cursorrules (Integrated)

```
# Git
Use feature branches
Clean commit history

# Development
Write clean code
Follow style guide
Write tests before code ← NEW
Test-driven development ← NEW

# Testing
Write tests before implementation ← NEW
Run tests before commit
Maintain 80% coverage ← NEW
Red-green-refactor cycle ← NEW
```

## What Changed

| Type | Change |
|------|--------|
| Added | 2 rules to Development section |
| Added | 3 rules to Testing section |
| Preserved | All existing content |
| Voice | Matched imperative style |
| Format | Matched categorized structure |

## Verification

✅ Natural flow - fits existing categories
✅ Voice consistent - imperative style
✅ No contradictions - complements existing
✅ Minimal disruption - only 5 new lines
✅ Clear directives - easy to follow

## Rollback

```bash
# Backup created
cp .cursorrules .cursorrules.backup

# To rollback
cp .cursorrules.backup .cursorrules
```
