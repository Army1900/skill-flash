# Cursor Platform Burning

How to burn skills into Cursor projects (.cursorrules).

## File Structure

### .cursorrules

```
# [Category]
[Rule 1]
[Rule 2]

# [Another Category]
[Rule 3]
[Rule 4]
```

**Or flat:**

```
[Rule 1]
[Rule 2]
[Rule 3]
```

## Detection Patterns

```bash
# Detect Cursor project
find . -name ".cursorrules" -o -name ".cursor"

# Detect Cursor-specific config
find . -name ".cursorignore"
```

## Common Patterns

### Pattern 1: Categorized (with # headers)

**Existing:**
```
# Git
Use feature branches
Clean commit history

# Testing
Run tests before commit
```

**Integration:** Add to relevant category

### Pattern 2: Flat List

**Existing:**
```
Use feature branches
Code review required
Run tests before commit
Keep tests fast
```

**Integration:** Add in logical position, or create categories

### Pattern 3: Mixed

**Existing:**
```
# Development
Feature branches
Code reviews

Testing required before commit  ← No header
```

**Integration:** Add near related content, consider adding headers

## Style Matching

| Element | Pattern | Example |
|---------|---------|---------|
| Headers | `# Category` | `# Testing` |
| Rules | Imperative | `Write tests first` |
| Voice | Direct | `Use feature branches` |
| Length | Concise | `Test first` |
| Groups | Related together | Testing rules together |

## Integration Strategy

### Step 1: Read .cursorrules

```
Read: .cursorrules
```

### Step 2: Analyze Structure

```python
def analyze_cursor_rules(content):
    """Analyze .cursorrules structure."""

    return {
        "has_headers": bool(re.search(r'^#', content, re.MULTILINE)),
        "rule_style": detect_rule_style(content),  # imperative vs descriptive
        "organization": detect_organization(content),  # flat vs grouped
        "line_length": detect_line_length(content),
    }
```

### Step 3: Find Integration Point

```python
def find_cursor_integration_point(content, skill_principles):
    """Find best place in .cursorrules."""

    # If has headers, find relevant header
    if has_headers(content):
        headers = parse_headers(content)
        for principle in skill_principles:
            if principle.category in headers:
                return headers[principle.category]

    # If flat, find related rules
    related = find_related_rules(content, skill_principles)
    if related:
        return related.location

    # Otherwise, add to end or create category
    return end_of_file or create_new_category
```

### Step 4: Match Format

```python
def match_cursor_format(existing_content, new_principles):
    """Match .cursorrules format."""

    # Extract format
    format = {
        "has_headers": has_headers(existing_content),
        "rule_voice": detect_voice(existing_content),
        "line_length": avg_line_length(existing_content),
    }

    # Apply to new principles
    if format["has_headers"]:
        # Add headers if creating new category
        return with_headers(new_principles)
    else:
        # Flat format
        return as_flat_list(new_principles)
```

## Examples

### Example 1: Add to Existing Category

**Before:**
```
# Development
Use feature branches
Write clean code

# Testing
Run tests before commit
Keep tests fast
```

**After (TDD integrated):**
```
# Development
Use feature branches
Write clean code
Write tests before code ← NEW
Test-driven development ← NEW

# Testing
Write tests before implementation ← NEW
Run tests before commit
Keep tests fast
Maintain 80% coverage ← NEW
```

### Example 2: Create New Category

**Before:**
```
Use feature branches
Code review required
```

**After (TDD integrated):**
```
Use feature branches
Code review required

# Testing  ← NEW category
Write tests before code
Maintain 80% coverage
```

### Example 3: Flat List Integration

**Before:**
```
Use feature branches
Code reviews
Run tests before commit
Keep tests fast
```

**After (TDD integrated):**
```
Use feature branches
Write tests before code ← NEW (grouped with development)
Code reviews
Write tests before implementation ← NEW (grouped with testing)
Run tests before commit
Keep tests fast
Maintain 80% coverage ← NEW
```

## Voice Matching

Match the imperative voice:

```python
# If existing uses:
"Use feature branches"
"Run tests before commit"

# New principles should be:
"Write tests first"
"Maintain 80% coverage"
```

NOT:
```python
# NOT this:
"Tests should be written first"  ← too passive
"It is recommended to write tests"  ← too wordy
```

## Quality Checks

```markdown
## .cursorrules Verification

- [ ] Voice matches (imperative)
- [ ] Line length similar
- [ ] Groups consistent (or no groups)
- [ ] Headers consistent (or no headers)
- [ ] No markdown formatting (unless present)
- [ ] Concise rules
- [ ] Clear directives
```

## Special Considerations

### Cursor is Always-On

.cursorrules is applied automatically to every file.
- Be careful with broad rules
- Consider file-specific patterns
- Test that rules don't interfere

### File-Type Specific Rules

Cursor supports file-type specific rules:

```
# Python
Use type hints
Follow PEP 8

# JavaScript
Use ES6+
Prefer const over let
```

When burning, consider if principles are:
- Universal (apply to all files) → Add to main section
- Language-specific → Add to language section

### Example: Language-Specific

```
# General
Write tests before code

# Python
Use pytest for tests
Type hint test functions

# JavaScript
Use Jest for tests
Mock external dependencies
```
