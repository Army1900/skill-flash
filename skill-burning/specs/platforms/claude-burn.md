# Claude Platform Burning

How to burn skills into Claude projects (CLAUDE.md).

## File Structure

### CLAUDE.md

```markdown
# Project Name

## Overview
[Brief description]

## Context
[Project context]

## Working Patterns  ← Common integration point
[Existing patterns]

## Constraints
[Project constraints]

## Preferences
[Developer preferences]
```

## Detection Patterns

```bash
# Detect Claude project
find . -name "CLAUDE.md" -o -name ".claude"

# Detect Claude Code project
find . -name ".claude" -type d
```

## Common Patterns

### Pattern 1: Section-Based

**Existing:**
```markdown
## Working Patterns

### Development
- Feature branches
- Code reviews

### Testing
- Run tests before commit
```

**Integration:** Add to relevant section

### Pattern 2: Flat List

**Existing:**
```markdown
- Use feature branches
- Code review required
- Run tests before commit
```

**Integration:** Group with related items, or add to end in same style

### Pattern 3: Mixed Sections and Lists

**Existing:**
```markdown
## Development
- Feature branches
- Code reviews

## Testing
Tests required before commit
```

**Integration:** Match format of target section

## Style Matching

| Element | Pattern | Example |
|---------|---------|---------|
| Sections | `## Name` | `## Testing` |
| Subsections | `### Name` | `### TDD` |
| Bullets | `- Item` | `- Test first` |
| Numbered | `1. Item` | `1. Test first` |
| Emphasis | `**bold**` | `**Test first**` |
| Code | `` `code` `` | `` `pytest` `` |

## Integration Strategy

### Step 1: Read CLAUDE.md

```
Read: CLAUDE.md
```

### Step 2: Find Integration Point

```python
def find_integration_point(content, skill_principles):
    """Find best place to integrate in CLAUDE.md."""

    # Look for relevant sections
    sections = parse_sections(content)

    # Map skill principles to sections
    for principle in skill_principles:
        if principle.category in sections:
            return sections[principle.category]

    # If no match, find closest section
    # Or create new section matching existing style
```

### Step 3: Match Format

```python
def match_claude_format(existing_section, new_content):
    """Match existing CLAUDE.md format."""

    # Extract format from existing
    format = {
        "heading_depth": detect_heading_depth(existing_section),
        "list_style": detect_list_style(existing_section),
        "indentation": detect_indentation(existing_section),
    }

    # Apply to new content
    return apply_format(new_content, format)
```

### Step 4: Integrate

```python
# Use Edit tool for targeted integration
Edit(
    file_path="CLAUDE.md",
    old_string=[existing section],
    new_string=[enhanced section]
)
```

## Examples

### Example 1: Add to Existing Section

**Before:**
```markdown
## Working Patterns

### Development
- Use feature branches
- Code review required

### Testing
- Run tests before commit
```

**After (TDD integrated):**
```markdown
## Working Patterns

### Development
- Use feature branches
- Code review required
- Write tests before code ← NEW
- Test-driven development ← NEW

### Testing
- Write tests before implementation ← NEW
- Run tests before commit
- Maintain 80% coverage ← NEW
```

### Example 2: Create New Section

**Before:**
```markdown
## Working Patterns
- Feature branches
- Code reviews
```

**After (TDD integrated):**
```markdown
## Working Patterns
- Feature branches
- Code reviews

## Testing Principles  ← NEW section (matches style)
- Test before implementation
- Maintain 80% coverage
- Red-green-refactor cycle
```

### Example 3: Enhance Workflow

**Before:**
```markdown
## Development Process
1. Design feature
2. Implement feature
3. Test feature
4. Code review
```

**After (TDD integrated):**
```markdown
## Development Process
1. Design feature
2. Write test ← NEW
3. Run test (expect fail) ← NEW
4. Implement feature
5. Run test (expect pass) ← NEW
6. Refactor if needed ← NEW
7. Code review
```

## Common Sections

### Working Patterns
Most common integration point for skill principles.

```markdown
## Working Patterns

### Development
[Skill principles here]

### Testing
[Skill principles here]

### Code Quality
[Skill principles here]
```

### Development Workflow
Good for process-oriented skills.

```markdown
## Development Workflow
1. [Step 1]
2. [Step 2]
[Integrate skill workflow steps here]
```

### Standards
Good for threshold-based principles.

```markdown
## Standards

### Code Standards
- [Existing standards]

### Testing Standards  ← NEW
- 80% coverage minimum
- All new code tested
```

## Quality Checks

```markdown
## CLAUDE.md Verification

- [ ] Heading depth matches (## vs ###)
- [ ] List style matches (bullets vs numbered)
- [ ] Indentation matches
- [ ] No markdown syntax errors
- [ ] Reads naturally
- [ ] No abrupt transitions
- [ ] Related content grouped
```
