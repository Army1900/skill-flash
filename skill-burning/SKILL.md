---
name: skill-burning
description: Analyze project or agent behavior patterns and intelligently integrate skill principles in a natural, consistent way. Reads existing guidelines first, then seamlessly blends new principles.
---

# Skill Burning

Analyze project or agent behavior patterns and intelligently integrate skill principles in a natural, consistent way. Not just appending - understanding context and blending seamlessly.

## Quick Execution Checklist

- [ ] 1. Identify target skill and project/agent
- [ ] 2. **ANALYZE: Read existing behavior patterns**
- [ ] 3. Detect current style, tone, and structure
- [ ] 4. Extract core principles from skill
- [ ] 5. Find integration points (not append points)
- [ ] 6. Match writing style and format
- [ ] 7. Generate blended content
- [ ] 8. Apply with minimal disruption
- [ ] 9. Verify consistency and natural flow
- [ ] 10. Document changes and rollback plan

---

## Trigger

Use this skill when:
- User wants to "burn" or "internalize" a skill
- User wants a skill to become "automatic behavior"
- User asks to integrate practices into project guidelines
- User wants team standards to be "always on"

---

## What is Skill Burning?

**Skill Burning** = Understanding existing behavior + Seamlessly integrating new principles

| Wrong Approach | Right Approach |
|----------------|----------------|
| Append to end of file | Find natural integration point |
| Use different format | Match existing format |
| Ignore existing rules | Complement existing rules |
| Change writing style | Match existing style |
| Add without context | Blend with context |

**Goal**: The burned principles should feel like they were always there.

---

## Step 1: Initial Setup

### 1.1 Identify Targets

Ask the user:

```
I'll analyze your project and intelligently integrate this skill.

1. **Skill to burn**: Which skill?
2. **Target**: Project directory or agent config?
3. **Depth**: How integrated?
   - Light: Reference existing practices
   - Medium: Add missing practices
   - Deep: Comprehensive integration
```

---

## Step 2: Analyze Existing Behavior (CRITICAL)

### 2.1 Read All Existing Configs

Use **Read tool** to read existing behavior files:

```
Read: CLAUDE.md
Read: .cursorrules
Read: .copilot-instructions.md
Read: README.md (guidelines section)
Read: package.json (scripts, config)
Read: pyproject.toml or similar
```

### 2.2 Extract Behavior Profile

Build a profile of existing behavior:

```markdown
## Project Behavior Profile

### Writing Style
- Tone: [formal/casual/technical]
- Format: [bullets/numbered/sections]
- Voice: [imperative/descriptive/questioning]
- Length: [concise/detailed]

### Existing Principles (by category)
**Testing**: [what's already there]
**Code Style**: [what's already there]
**Workflow**: [what's already there]
**Communication**: [what's already there]

### Structure Patterns
- How are rules organized? [grouping method]
- What comes first? [priority order]
- How are examples shown? [example format]

### Gaps (what's missing)
- [gap 1]
- [gap 2]
```

### 2.3 Identify Integration Style

Determine how this project handles guidelines:

| Pattern | Integration Approach |
|---------|---------------------|
| Minimal, concise | Add brief principles only |
| Comprehensive, detailed | Add full workflows |
| Section-based | Find related section |
| Bulleted lists | Match bullet style |
| Code examples | Include examples |

---

## Step 3: Extract Skill Principles

### 3.1 Read Target Skill

```
Read: [skill-file-path]
```

### 3.2 Extract Core Principles

Extract ONLY what's essential:

```
✅ Keep:
- Fundamental rules
- Decision frameworks
- "Always" and "never" statements
- Core workflows

❌ Discard:
- Examples
- Explanations
- Edge cases
- Platform-specific details
```

### 3.3 Map to Existing Profile

Map skill principles to existing categories:

```markdown
### Skill-to-Project Mapping

**Skill Principle**: [principle from skill]
**Existing Category**: [matches this category]
**Integration Point**: [add here]
**Format Needed**: [match this style]

**Skill Principle**: [another principle]
**Existing Category**: [NEW - no existing equivalent]
**Integration Point**: [create new section or add to related]
**Format Needed**: [match project style]
```

---

## Step 4: Find Integration Points

### 4.1 Natural Integration (Preferred)

Find where principles naturally fit:

**Example 1: Project has "Testing" section**

```markdown
## Existing CLAUDE.md
### Testing
- Run tests before committing
- Keep tests fast

## Integration
Add TO this section (not create new one):
### Testing
- Run tests before committing
- Keep tests fast
- Write tests BEFORE code (TDD) ← blended in
- Aim for 80% coverage ← blended in
```

**Example 2: Project has workflow section**

```markdown
## Existing structure
1. Feature development
2. Code review
3. Deployment

## Integration
Add relevant steps INSIDE workflow:
1. Feature development
   - Write test first ← new step blended
   - Implement feature
   - Run tests
2. Code review
...
```

### 4.2 Complementary Integration (When no exact fit)

If no exact category exists, find related one:

```markdown
## No "Testing" section, but has "Quality" section

### Quality
- Code review required
- Linting must pass

## Integration
Add to Quality section:
### Quality
- Code review required
- Linting must pass
- Test coverage minimum 80% ← complementary
- Tests written before code ← complementary
```

### 4.3 New Section (Last resort)

Only create new section when:
- No related category exists
- Principle represents fundamentally new area
- It fits the project's structure

```markdown
## Add new section that MATCHES existing style:

### Testing Principles
- Write tests before code
- Maintain 80% coverage
- Run tests before committing
```

---

## Step 5: Match Writing Style

### 5.1 Style Matching Table

Match the project's existing style:

| If project uses... | Then use... |
|-------------------|-------------|
| "Always do X" | "Always write tests first" |
| "Do X" | "Write tests first" |
| "X is required" | "Tests are required" |
| "Please do X" | "Please write tests first" |
| "Consider X" | "Consider writing tests" |
| Bullets (-) | - Test first |
| Numbers (1.) | 1. Test first |
| Concise | "Test first" |
| Detailed | "Write tests before implementing code" |

### 5.2 Tone Matching

Match the project's tone:

```markdown
## Formal tone
"Test coverage shall not fall below 80%."

## Casual tone
"Keep test coverage above 80%."

## Technical tone
"Maintain minimum 80% test coverage threshold."

## Direct tone
"80% test coverage required."
```

### 5.3 Format Matching

Match the project's format:

```markdown
## If project uses this format:
### Category
- Rule 1
- Rule 2

## Use this format:
### Testing
- Write tests first
- Maintain 80% coverage
```

---

## Step 6: Generate Blended Content

### 6.1 Read Existing Content

```
Read: [target-config-file]
```

### 6.2 Generate Integration

**WRONG** (simple append):
```markdown
[existing content]

## New TDD Principles
- Write tests first
- Test coverage 80%
```

**RIGHT** (blended integration):
```markdown
### Testing Workflow
1. Design test cases
2. Write tests ← NEW: blended into existing workflow
3. Run tests (should fail) ← NEW: blended
4. Implement code
5. Run tests (should pass) ← NEW: blended
6. Refactor if needed

**Coverage**: Maintain minimum 80% ← NEW: blended as standard
```

### 6.3 Show Before/After

Present to user:

```markdown
## Integration Preview

### Before (Existing)
[excerpt from existing file]

### After (Integrated)
[show how it looks integrated]

### Changes
- Added: [what was added]
- Modified: [what was modified]
- Preserved: [what stayed the same]
```

---

## Step 7: Apply with Minimal Disruption

### 7.1 Backup First

```bash
cp [file] [file].backup
```

### 7.2 Apply Integration

Use **Edit tool** for targeted changes:

```python
# Replace specific section with integrated version
Edit(
  file_path="CLAUDE.md",
  old_string=[existing section],
  new_string=[integrated section]
)
```

NOT **Write tool** (replaces entire file):
```python
# DON'T DO THIS - loses existing context
Write("CLAUDE.md", entire_new_content)
```

### 7.3 Verify Changes

After applying, verify:

```markdown
## Integration Verification

✅ Existing content preserved
✅ New principles integrated
✅ Style matches existing
✅ Format matches existing
✅ No contradictions
✅ Natural flow maintained
```

---

## Step 8: Multi-Platform Consistency

When burning to multiple platforms:

### 8.1 Ensure Consistent Principles

Same principle, appropriate expression:

```markdown
## CLAUDE.md (concise bullets)
### Testing
- Test before code
- 80% coverage minimum

## .cursorrules (imperative)
# Testing rules
Write tests before implementing code.
Maintain 80% test coverage.

## Copilot instructions (descriptive)
## Testing guidelines
When implementing features, write tests first.
Ensure test coverage stays above 80%.
```

### 8.2 Cross-Reference

Document how principles map across platforms:

```markdown
## Cross-Platform Reference

| Principle | Claude | Cursor | Copilot |
|-----------|--------|--------|---------|
| Test first | "Test before code" | "Write tests first" | "write tests first" |
| 80% coverage | "80% coverage" | "80% test coverage" | "above 80%" |
```

---

## Step 9: Verification

### 9.1 Consistency Check

Verify no contradictions:

```markdown
## Consistency Check

### Check 1: No Conflicting Rules
Existing: "Quick iterations over tests"
New: "Tests before code"
❓ Conflict? No - complementary

### Check 2: No Redundancy
Existing: "Run tests before commit"
New: "Test before code"
❓ Redundant? No - different timing

### Check 3: Style Consistency
Existing tone: [casual/direct]
New additions: [casual/direct]
✅ Match
```

### 9.2 Flow Check

Read the integrated content and verify:

```markdown
## Flow Check

Read from start to finish. Does it:
- ✅ Flow naturally?
- ✅ Feel cohesive?
- ✅ Make sense in order?
- ✅ Not feel "tacked on"?
```

### 9.3 User Validation

Ask user:

```markdown
## Integration Complete

I've analyzed your project's existing guidelines and integrated
the skill principles in a natural way.

### What I Found
- Writing style: [style]
- Existing categories: [categories]
- Integration approach: [approach]

### Changes Made
[show before/after for each file]

### Please Verify
1. Read the updated files
2. Check that style matches
3. Verify principles are present
4. Confirm natural flow

Approve? Adjust? Rollback?
```

---

## Step 10: Documentation

### 10.1 Integration Record

Create `.claude/integration-record.md`:

```markdown
# Skill Integration Record

**Date**: [timestamp]
**Skill**: [skill name]
**Approach**: Blended integration (not append)

## What Was Integrated

| Principle | Location | Format |
|-----------|----------|--------|
| [principle 1] | CLAUDE.md, Testing section | Bullet |
| [principle 2] | .cursorrules, line 15 | Imperative |

## Integration Strategy

- **Style matched**: [how style was matched]
- **Integration points**: [where added]
- **Conflicts resolved**: [any conflicts]

## Rollback
Backup: [file].backup
Command: cp [file].backup [file]
```

---

## Platform-Specific Analysis

### Claude (CLAUDE.md)

**Typical patterns:**
- Section-based (## Headers)
- Bulleted lists
- Mix of principles and workflows
- Often has "Working Patterns" section

**Integration strategy:**
- Find relevant section
- Add bullets to existing lists
- Match section heading style

### Cursor (.cursorrules)

**Typical patterns:**
- Line-based rules
- Often imperative ("Do X")
- Minimal formatting
- Sometimes grouped by topic

**Integration strategy:**
- Add rules to related topic groups
- Match imperative voice
- Keep minimal formatting

### Copilot (.copilot-instructions.md)

**Typical patterns:**
- Markdown sections
- Descriptive sentences
- Often has context + rules
- May include examples

**Integration strategy:**
- Add to relevant sections
- Use descriptive style
- Include context

---

## Common Integration Patterns

### Pattern 1: Complementary Addition

```
Existing: "Keep code clean"
Add: "Keep tests clean too"
Result: Both integrated naturally
```

### Pattern 2: Workflow Enhancement

```
Existing workflow: Design → Code → Test
Enhanced workflow: Design → Test → Code → Test
Result: Test steps blended in
```

### Pattern 3: Standard Establishment

```
Existing: "Try to maintain coverage"
Add: "80% coverage minimum"
Result: Clear standard established
```

### Pattern 4: Missing Category

```
No existing category for [X]
Create new section matching existing style
Result: Feels like it was always there
```

---

## Quality Checklist

Before completing:

**Analysis:**
- [ ] Read all existing behavior files
- [ ] Built behavior profile
- [ ] Identified writing style
- [ ] Found integration points

**Integration:**
- [ ] Extracted core principles only
- [ ] Matched writing style
- [ ] Matched format
- [ ] Found natural integration points
- [ ] Avoided simple append

**Verification:**
- [ ] No contradictions with existing
- [ ] No redundancy
- [ ] Natural flow maintained
- [ ] Style consistent throughout
- [ ] User validated changes

**Safety:**
- [ ] Backups created
- [ ] Integration record created
- [ ] Rollback documented

---

## Example Execution

**User**: "Burn TDD into this project"

**You**:
1. ✅ Read: CLAUDE.md, .cursorrules, etc.
2. ✅ Analyze: Project uses casual tone, section-based, has "Testing" section
3. ✅ Extract: "Test first", "80% coverage", "Red-green-refactor"
4. ✅ Map: All fit in existing "Testing" section
5. ✅ Match: Use casual tone, bullet points
6. ✅ Generate: Enhanced "Testing" section with new principles blended
7. ✅ Show: Before/after preview
8. ✅ Apply: Edit existing section
9. ✅ Verify: Natural flow, style matches
10. ✅ Document: Integration record

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Feels "tacked on" | Simple append | Re-integrate at natural point |
| Style doesn't match | Didn't analyze style | Re-read and match |
| Contradictions | Didn't check conflicts | Resolve with user |
| Can't find fit | No good integration point | Create new section matching style |
| Lost existing content | Used Write not Edit | Restore from backup, use Edit |

---

## Key Principles

1. **Analyze first** - Understand before changing
2. **Blend, don't append** - Find natural integration points
3. **Match style** - Feel like it was always there
4. **Minimal disruption** - Change only what's needed
5. **Verify flow** - Read end-to-end
6. **User validates** - Get approval before finalizing
