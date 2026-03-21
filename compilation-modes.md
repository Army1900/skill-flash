# Compilation Modes Discussion

Should skill compilation create new files or edit existing ones?

## Problem Statement

Current skill-compilation always creates new files in `optimized/` directory.
This raises questions:
- What happens to the original file?
- How to choose between versions?
- Can I see what changed?

## Analysis: Three Approaches

### Approach 1: In-Place Edit (替换原文件)

**Workflow:**
```
compile_skill(tdd.md) → 直接修改 tdd.md
```

**Pros:**
- ✅ Simple workflow
- ✅ No extra files
- ✅ Immediate effect

**Cons:**
- ❌ **NO ROLLBACK** - If optimization is bad, original is lost
- ❌ **NO COMPARISON** - Can't see what changed
- ❌ **NO EXPERIMENTATION** - Can't try different strategies
- ❌ **HIGH RISK** - Direct modification of working file

**Use case:** Only when optimization is proven and trusted

---

### Approach 2: Create New File (创建新文件)

**Workflow:**
```
compile_skill(tdd.md) → 生成 optimized/tdd.md
```

**Pros:**
- ✅ Safe - Original preserved
- ✅ Comparable - Can diff versions
- ✅ Experimental - Can generate multiple
- ✅ Reversible - Delete if unhappy

**Cons:**
- ⚠️ File clutter
- ⚠️ Choice confusion
- ⚠️ Which file to use?

**Use case:** Default mode for new compilations

---

### Approach 3: Hybrid (混合模式) ⭐ RECOMMENDED

**Workflow:**
```
compile_skill(tdd.md, mode=[auto|new|replace])

Auto mode: Ask user for choice
- "Generate new file or replace original?"
- "Choose optimization strategy: aggressive/balanced/conservative"
- Generate accordingly

New mode: Create optimized/tdd.md
Replace mode: Edit tdd.md in-place (with backup)
```

**Pros:**
- ✅ **User choice** - Decide per compilation
- ✅ **Safety first** - Default to creating new file
- ✅ **Flexibility** - Can replace when confident
- ✅ **Experimentation** - Generate multiple variants

**Cons:**
- ⚠️ Slightly more complex
- ⚠️ Requires user decision

---

## Recommended Design

### Step 1: Initial Questions (Already in SKILL.md)

Add mode selection:

```markdown
## Step 1: Initial Setup

### 1.1 Collect Decisions

Before proceeding, ask the user:

```
I'll optimize this skill. I need a few details:

1. **Output mode?**
   - new: Create optimized/[skill-name].md (safe, can compare)
   - replace: Edit original file in-place (with backup)

2. **Optimization strategy?**
   - aggressive: Max token savings (~40%), may lose explanations
   - balanced: Moderate savings (~15%), keeps key explanations
   - conservative: Minimal changes (~5%), very safe

3. **Output location?**
   - Default: ./optimized/
   - Or specify path
```

Wait for user choices before proceeding.
```

### Step 2: Smart Defaults

```python
# Auto mode (if user doesn't specify)
DEFAULT_MODE = "new"  # Safe default
DEFAULT_STRATEGY = "balanced"  # Recommended strategy
```

### Step 3: File Handling

```python
def compile_skill(skill_path, mode="new", strategy="balanced"):
    if mode == "replace":
        # Always create backup first
        create_backup(skill_path)
        # Edit in-place
        edit_skill(skill_path, strategy)
    else:
        # Create new file
        output_path = get_output_path(skill_path, strategy)
        create_compiled_skill(skill_path, output_path, strategy)
```

---

## Usage Examples

### Example 1: Safe Compilation (Default)

```
You: "Compile the TDD skill"

You: I'll optimize this skill.
     Output mode: new, replace, or auto? [new]
     Optimization strategy: aggressive, balanced, or conservative? [balanced]

     [Generates optimized/tdd.md]

You: "Can I see what changed?"
You: [Shows diff between original and optimized]
```

### Example 2: Trusted Replacement

```
You: "Compile the TDD skill, replace mode"

You: I'll optimize this skill in REPLACE mode.
     ⚠️ Original will be backed up as tdd.md.backup
     [Edits tdd.md directly with balanced optimization]

You: "I don't like the result"
You: [Restores from backup]
```

### Example 3: Strategy Experimentation

```
You: "Try all three strategies on TDD"

You: [Generates three files]
     optimized/aggressive/tdd.md (43.5% savings)
     optimized/balanced/tdd.md (15.3% savings)
     optimized/conservative/tdd.md (5% savings)

You: "Show me diffs"
You: [Shows comparison, user chooses balanced]
```

---

## Implementation Changes

### Update SKILL.md

Add to Step 1 (Initial Setup):

```markdown
### 1.1 Collect Decisions

Before proceeding, ask the user:

```
I'll optimize this skill. I need a few details:

1. **Output mode?**
   - new: Create optimized/[skill-name].md (safe, default)
   - replace: Edit original file in-place (with backup)
   - auto: I'll choose for you

2. **Optimization strategy?**
   - aggressive: Max token savings (~40%), may lose explanations
   - balanced: Moderate savings (~15%), keeps key explanations (recommended)
   - conservative: Minimal changes (~5%), very safe

3. **Compare mode?**
   - yes: Show diff between original and optimized
   - no: Just generate the file
```
```

### Add to Step 5: Generate Output

```markdown
### 5.4 Apply Changes (Based on Mode)

**Mode: NEW (default)**
```python
Write("[output-path]/optimized/skill-name.md", optimized_content)
```

**Mode: REPLACE**
```python
# 1. Create backup
backup_path = "[skill].backup"
Write(backup_path, original_content)

# 2. Edit in-place
Edit("[skill-path]", old_content, new_content)

# 3. Document change
Write("[skill-path].changes", change_log)
```

**Mode: COMPARE**
```python
# Generate diff
diff = generate_diff(original, optimized)
print(diff)

# Ask user which to use
user_choice = ask_user("Use optimized version?")
if user_choice == "yes":
    Apply changes...
```
```

---

## Diff Visualization

When compare mode is enabled:

```markdown
## Optimization Preview

### File: TDD Skill

**Strategy:** Balanced (15.3% savings)

### Changes

**Removed:**
```
~~Test-Driven Development (TDD) is a software development process...~~
```

**Modified:**
```diff
- Always write tests before writing code. This is the most fundamental...
+ **Test before code** - Always write tests before implementation
```

**Preserved:**
```
✓ Red-Green-Refactor workflow
✓ Coverage standards
✓ Common mistakes
```

### Token Impact
- Before: 648 tokens
- After: 549 tokens
- Savings: 99 tokens (15.3%)
```

---

## Recommendation

### Default Behavior (Safe First)

```
mode = "new"           # Safe, creates new file
strategy = "balanced"  # Recommended
compare = "auto"       # Show if significant change
```

### User Has Choice

- First time → Use "new" mode
- Confident → Use "replace" mode
- Experimenting → Generate multiple strategies
- Comparing → Use "compare" mode

---

## CLI Examples

```bash
# Default: safe new file
compile_skill tdd.md

# Replace original (with backup)
compile_skill tdd.md --mode replace

# Try specific strategy
compile_skill tdd.md --strategy aggressive

# Generate all variants for comparison
compile_skill tdd.md --all-strategies

# Show diff first
compile_skill tdd.md --compare
```

---

## Conclusion

**Recommendation: Implement hybrid mode**

Reasons:
1. **Safety first** - Default to creating new file
2. **User choice** - Let user decide per compilation
3. **Flexibility** - Support multiple workflows
4. **Experimentation** - Enable strategy comparison
5. **Trust building** - User can switch to replace when confident

**Implementation priority:**
1. Add mode selection to initial questions
2. Implement backup for replace mode
3. Add diff/compare functionality
4. Generate multiple strategies when requested
