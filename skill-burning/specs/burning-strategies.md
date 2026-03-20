# Burning Strategies

Detailed strategies for intelligently integrating skills into different project contexts.

## Core Principle

> **Analyze → Match → Blend → Verify**

Never simply append. Always integrate naturally.

---

## Analysis Phase

### 1. Read Existing Behavior

**Files to read:**
```bash
# Primary behavior files
CLAUDE.md
.cursorrules
.copilot-instructions.md

# Secondary (for context)
README.md
CONTRIBUTING.md
docs/guidelines.md

# Project-specific
pyproject.toml
package.json
Makefile
```

### 2. Build Behavior Profile

Create a structured profile:

```yaml
project_profile:
  writing_style:
    tone: formal|casual|technical|direct
    voice: imperative|descriptive|questioning
    format: bullets|numbered|sections|prose
    length: concise|moderate|detailed

  structure:
    organization: category_based|workflow_based|priority_based
    headings: "## Section"|"### Subsection"|"# Topic"
    ordering: what_comes_first

  existing_categories:
    testing: [what_exists]
    code_style: [what_exists]
    workflow: [what_exists]
    communication: [what_exists]

  patterns:
    rule_format: "Do X"|"X is required"|"Consider X"
    example_format: code_block|bullet|inline
    workflow_style: numbered|bullets|arrows

  gaps:
    - [missing_category_1]
    - [missing_category_2]
```

### 3. Detect Integration Style

How does this project handle guidelines?

```markdown
## Pattern Detection

| Pattern | Indicator | Integration Strategy |
|---------|-----------|---------------------|
| Minimalist | Short file, <50 lines | Add brief bullets only |
| Comprehensive | Long file, >200 lines | Can add full workflows |
| Structured | Clear ## sections | Add to relevant section |
| Streamlined | No sections, just rules | Add related rules together |
| Example-heavy | Lots of code blocks | Include examples |
| Principle-based | "Always/never" language | Match principle style |
```

---

## Matching Phase

### 1. Style Matching

**Tone Mapping:**

```python
def match_tone(existing_tone, principle):
    """Rewrite principle to match existing tone."""

    tone_patterns = {
        "formal": {
            "template": "{action} shall {requirement}",
            "example": "Tests shall be written before implementation"
        },
        "casual": {
            "template": "{action} - {requirement}",
            "example": "Write tests first - keep coverage high"
        },
        "technical": {
            "template": "Maintain {metric} {threshold}",
            "example": "Maintain test coverage ≥80%"
        },
        "direct": {
            "template": "{requirement} required",
            "example": "Test coverage 80% required"
        }
    }

    return tone_patterns[existing_tone]["template"].format(...)
```

**Voice Mapping:**

```python
voice_patterns = {
    "imperative": ["Write tests", "Run coverage", "Maintain 80%"],
    "descriptive": ["Tests should be written", "Coverage is required"],
    "questioning": ["Have you written tests?", "Is coverage above 80%?"],
}
```

**Format Mapping:**

```python
format_patterns = {
    "bullets": "- Test first\n- 80% coverage",
    "numbered": "1. Test first\n2. 80% coverage",
    "sections": "## Testing\n### Test First\n### Coverage",
}
```

### 2. Category Mapping

Map skill principles to existing categories:

```yaml
skill_principle: "Write tests before code"
existing_categories:
  testing: "Run tests before committing"  # ✅ Match
  quality: "Code must pass review"       # ⚠️ Related
  workflow: "Design → Implement → Test"  # ❌ Wrong order

integration_point: "testing"
integration_method: "add to existing testing section"
```

**When no exact match:**

1. Find related category (test → quality)
2. Find broader category (coverage → standards)
3. Create new section (if truly new area)

---

## Blending Phase

### 1. Integration Techniques

**Technique 1: Enhancement**

```markdown
### Before
## Testing
- Run tests before committing
- Keep tests fast

### After
## Testing
- Write tests before implementation ← NEW
- Run tests before committing
- Keep tests fast
- Maintain 80% coverage ← NEW
```

**Technique 2: Workflow Integration**

```markdown
### Before
## Development Process
1. Design feature
2. Implement feature
3. Test feature
4. Commit

### After
## Development Process
1. Design feature
2. Write test ← NEW (blended)
3. Run test (expect fail) ← NEW (blended)
4. Implement feature
5. Run test (expect pass) ← NEW (blended)
6. Commit
```

**Technique 3: Standard Addition**

```markdown
### Before
## Code Quality
- Linting must pass
- Code review required

### After
## Code Quality
- Linting must pass
- Code review required
- Test coverage minimum 80% ← NEW standard
- All new code requires tests ← NEW standard
```

### 2. Section Organization

**If existing sections:**

```markdown
## Existing Structure
### Testing
[existing rules]

## Integration
ADD TO "Testing" section:
### Testing
[existing rules]
- Write tests first ← blended
- 80% coverage ← blended
```

**If no sections:**

```markdown
## Existing Structure
[flat list of rules]

## Integration
GROUP related rules:
### Testing
- Run tests (existing)
- Write first (new) ← grouped
- 80% coverage (new) ← grouped

### Code Style
- Use linter (existing)
```

**If adding new section:**

```markdown
## Create section that MATCHES existing style:

# If other sections are:
## Development
## Code Review
## Deployment

# Create similar:
## Testing  ← matches pattern
- Test first
- 80% coverage
```

---

## Verification Phase

### 1. Consistency Checks

```python
def check_consistency(existing_content, new_principles):
    """Verify no conflicts or contradictions."""

    checks = []

    # Check 1: No direct contradictions
    for principle in new_principles:
        for existing in existing_content:
            if contradicts(principle, existing):
                checks.append(f"⚠️ Contradiction: {principle} vs {existing}")

    # Check 2: No redundancy
    for principle in new_principles:
        if is_redundant(principle, existing_content):
            checks.append(f"⚠️ Redundant: {principle}")

    # Check 3: Style consistency
    if not matches_style(new_principles, existing_content):
        checks.append("⚠️ Style mismatch")

    return checks
```

### 2. Flow Verification

Read the integrated content and check:

```markdown
## Flow Checklist

- [ ] Reads naturally from start to finish
- [ ] No abrupt transitions
- [ ] Related concepts are grouped
- [ ] Logical progression
- [ ] Doesn't feel "stitched together"
```

### 3. User Validation

```markdown
## Validation Questions

1. Does this sound like your project's voice?
2. Does anything feel out of place?
3. Is the flow natural?
4. Are the principles clear?
5. Would anything be confusing?
```

---

## Platform-Specific Strategies

### Claude (CLAUDE.md)

**Common patterns:**
- Section-based (## Headers)
- Bulleted lists
- Mix of high-level and specific
- Often has "Working Patterns" section

**Strategy:**
1. Find most relevant section
2. Add bullets to existing lists
3. Match heading depth (## vs ###)
4. Keep bullet style consistent

**Example:**
```markdown
## Existing
### Working Patterns
- Feature branches
- Code reviews

## Integration
### Working Patterns
- Feature branches
- Code reviews
- Test-driven development ← matches style
```

### Cursor (.cursorrules)

**Common patterns:**
- Line-based rules
- Imperative voice ("Do X")
- Minimal formatting
- Sometimes grouped by topic

**Strategy:**
1. Add to related topic group
2. Use imperative voice
3. Keep minimal formatting
4. Match line length

**Example:**
```
# Existing
# Git workflow
Use feature branches
Clean history

# Integration
# Git workflow
Use feature branches
Write tests before commit ← matches style
Clean history
```

### Copilot Instructions

**Common patterns:**
- Markdown sections
- Descriptive sentences
- Context + rules
- May include examples

**Strategy:**
1. Add to relevant sections
2. Use descriptive style
3. Provide context
4. Match example format

**Example:**
```markdown
## Existing
## Code Quality
When writing code, ensure it passes linting.
Include comments for complex logic.

## Integration
## Code Quality
When writing code, ensure it passes linting.
Include comments for complex logic.
Write tests before implementing new features. ← matches descriptive style
Aim for 80% test coverage. ← specific metric
```

---

## Common Integration Scenarios

### Scenario 1: Missing Category

**Situation:** Skill has principles for area not covered in project

**Solution:** Create new section matching existing style

```markdown
## Existing sections
## Development
## Code Review
## Deployment

## New section (matches pattern)
## Testing
- Write tests first
- Maintain 80% coverage
```

### Scenario 2: Partial Overlap

**Situation:** Some principles exist, need to enhance

**Solution:** Add to existing section, enhance not replace

```markdown
## Existing
### Testing
- Run tests before commit

## Enhanced
### Testing
- Write tests before implementation ← NEW
- Run tests before commit (existing)
- Maintain 80% coverage ← NEW
```

### Scenario 3: Conflict Resolution

**Situation:** New principle conflicts with existing

**Solution:** Resolve with user, document decision

```markdown
## Conflict
Existing: "Quick iterations over tests"
New: "Tests before code"

## Resolution
Merged: "Write quick tests before code"
Rationale: Both value speed, tests ensure quality
```

### Scenario 4: Style Mismatch

**Situation:** Skill language doesn't match project

**Solution:** Rewrite to match project style

```markdown
## Project style (casual, brief)
- Keep tests fast
- Test before commit

## Skill language (formal, detailed)
"Test coverage shall not fall below 80%"

## Integrated (matches project)
- Keep tests fast
- Test before commit
- 80% coverage minimum ← rewritten to match
```

---

## Quality Metrics

Successful integration should achieve:

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Natural flow | 10/10 | Read and rate |
| Style consistency | 100% | Format matches |
| No contradictions | 0 conflicts | Automated check |
| User satisfaction | Approved | User feedback |
| Minimal disruption | <10% change | Lines changed |

---

## Anti-Patterns

**Avoid these:**

❌ **Simple append** - Adding to end without integration
❌ **Style mismatch** - Different tone/format than existing
❌ **Redundancy** - Repeating existing content
❌ **Over-integration** - Changing too much
❌ **Lost context** - Removing existing nuance

**Instead:**

✅ **Blend** - Find natural integration point
✅ **Match** - Copy existing style/format
✅ **Complement** - Add what's missing
✅ **Enhance** - Improve existing content
✅ **Preserve** - Keep existing value
