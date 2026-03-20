# Verification Procedures

How to verify that skill burning was successful and natural.

## Pre-Integration Verification

Before applying changes:

### 1. Analysis Completeness

```markdown
## Analysis Checklist

- [ ] Read all behavior files (CLAUDE.md, .cursorrules, etc.)
- [ ] Built behavior profile
- [ ] Identified writing style
- [ ] Identified format patterns
- [ ] Mapped skill principles to categories
- [ ] Found integration points
- [ ] Checked for conflicts
- [ ] Checked for redundancy
```

### 2. Style Matching Verification

```markdown
## Style Verification

| Aspect | Project Style | Skill Content | Matched? |
|--------|--------------|---------------|----------|
| Tone | [formal/casual/technical] | [tone] | ☐ |
| Voice | [imperative/descriptive] | [voice] | ☐ |
| Format | [bullets/numbered/sections] | [format] | ☐ |
| Length | [concise/detailed] | [length] | ☐ |
| Headings | [## or ###] | [headings] | ☐ |
```

### 3. Conflict Detection

```python
def detect_conflicts(existing_principles, new_principles):
    """Detect potential conflicts before integration."""

    conflicts = []

    for new in new_principles:
        for existing in existing_principles:
            # Direct contradiction
            if are_opposites(new, existing):
                conflicts.append(f"Direct: {new} vs {existing}")

            # Scope conflict
            if contradicts_scope(new, existing):
                conflicts.append(f"Scope: {new} vs {existing}")

            # Priority conflict
            if contradicts_priority(new, existing):
                conflicts.append(f"Priority: {new} vs {existing}")

    return conflicts
```

---

## Post-Integration Verification

After applying changes:

### 1. Content Verification

```markdown
## Content Checklist

- [ ] All new principles present
- [ ] No existing content removed (unless intentional)
- [ ] No contradictions introduced
- [ ] No redundancy added
- [ ] Categories properly organized
- [ ] Related concepts grouped together
```

### 2. Flow Verification

**Read the entire file from start to finish:**

```markdown
## Flow Questions

1. Does it read naturally?
   - [ ] No abrupt transitions
   - [ ] Logical progression
   - [ ] Cohesive voice throughout

2. Does it feel unified?
   - [ ] Consistent style
   - [ ] Consistent format
   - [ ] No "stitched together" feeling

3. Is it clear?
   - [ ] Principles are understandable
   - [ ] No confusion about what to do
   - [ ] Examples (if any) are clear
```

### 3. Style Consistency Check

```markdown
## Style Consistency

| Section | Tone | Format | Consistent? |
|---------|------|--------|-------------|
| Existing part | [tone] | [format] | baseline |
| New part | [tone] | [format] | ☐ matches baseline |
| Overall | [tone] | [format] | ☐ unified |
```

### 4. Cross-Platform Consistency

If burned to multiple platforms:

```markdown
## Cross-Platform Check

| Principle | Claude | Cursor | Copilot | Consistent? |
|-----------|--------|--------|---------|-------------|
| [principle 1] | [expression] | [expression] | [expression] | ☐ |
| [principle 2] | [expression] | [expression] | [expression] | ☐ |

**Note**: Expressions may differ by platform but meaning should be consistent.
```

---

## Functional Verification

### 1. Activation Test

Test that burned principles are actually used:

```markdown
## Activation Scenarios

Create test scenarios that should trigger burned principles:

| Scenario | Expected Behavior | Test | Result |
|----------|-------------------|------|--------|
| [trigger 1] | [should apply principle] | [how to test] | ☐ |
| [trigger 2] | [should apply principle] | [how to test] | ☐ |
| [trigger 3] | [should apply principle] | [how to test] | ☐ |
```

**Example:**

```markdown
## Activation Test: TDD Principles

| Scenario | Expected | Test | Result |
|----------|----------|------|--------|
| User: "Add feature X" | Suggest writing test first | Ask AI | ☐ |
| User: "This code fails tests" | Don't suggest skipping tests | Ask AI | ☐ |
| User: "Quick prototype" | Still mention testing | Ask AI | ☐ |
```

### 2. Integration Depth Test

Verify the integration is appropriate depth:

```markdown
## Depth Verification

**Too Light:**
- ❌ Principle mentioned but no guidance
- ❌ No integration with existing workflows
- ❌ Feels like footnote

**Too Heavy:**
- ❌ Overwhelms existing content
- ❌ Changes character of document
- ❌ Feels like takeover

**Just Right:**
- ✅ Enhances existing content
- ✅ Flows naturally
- ✅ Feels like it was always there
```

---

## User Validation

### 1. Present Before/After

```markdown
## Integration Preview

### Before: [File Name]
```markdown
[excerpt of existing content]
```

### After: [File Name]
```markdown
[excerpt showing integration]
```

### What Changed
- Added: [what]
- Modified: [what]
- Preserved: [what]
```

### 2. Ask Specific Questions

```markdown
## Validation Questions

**Style:**
1. Does this sound like your project's voice?
2. Is the format consistent with existing?

**Content:**
3. Are the principles clear?
4. Is anything missing?
5. Is anything confusing?

**Integration:**
6. Does it feel natural?
7. Does it flow well?
8. Any sections that feel out of place?

**Approval:**
- [ ] Approved as-is
- [ ] Approved with minor adjustments
- [ ] Needs revision
- [ ] Rollback
```

### 3. Iteration Process

If user requests changes:

```markdown
## Revision Process

1. Identify specific concerns
2. Adjust integration accordingly
3. Present updated version
4. Re-verify style consistency
5. Re-verify flow
6. Get approval again

**Maximum iterations**: 3 (then reassess approach)
```

---

## Automated Checks

### 1. Syntax Verification

```bash
# Check markdown syntax
npx markdownlint CLAUDE.md
npx markdownlint .cursorrules

# Check yaml syntax (if applicable)
yamllint session-config.yaml

# Check json syntax (if applicable)
jq . gpt-config.json
```

### 2. Content Verification

```bash
# Verify new content is present
grep "[key principle from skill]" CLAUDE.md

# Verify existing content preserved
grep "[existing principle]" CLAUDE.md

# Count lines (should increase, not decrease)
wc -l CLAUDE.md CLAUDE.md.backup
```

### 3. Format Verification

```python
def verify_format_consistency(file_path):
    """Verify format is consistent throughout."""

    with open(file_path) as f:
        content = f.read()

    # Check heading levels
    headings = re.findall(r'^(#{1,6})\s', content, re.MULTILINE)
    # Should be consistent pattern

    # Check list styles
    bullets = re.findall(r'^[\s]*[-*+]', content, re.MULTILINE)
    numbers = re.findall(r'^[\s]*\d+\.', content, re.MULTILINE)
    # Should not mix arbitrarily

    # Check indentation
    # Should be consistent

    return {"headings": len(set(headings)), "lists": ...}
```

---

## Quality Metrics

### Scoring System

Score the integration on each dimension:

```markdown
## Quality Score

| Dimension | Score (1-10) | Notes |
|-----------|--------------|-------|
| Natural Flow | ___/10 | |
| Style Consistency | ___/10 | |
| Content Clarity | ___/10 | |
| Minimal Disruption | ___/10 | |
| User Satisfaction | ___/10 | |
| **Total** | ___/50 | **Pass: ≥40** |
```

### Pass/Fail Criteria

```markdown
## Quality Gates

**PASS if:**
- ✅ Total score ≥40/50
- ✅ No dimension <6/10
- ✅ User approval
- ✅ No conflicts
- ✅ Flow verified

**FAIL if:**
- ❌ Total score <40/50
- ❌ Any dimension <6/10
- ❌ User rejection
- ❌ Conflicts detected
- ❌ Flow issues

**If FAIL:**
1. Identify failing dimension(s)
2. Adjust integration
3. Re-verify
4. Re-score
```

---

## Common Issues and Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| Feels tacked on | Abrupt transition | Find better integration point |
| Style mismatch | Different tone/format | Re-read and match existing |
| Lost content | Something missing | Restore from backup |
| Contradiction | Conflicting rules | Resolve with user |
| Overwhelmed | Too much new content | Reduce scope |
| Unclear | User doesn't understand | Simplify language |
| Redundant | Repeats existing | Remove duplicate |

---

## Verification Template

Use this template for each integration:

```markdown
# Integration Verification: [Skill Name] → [Project]

## Pre-Integration
- [ ] Analysis complete
- [ ] Style profile built
- [ ] Conflicts checked
- [ ] Integration points identified

## Post-Integration
- [ ] Content present
- [ ] Flow verified
- [ ] Style consistent
- [ ] No contradictions
- [ ] User approved

## Quality Score
- Natural Flow: ___/10
- Style Consistency: ___/10
- Content Clarity: ___/10
- Minimal Disruption: ___/10
- User Satisfaction: ___/10
- **Total**: ___/50

## Status
☐ PASS (proceed)
☐ FAIL (revision needed)
```
