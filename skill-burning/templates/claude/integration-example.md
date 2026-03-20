# Claude Integration Example

Example of burning a skill into CLAUDE.md with intelligent integration.

## Before Integration

### CLAUDE.md (Original)

```markdown
# My Project

## Overview
A web application for tracking tasks.

## Working Patterns

### Development
- Use feature branches
- Code review required

### Testing
- Run tests before committing
- Keep tests fast

## Constraints
- No external dependencies
- Must work offline
```

## Skill to Burn: TDD

### Core Principles
1. Write tests before code
2. Maintain 80% coverage
3. Red-green-refactor cycle

## Analysis

### Project Profile
- **Tone**: Casual, direct
- **Format**: Bulleted lists
- **Structure**: Section-based (### headings)
- **Existing Testing section**: Yes - perfect integration point

### Integration Strategy
- Add to existing "Testing" section
- Match bullet format
- Keep casual tone
- Enhance existing content

## After Integration

### CLAUDE.md (Integrated)

```markdown
# My Project

## Overview
A web application for tracking tasks.

## Working Patterns

### Development
- Use feature branches
- Code review required
- Write tests before implementing features ← NEW
- Test-driven development workflow ← NEW

### Testing
- Write tests before implementation ← NEW
- Run tests before committing
- Keep tests fast
- Maintain 80% test coverage ← NEW
- Red-green-refactor cycle ← NEW

## Constraints
- No external dependencies
- Must work offline
```

## What Changed

| Type | Change |
|------|--------|
| Added | 3 bullets to Development section |
| Added | 3 bullets to Testing section |
| Preserved | All existing content |
| Style | Matched existing casual tone |
| Format | Matched existing bullet style |

## Verification

✅ Natural flow - reads like it was always there
✅ Style consistent - matches existing tone
✅ No contradictions - complements existing rules
✅ Minimal disruption - only 6 new lines
✅ Clear meaning - TDD principles are clear

## Rollback

```bash
# Backup created
cp CLAUDE.md CLAUDE.md.backup

# To rollback
cp CLAUDE.md.backup CLAUDE.md
```
