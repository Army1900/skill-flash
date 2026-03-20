# Example: TDD Skill Burning

Complete example of burning TDD principles into a real project.

## Scenario

**Project:** Web application with existing guidelines

**Goal:** Burn TDD principles so the AI automatically applies them

---

## Step 1: Analyze Existing Project

### Read Existing Configs

**CLAUDE.md (original):**
```markdown
# TaskMaster

## Overview
Web application for task management

## Working Patterns

### Development
- Use feature branches
- Write clean code
- Code review required

### Testing
- Run tests before committing
- Keep tests fast

## Constraints
- Python 3.10+
- No external dependencies
```

**.cursorrules (original):**
```
# Git
Use feature branches
Clean history

# Development
Follow PEP 8
Write docstrings

# Testing
Run tests before commit
```

### Build Behavior Profile

```yaml
project_profile:
  writing_style:
    tone: casual
    voice: imperative
    format: section_based (###)
    length: concise

  structure:
    CLAUDE.md: ## Overview, ## Working Patterns (### sections)
    .cursorrules: # categorized headers

  existing_categories:
    development: [feature branches, clean code, code review]
    testing: [run tests, keep tests fast]

  patterns:
    CLAUDE.md: "### Category\n- Bullet\n- Bullet"
    .cursorrules: "# Category\nRule\nRule"
```

---

## Step 2: Extract TDD Principles

**From TDD skill, extract:**

1. **Write tests before code** (core principle)
2. **80% coverage minimum** (standard)
3. **Red-green-refactor cycle** (workflow)

---

## Step 3: Find Integration Points

### CLAUDE.md Integration

**Target: "Testing" section** - Already exists!

```
Existing:
### Testing
- Run tests before committing
- Keep tests fast

Integration point: Add to this section
```

### .cursorrules Integration

**Target: "Testing" category** - Already exists!

```
Existing:
# Testing
Run tests before commit

Integration point: Add to this category
```

---

## Step 4: Match Style

### CLAUDE.md Style

| Aspect | Existing | Match With |
|--------|----------|------------|
| Section header | `### Testing` | Same |
| Bullet style | `- Text` | Same |
| Voice | Imperative | "Write tests first" |
| Length | Concise | Short phrases |

### .cursorrules Style

| Aspect | Existing | Match With |
|--------|----------|------------|
| Category header | `# Testing` | Same |
| Rule style | Imperative | "Write tests first" |
| Length | Concise | Short phrases |

---

## Step 5: Generate Blended Content

### CLAUDE.md (Integrated)

```markdown
# TaskMaster

## Overview
Web application for task management

## Working Patterns

### Development
- Use feature branches
- Write clean code
- Code review required
- Write tests before code ← NEW (blended)
- Test-driven development ← NEW (blended)

### Testing
- Write tests before implementation ← NEW (blended)
- Run tests before committing
- Keep tests fast
- Maintain 80% coverage ← NEW (blended)
- Red-green-refactor cycle ← NEW (blended)

## Constraints
- Python 3.10+
- No external dependencies
```

### .cursorrules (Integrated)

```
# Git
Use feature branches
Clean history

# Development
Follow PEP 8
Write docstrings
Write tests before code ← NEW
Test-driven development ← NEW

# Testing
Write tests before implementation ← NEW
Run tests before commit
Maintain 80% coverage ← NEW
```

---

## Step 6: Show Before/After

### CLAUDE.md Comparison

**Before:**
```markdown
### Testing
- Run tests before committing
- Keep tests fast
```

**After:**
```markdown
### Testing
- Write tests before implementation ← NEW
- Run tests before committing
- Keep tests fast
- Maintain 80% coverage ← NEW
```

**Changes:**
- Added 2 bullets
- Preserved existing content
- Matches style
- Natural flow

---

## Step 7: Apply Changes

### Using Edit Tool (not Write)

```python
# CLAUDE.md
Edit(
  file_path="CLAUDE.md",
  old_string="### Testing\n- Run tests before committing\n- Keep tests fast",
  new_string="### Testing\n- Write tests before implementation\n- Run tests before committing\n- Keep tests fast\n- Maintain 80% coverage"
)
```

```python
# .cursorrules
Edit(
  file_path=".cursorrules",
  old_string="# Testing\nRun tests before commit",
  new_string="# Testing\nWrite tests before implementation\nRun tests before commit\nMaintain 80% coverage"
)
```

---

## Step 8: Verification

### Content Verification

| Check | Status |
|-------|--------|
| TDD principles present | ✅ |
| Existing content preserved | ✅ |
| Style matches | ✅ |
| No contradictions | ✅ |
| Natural flow | ✅ |

### Flow Check

Read CLAUDE.md from start to finish:
- ✅ Transitions are smooth
- ✅ No abrupt changes
- ✅ Feels cohesive

### Cross-Platform Check

| Principle | CLAUDE.md | .cursorrules | Consistent? |
|-----------|-----------|-------------|-------------|
| Test first | "Write tests before code" | "Write tests before code" | ✅ |
| 80% coverage | "Maintain 80% coverage" | "Maintain 80% coverage" | ✅ |
| TDD cycle | "Red-green-refactor" | (not in cursor) | ✅ (appropriate) |

---

## Step 9: User Validation

### Present to User

```markdown
## TDD Integration Complete

I've analyzed your project's existing guidelines and integrated
TDD principles in a natural way.

### What I Found
- **Style**: Casual, imperative voice
- **Format**: Section-based with bullets
- **Existing testing section**: Perfect fit

### Changes Made

**CLAUDE.md:**
- Added 2 principles to Development section
- Added 2 principles to Testing section
- Total: +4 lines

**.cursorrules:**
- Added 2 rules to Development section
- Added 2 rules to Testing section
- Total: +4 lines

### Preview

**Before:**
### Testing
- Run tests before committing

**After:**
### Testing
- Write tests before implementation
- Run tests before committing
- Maintain 80% coverage

### Verification
✅ Style matches your project
✅ No contradictions
✅ Natural flow
✅ All TDD principles present

### Backups
- CLAUDE.md.backup
- .cursorrules.backup

### Rollback (if needed)
```bash
cp CLAUDE.md.backup CLAUDE.md
cp .cursorrules.backup .cursorrules
```

**Does this look good?**
- [ ] Approve
- [ ] Adjust
- [ ] Rollback
```

---

## Result: Automatic TDD

After burning, when the AI works on this project:

**User:** "Add a login feature"

**AI (with TDD burned):**
> I'll add the login feature. Following your project's TDD principles:
> 1. First, I'll write tests for the login functionality
> 2. Then implement the login code
> 3. Verify all tests pass
>
> What testing framework are you using? (I see you use pytest)

**Without burning:**
> I'll add the login feature. Let me create the login form...

---

## Integration Record

```markdown
# Integration Record

**Date:** 2025-01-15
**Skill:** TDD
**Approach:** Blended integration

## Changes

### CLAUDE.md
- Added: 4 bullets (Development: 2, Testing: 2)
- Location: Lines 15-18, 24-26
- Style: Matched existing casual/imperative

### .cursorrules
- Added: 4 rules (Development: 2, Testing: 2)
- Location: Lines 10-11, 17-18
- Style: Matched existing imperative

## Quality Metrics
- Natural flow: ✅
- Style consistency: ✅
- Content coverage: ✅
- User approval: ✅

## Rollback
Backups at: CLAUDE.md.backup, .cursorrules.backup
```

---

## Key Takeaways

### What Worked

1. **Analysis first** - Understood project style before changing
2. **Found natural fit** - Existing Testing section was perfect
3. **Matched style** - Casual, imperative, concise
4. **Minimal change** - Only 4 lines per file
5. **Blended seamlessly** - Feels like it was always there

### Result

- TDD is now **automatic** - AI applies without prompting
- **Zero token cost** - Principles are in config, not skill
- **Natural** - Doesn't feel like an add-on
- **Consistent** - Same behavior across platforms
