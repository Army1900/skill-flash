---
name: skill-compilation
description: Analyze and optimize AI skills by extracting core principles, identifying scriptable rules, and restructuring into efficient three-tier architecture. Reduces token cost and improves execution speed.
---

# Skill Compilation

Optimize AI skills by restructuring them into an efficient three-tier architecture that minimizes token cost while maintaining accuracy.

## Quick Execution Checklist

**Use this checklist to ensure no steps are missed:**

- [ ] 1. Collect initial decisions (platform, goal, output location)
- [ ] 2. Read target skill file using Read tool
- [ ] 3. Detect platform format (use detection table below)
- [ ] 4. Read corresponding platform spec from `specs/platforms/`
- [ ] 5. Extract and count: principles, rules, workflows, decisions, tokens
- [ ] 6. Present analysis summary to user
- [ ] 7. Classify content into Tier 1/2/3
- [ ] 8. Identify scriptable rules
- [ ] 9. Generate Tier 1 principles (<100 tokens)
- [ ] 10. Generate Tier 2 session config
- [ ] 11. Generate Tier 3 simplified skill
- [ ] 12. Generate scripts (reference `specs/code-examples.py`)
- [ ] 13. Batch decision points
- [ ] 14. Write output files to target location
- [ ] 15. **QUALITY CHECK: Read `specs/quality-checklist.md` and verify**
- [ ] 16. Generate and present report

---

## Trigger

Use this skill when:
- User asks to optimize, compile, or improve a skill
- User mentions "skill is too long" or "too many tokens"
- User wants to convert skills between platforms
- User asks to analyze or audit a skill

---

## Step 1: Initial Setup

### 1.1 Collect Decisions (Ask Once)

Before proceeding, ask the user:

```
I'll help you optimize this skill. I need a few details:

1. **Target platform?** (claude, openai, cursor, universal, or auto-detect)
2. **Optimization strategy?**
   - balanced (15% savings, keeps key explanations) ← recommended
   - aggressive (40% savings, may lose explanations)
   - conservative (5% savings, very safe)
3. **Generate all variants?**
   - no: Generate only chosen strategy (default)
   - yes: Generate all three for comparison

4. **Compare with original?**
   - no: Just generate the file
   - yes: Show diff before generating
```

**Note:** If user doesn't specify:
- Strategy: `balanced`
- Variants: `no` (only chosen strategy)
- Compare: `no` (generate directly)

### 1.2 Read Target Skill File

Use the **Read tool** to read the target skill file:

```
Read the skill file at: [user provided path or detected path]
```

Keep the content in context for analysis.

---

## Step 2: Parse and Analyze

### 2.1 Detect Platform Format

Use this table to detect the platform:

| Clues in file | Platform | Spec to read |
|---------------|----------|--------------|
| Starts with `---`, has `name:` in frontmatter | Claude | `specs/platforms/claude.py` |
| JSON format, has `instructions` field | OpenAI | `specs/platforms/openai.py` |
| Filename is `.cursorrules`, line-based rules | Cursor | `specs/platforms/cursor.py` |
| Markdown with `##` sections, no frontmatter | Universal | Use Claude as default |

**Action**: After detecting platform, read the corresponding spec file:
```
Read specs/platforms/[detected-platform].py
```

### 2.2 Extract Structure

From the skill content, extract:

```
✓ Core Principles - Look for sections like "Core Principles", "Guidelines"
  - Markers: "always", "never", "must", fundamental rules

✓ Structured Rules - Look for specific, checkable conditions
  - Markers: "check", "verify", "ensure", specific requirements

✓ Workflows - Look for step-by-step processes
  - Markers: "Step 1", "First", "Then", numbered lists

✓ Decision Points - Look for questions to ask user
  - Markers: "ask user", "confirm", "prompt", "?"

✓ Token Count - Estimate: character count ÷ 4
```

### 2.3 Present Analysis

Show the user this analysis:

```markdown
## 📊 Skill Analysis: [Skill Name]

**Platform**: [detected platform]
**Estimated tokens**: [number] (~[chars] characters ÷ 4)

**Structure**:
- Principles: [count]
- Rules: [count]
- Workflows: [count]
- Decision points: [count]

---

Now identifying optimization opportunities...
```

---

## Step 3: Identify Optimization Opportunities

### 3.1 Classify into Tiers

For each extracted item, classify:

**Tier 1 (Internalized) - System Prompt**
- Criteria: High-frequency, stable, fundamental
- Mark if: Used in >80% of skill invocations
- Target: 3-5 principles, <100 tokens total

**Tier 2 (Session) - Load Once**
- Criteria: Medium-frequency, project-specific
- Mark if: Used in 20-80% of invocations
- Target: Key rules and workflows

**Tier 3 (On-Demand) - Pay Per Use**
- Criteria: Low-frequency, edge cases
- Mark if: Used in <20% of invocations
- Target: Complex scenarios only

### 3.2 Identify Scriptable Rules

Look for rules with these patterns:
- "Check that X"
- "Verify Y"
- "Ensure Z"
- Clear pass/fail condition

For each scriptable rule, note:
- Rule name
- What to check
- Best language (bash for simple checks, python for parsing)
- Reference `specs/code-examples.py` for templates

---

## Step 4: Generate Optimized Output

### 4.1 Tier 1 - Core Principles

Extract top 3-5 principles:

```markdown
## [Skill Name] Principles

- [Principle 1 - keep under 20 words]
- [Principle 2 - keep under 20 words]
- [Principle 3 - keep under 20 words]
- [Principle 4 - keep under 20 words]
- [Principle 5 - keep under 20 words]
```

**Verify**: Total <100 tokens

### 4.2 Tier 2 - Session Configuration

Generate session config:

```yaml
# session-config.yaml
session:
  skills: [skill-name]
  loaded_at: session_start
  reference_mode: true

rules:
  - name: [rule-name]
    description: [brief description]
  - name: [rule-name]
    description: [brief description]

workflows:
  - name: main
    steps:
      - [step 1]
      - [step 2]
      - [step 3]
```

### 4.3 Tier 3 - Simplified Skill

Create streamlined version:

```markdown
---
name: [name]
description: [description]
optimized: true
---

# [Skill Name] (Optimized)

> **Note**: Core principles are embedded in system prompt. This handles edge cases only.

## When to Use

Use this skill when:
- [Complex scenario 1]
- [Complex scenario 2]

## Quick Reference

Core workflow is loaded at session start. Use this for:
- [Edge case 1]
- [Edge case 2]

## Scripts

The following checks run automatically:
- `[script name]` - [purpose]
- `[script name]` - [purpose]
```

### 4.4 Generate Scripts

For each scriptable rule:

1. **Reference** `specs/code-examples.py` for templates
2. **Adapt** to the specific rule and project
3. **Generate** complete, executable script

Example script structure:

```bash
#!/bin/bash
# [script-name].sh - [purpose]
set -e

# [Check logic]
if [condition]; then
    echo "PASS: [message]"
    exit 0
else
    echo "FAIL: [message]"
    exit 1
fi
```

### 4.5 Optimize Decision Points

**Key insight**: Smart defaults eliminate most questions. Optional configuration when needed.

**Speed impact**:
- Sequential questions: N questions = N round-trips
- Smart defaults: 0 questions (usually)
- Optional config: 1 round-trip (when needed)
- Example: 5 questions → 0-1 round-trips = 5-10x faster

#### Step 1: Identify Independent Decisions

Look for questions that:
- Have NO dependency on each other's answers
- Can be asked upfront before execution
- Don't require context from the task
- Have sensible defaults

**Dependency check**:
```
Q1: What framework? (React/Vue/Svelte) → Has default by language
Q2: What state manager for [framework]? ← DEPENDS on Q1, keep in-flow
Q3: What styling approach? (Tailwind/CSS) → Has clear default

Result: Q1 has smart default, Q2 stays in-flow, Q3 has default
```

**Marking patterns**:
- "Ask user: X" with obvious default → Smart default
- "Ask user: X" with dependency → Keep in-flow
- "Confirm: X" → Usually unnecessary, remove or make default

#### Step 2: Extract and Prioritize Decisions

For each decision, categorize:

```yaml
[decision_name]:
  has_smart_default: true/false     # Can we guess well?
  default_value: "sensible choice"  # What works most often?
  user_often_changes: true/false    # Do users frequently customize?
  can_detect_from_context: true/false # Can we auto-detect?
```

**Prioritization**:
1. **Smart defaults** - High-quality defaults, auto-detect when possible
2. **Optional config** - Clear format for when users want to customize
3. **Keep in-flow** - Only decisions that truly depend on task context

**Examples**:
```yaml
testing_framework:
  has_smart_default: true  # Detect from language/file extension
  default_value: "pytest"   # For Python
  can_detect_from_context: true
  → Use smart default

coverage_target:
  has_smart_default: true
  default_value: "80%"
  user_often_changes: false
  → Use smart default, mention in docs

project_name:
  has_smart_default: false
  → Keep as in-flow question
```

#### Step 3: Generate Smart Defaults Format

**Recommended output**:

```markdown
## Configuration

**Smart defaults** (usually work well):
- Framework: auto-detected from your project
- Coverage: 80% (industry standard)
- Mock strategy: mock (faster, isolated)

I'll start with these. To customize, say **"config"** and I'll show options.

---

[Skill proceeds immediately with defaults]

[If user says "config"]

**Configuration options**:

To change settings, provide in ONE message:
```
framework, coverage%, mock_strategy
```

Example: `jest, 90%, real`

Or set individually:
- Framework: pytest, jest, go test, junit
- Coverage: 80%, 90%, 100%
- Mock: mock, real, hybrid

Your config:
```

**Benefits**:
- Zero latency for most users (defaults work)
- Clear escape hatch ("say config")
- One-shot configuration when needed
- No confusion about input format

#### Step 4: Transform Sequential Questions

**Before (original skill)**:
```markdown
## Framework Selection
Ask user: Which testing framework to use?

## Coverage Requirements
Ask user: What is the target coverage percentage?

## Test Style
Ask user: Should we mock dependencies?
```

**After (compiled skill)**:
```markdown
## Configuration

**Smart defaults**:
- Framework: auto-detected (pytest for Python, jest for JS, etc.)
- Coverage: 80%
- Mock: yes (for fast, isolated tests)

I'll use these unless you say otherwise. To customize, say **"config"**.

---

## Core Workflow

[Proceeds immediately - no questions needed]

[Reference the defaults in workflow]
"Using [detected framework] with 80% coverage target..."
```

#### Step 5: Handle Conditional Decisions

Some decisions genuinely depend on context. Keep these in-flow:

```markdown
## Smart Defaults (Independent)
- Framework: auto-detected
- Test style: unit by default

[Skill starts work]

## Runtime Decisions (Dependent)
When context emerges, ask naturally:

"Writing integration tests. Should I use a real database or sqlite?"
"Detected Django. Use pytest-django or plain pytest?"
```

**Rule of thumb**:
- Can be guessed/detected → Smart default
- User often customizes → Optional config ("say config")
- Truly task-specific → Ask naturally when relevant

#### Quality Check for Optimized Decisions

After generating, verify:

- [ ] All guessable decisions have smart defaults
- [ ] Common customization path is clear ("say config")
- [ ] Input format is simple and unambiguous
- [ ] No questions that could be answered by context
- [ ] Conditional decisions stay in-flow where they belong
- Writing test-driven code (uses framework from config)
- Analyzing coverage (uses target from config)
- Setting up test structure (uses mock strategy from config)
```

#### Quality Check for Batched Decisions

After generating, verify:

- [ ] All independent decisions are in the initial section
- [ ] No questions remain in the workflow body (unless truly conditional)
- [ ] Defaults are provided for all non-critical decisions
- [ ] Format is clear and easy to respond to
- [ ] Dependencies are properly separated (conditional decisions stay in-flow)

---

## Step 5: Write Output Files

### 5.1 Folder Naming Convention

**Skills are folders, not files. Create new folder for compiled variant:**

```
skills/
├── tdd/                    ← Original skill folder
│   ├── SKILL.md
│   ├── scripts/
│   └── examples/
│
├── tdd-balanced/           ← Compiled (recommended)
│   ├── SKILL.md          ← Optimized content
│   ├── scripts/          ← Generated scripts
│   └── examples/         ← Simplified examples
│
└── tdd-aggressive/         ← Alternative strategy
    ├── SKILL.md
    └── scripts/
```

**User workflow:**
```bash
# Compare versions
diff skills/tdd/SKILL.md skills/tdd-balanced/SKILL.md

# Use compiled version
cp -r skills/tdd-balanced/* skills/tdd/

# Or switch to compiled folder
cd skills/tdd-balanced/
```

### 5.2 Output Structure

Based on target platform and user choices:

**Single file output (if not generating all variants):**

**Claude:**
```
[same-directory-as-original]/
├── tdd.balanced.md          # Optimized skill (main output)
├── tdd.balanced.session.yaml # Session config
├── tdd.balanced.scripts/     # Generated scripts
└── tdd.report.md             # Compilation report
```

**All variants (if user requested):**

```
[same-directory-as-original]/
├── tdd.balanced.md
├── tdd.aggressive.md
├── tdd.conservative.md
└── tdd.report.md             # Comparison of all variants
```

### 5.3 Write Files

Use **Write tool** to create each file:

```python
# Example: Write Tier 1
Write("[output-dir]/CLAUDE.md.fragment", tier1_content)

# Example: Write session config
Write("[output-dir]/session-config.yaml", tier2_content)

# Example: Write scripts
Write("[output-dir]/scripts/check_coverage.sh", script_content)
```

---

## Step 6: Generate Report

Create comprehensive report:

```markdown
# 📦 Compilation Report

## Summary
- **Skill**: [name]
- **Platform**: [platform]
- **Original tokens**: [number]
- **Optimized tokens**: [number]
- **Savings**: [percentage]%

## Token Breakdown

| Tier | Original | Optimized | Savings |
|------|----------|-----------|---------|
| Tier 1 (per use) | [tokens] | 0 | 100% |
| Tier 2 (session) | [tokens] | [tokens] | [%] |
| Tier 3 (on-demand) | [tokens] | [tokens] | [%] |
| **Total** | **[tokens]** | **[tokens]** | **[%]** |

## Scripts Generated
- ✓ `[script1]` - [purpose]
- ✓ `[script2]` - [purpose]

## Changes Made
- Extracted [N] core principles to Tier 1
- Identified [N] scriptable rules
- Batched [N] decision points
- Simplified skill file by [N]%

## Next Steps
1. Add `CLAUDE.md.fragment` content to your project's CLAUDE.md
2. Load `session-config.yaml` at session start
3. Place scripts in your project's scripts directory
4. Use optimized `SKILL.md` for edge cases

## Files Created
[List all generated files with brief descriptions]

## Quality Assurance

**CRITICAL**: Before declaring completion, verify the optimized skill maintains equivalent functionality.

### 7.1 Coverage Check

Verify no important content was lost:

| Original Content | Optimized Location | Status |
|------------------|-------------------|--------|
| [Principle 1] | Tier 1 / CLAUDE.md.fragment | ✅/❌ |
| [Principle 2] | Tier 1 / CLAUDE.md.fragment | ✅/❌ |
| [Rule 1] | Tier 2 session config | ✅/❌ |
| [Rule 2] | Tier 2 session config | ✅/❌ |
| [Workflow Step 1] | Tier 3 SKILL.md | ✅/❌ |
| [Workflow Step 2] | Tier 3 SKILL.md | ✅/❌ |

**Action**: Create this table and verify every important item has a location.

### 7.2 Equivalence Test

Test key scenarios to ensure behavior is preserved:

```
Scenario 1: [Common use case]
  Original skill would: [expected behavior]
  Optimized skill should: [same behavior]
  Result: ✅ Pass / ❌ Fail

Scenario 2: [Edge case]
  Original skill would: [expected behavior]
  Optimized skill should: [same behavior]
  Result: ✅ Pass / ❌ Fail

Scenario 3: [Error condition]
  Original skill would: [expected behavior]
  Optimized skill should: [same behavior]
  Result: ✅ Pass / ❌ Fail
```

**Minimum 3 scenarios** - include common, edge, and error cases.

### 7.3 Script Validation

For each generated script:

| Script | Test Command | Expected | Actual | Status |
|--------|-------------|----------|--------|--------|
| check_coverage.sh | pytest --cov | PASS on good code | | ✅/❌ |
| check_secrets.sh | echo "password=123" | FAIL | | ✅/❌ |
| validate_tests.py | missing test file | FAIL | | ✅/❌ |

**Action**: Describe how to test each script. Scripts must be verifiable.

### 7.4 Token Accuracy Verification

Verify token calculations are correct:

```
Original skill: [X] characters ÷ 4 = [Y] tokens
Tier 1 fragment: [A] characters ÷ 4 = [B] tokens
Tier 2 config: [C] characters ÷ 4 = [D] tokens
Tier 3 skill: [E] characters ÷ 4 = [F] tokens
Scripts: [G] characters ÷ 4 = [H] tokens

Per invocation cost:
  Original: [Y] tokens
  Optimized: [D] + [F] = [J] tokens (Tier 1 is free)
  Savings: [Y - J] tokens = [%]%
```

**Action**: Recalculate and verify.

### 7.5 Regression Prevention

Create safety net for user:

```markdown
## Rollback Plan

If the optimized skill doesn't work as expected:

1. **Immediate rollback**: Delete optimized files, use original
2. **Location of original**: [path to backup or original]
3. **What to keep**: Even if rollback, you can keep Tier 1 in CLAUDE.md

**Backup created at**: [location]
**Original skill preserved at**: [location]
```

**Action**: Always preserve original skill file.

### 7.6 User Validation Checklist

Before finalizing, ask user to verify:

```markdown
## Please Verify

I've generated an optimized version of your skill. Please confirm:

- [ ] Core principles are accurately captured in Tier 1
- [ ] Key workflows are preserved in Tier 2/3
- [ ] No critical information appears to be lost
- [ ] Scripts look reasonable for your environment
- [ ] Token savings are acceptable

Would you like me to:
1. Adjust anything before finalizing?
2. Explain any changes in more detail?
3. Proceed with the optimized version?
```

**Action**: Present to user and wait for confirmation.

### 7.7 Failure Criteria

**Compilation FAILS quality check if:**

- ❌ Any core principle is missing
- ❌ Critical workflow steps are lost
- ❌ Scripts have obvious bugs
- ❌ Token savings < 10% (not worth the risk)
- ❌ User identifies missing functionality

**If quality check fails:**
1. Identify what's missing
2. Add it back to appropriate tier
3. Re-run verification
4. Update report

---

## Reference Files (Read as Needed)

| File | When to Read |
|------|--------------|
| `specs/platforms/claude.py` | Parsing Claude format skills |
| `specs/platforms/openai.py` | Parsing OpenAI GPTs |
| `specs/platforms/cursor.py` | Parsing .cursorrules |
| `specs/code-examples.py` | Generating scripts |
| `specs/quality-checklist.md` | **CRITICAL: Quality assurance procedures** |
| `references/platform-formats.md` | Understanding platform formats |
| `references/optimization-patterns.md` | Optimization techniques |
| `templates/` | Output format templates |

---

## Verification Checklist

Before completing, verify:

**Content Completeness:**
- [ ] All core principles extracted to Tier 1
- [ ] All important rules have a location (Tier 1/2/3)
- [ ] All workflow steps are preserved
- [ ] No critical information is missing

**Optimization Quality:**
- [ ] Tier 1 is <100 tokens
- [ ] Scriptable rules converted to executable code
- [ ] Decision points batched into single collection
- [ ] Token reduction is >10% (otherwise not worth it)

**Technical Correctness:**
- [ ] Token calculations are accurate
- [ ] Scripts are syntactically correct
- [ ] Output format matches target platform specification
- [ ] Scripts have clear test commands

**Safety:**
- [ ] Original skill file is preserved
- [ ] Rollback plan is documented
- [ ] Backup location is specified

**Delivery:**
- [ ] All files written to output location
- [ ] Report is comprehensive and accurate
- [ ] User has clear next steps
- [ ] Quality assurance tests documented

---

## Example Execution Flow

**User**: "Optimize the TDD skill at ~/.claude/plugins/tdd/SKILL.md"

**You**:
1. ✅ Ask: Target platform, goal, output location
2. ✅ Read: `~/.claude/plugins/tdd/SKILL.md`
3. ✅ Detect: Claude format
4. ✅ Read: `specs/platforms/claude.py` for reference
5. ✅ Extract: principles, rules, workflows, decisions
6. ✅ Present: Analysis summary
7. ✅ Classify: Tier 1/2/3
8. ✅ Identify: 3 scriptable rules
9. ✅ Generate: Tier 1 (5 principles, 60 tokens)
10. ✅ Generate: Tier 2 session config
11. ✅ Generate: Tier 3 simplified skill
12. ✅ Generate: 3 scripts (reference code-examples.py)
13. ✅ Batch: 2 decision points
14. ✅ Write: All files to output directory
15. ✅ **QUALITY CHECK**: Run coverage check, equivalence tests
16. ✅ **USER VALIDATION**: Ask user to verify changes
17. ✅ Present: Final report with quality metrics

---

## Common Patterns (Quick Reference)

**When you see...** → **Do this...**

"Always write tests before code" → Extract to Tier 1

"Check test coverage is at least 80%" → Generate bash script

"Ask user: What framework?" → Batch with other questions

"Verify no hardcoded secrets" → Generate git grep script

"Follow these 10 steps..." → Keep in Tier 3, simplify description
