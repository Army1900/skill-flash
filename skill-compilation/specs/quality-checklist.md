# Quality Assurance for Skill Compilation

This document provides detailed quality assurance procedures for skill compilation.

## Core Principle

> **Better to be conservative than aggressive.** If in doubt, keep more content rather than less. Token savings are not worth functionality loss.

## Quality Metrics

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| Token savings | >10% | Below this, risk outweighs benefit |
| Content coverage | 100% | All important content must be preserved |
| Principle accuracy | 100% | Core principles must be exact |
| Script testability | 100% | Every script must have a test |

---

## 1. Coverage Matrix Template

Use this template to ensure all content is accounted for:

```markdown
### Content Coverage

| Original Section | Type | Optimized Location | Verified |
|------------------|------|-------------------|----------|
| "Core Principles" | Principles | Tier 1: CLAUDE.md.fragment | ☐ |
| "Always write tests first" | Principle | Tier 1, line 3 | ☐ |
| "Check coverage >80%" | Rule | Script: check_coverage.sh | ☐ |
| "Step 1: Write test" | Workflow | Tier 3, Workflow section | ☐ |
| "Ask: What framework?" | Decision | Tier 2, decisions block | ☐ |

**Coverage**: X/Y items (Z%)
**Gaps**: [list any missing items]
```

**Rules:**
- Every row must have a location
- If something doesn't fit, note it as "PRESERVE IN TIER 3"
- Get to 100% coverage before declaring done

---

## 2. Equivalence Test Scenarios

### Minimum Test Set

For each skill compilation, define at least 3 test scenarios:

#### Scenario 1: Common Path
```
Input: [Typical user request]
Original behavior: [What original skill does]
Optimized behavior: [What optimized skill should do]
Test: How to verify
Status: ☐ Pass / ☐ Fail
```

#### Scenario 2: Edge Case
```
Input: [Unusual but valid request]
Original behavior: [What original skill does]
Optimized behavior: [What optimized skill should do]
Test: How to verify
Status: ☐ Pass / ☐ Fail
```

#### Scenario 3: Error Condition
```
Input: [Invalid input or error state]
Original behavior: [How original skill handles it]
Optimized behavior: [How optimized skill should handle it]
Test: How to verify
Status: ☐ Pass / ☐ Fail
```

### Example: TDD Skill

| Scenario | Input | Original | Optimized | Test |
|----------|-------|----------|-----------|------|
| Common | "Add a new feature" | Writes test first, then code | Same | Run workflow |
| Edge | "Add feature with external API" | Suggests mocking | Same | Check Tier 3 |
| Error | "Tests fail" | Stops, doesn't write code | Same | Check logic |

---

## 3. Script Validation Checklist

For each generated script:

### Syntactic Correctness
```bash
# Bash scripts
[ ] Has shebang (#!/bin/bash)
[ ] Has set -e for error handling
[ ] Variables are quoted
[ ] Exit codes are explicit (0 for success, 1 for failure)

# Python scripts
[ ] Has shebang (#!/usr/bin/env python3)
[ ] Has if __name__ == "__main__"
[ ] Uses sys.exit() with proper codes
[ ] Handles errors gracefully
```

### Functional Correctness
```bash
# Test command: [command to run script]
# Expected output: PASS/FAIL message
# Expected exit code: 0 for pass, 1 for fail

[ ] Test command defined
[ ] Expected output specified
[ ] Edge cases considered
[ ] Dependencies documented
```

### Documentation
```bash
[ ] Has comment explaining purpose
[ ] Has usage instructions if takes arguments
[ ] Error messages are clear
[ ] References original rule
```

---

## 4. Token Calculation Verification

### Formula

```
Token Estimate = Character Count ÷ 4

Per-Invocation Cost:
  Original = Tier 1 + Tier 2 + Tier 3
  Optimized = Tier 2 + Tier 3 (Tier 1 is in system prompt)

Session Savings (N invocations):
  Total Original = N × (Tier 1 + Tier 2 + Tier 3)
  Total Optimized = Tier 1 + N × (Tier 2 + Tier 3)
  Savings = Total Original - Total Optimized
```

### Verification Steps

1. **Count characters** in each generated file
2. **Divide by 4** for token estimate
3. **Calculate per-invocation cost**
4. **Calculate session savings** (assume N=10 for example)
5. **Verify >10% savings**

### Example Calculation

```
Original: 5000 chars = 1250 tokens

Optimized:
  Tier 1: 400 chars = 100 tokens (one-time, in system prompt)
  Tier 2: 600 chars = 150 tokens
  Tier 3: 800 chars = 200 tokens

Per invocation:
  Original: 1250 tokens
  Optimized: 150 + 200 = 350 tokens
  Savings: 900 tokens (72%)

Session (10 invocations):
  Original: 10 × 1250 = 12,500 tokens
  Optimized: 100 + 10 × 350 = 3,600 tokens
  Savings: 8,900 tokens (71%)
```

---

## 5. Rollback Procedure

### Backup Strategy

```bash
# Before optimization
cp SKILL.md SKILL.md.backup
cp SKILL.md SKILL.md.original-$(date +%Y%m%d)

# After optimization (if user approves)
# Keep backup for at least 30 days
```

### Rollback Steps

If user reports issues:

1. **Immediate**: Restore from backup
   ```bash
   cp SKILL.md.backup SKILL.md
   ```

2. **Diagnose**: What functionality was lost?
   - Review coverage matrix
   - Check test scenarios
   - Identify missing content

3. **Fix**: Add missing content to appropriate tier
4. **Retest**: Run quality checks again
5. **Redeploy**: Present fixed version to user

### What to Keep Even on Rollback

Even if the optimized version is rejected, some improvements can be kept:

- ✅ Tier 1 principles in CLAUDE.md (safe to keep)
- ✅ Scripts that work correctly (can be used independently)
- ❌ Tier 3 simplified skill (use original)

---

## 6. Red Flags

**Stop and reconsider if:**

- 🚩 Token savings < 10% → Not worth the risk
- 🚩 Can't locate important content → May be lost
- 🚩 Scripts are complex → Could have bugs
- 🚩 User questions the accuracy → Verify thoroughly
- 🚩 Skill has < 500 tokens → Too small to optimize

**When in doubt, keep more content.**

---

## 7. User Validation Questions

Before finalizing, ask the user:

```
I've optimized your skill with [X]% token savings.

Please verify these key points:

1. Core Principles
   - [Original principle 1] → Now in CLAUDE.md
   - [Original principle 2] → Now in CLAUDE.md
   Are these accurate? ☐ Yes ☐ Needs changes

2. Key Rules
   - [Important rule 1] → Now in session config / script
   - [Important rule 2] → Now in session config / script
   Are these preserved? ☐ Yes ☐ Needs changes

3. Workflows
   - The main workflow steps are in Tier 3
   Is anything missing? ☐ No ☐ Yes (what?)

Would you like me to:
- Adjust anything?
- Explain any changes?
- Proceed with this version?
```

---

## 8. Final Quality Gate

**All must be ✅ before declaring success:**

- [ ] Coverage matrix: 100% of important content located
- [ ] Equivalence tests: All 3+ scenarios pass
- [ ] Scripts: All syntactically correct and testable
- [ ] Token math: Calculations verified, >10% savings
- [ ] Backup: Original skill preserved
- [ ] User approval: User has verified and accepted changes

**If any ❌:**
1. Identify issue
2. Fix it
3. Re-run affected checks
4. Get user approval again

---

## 9. Common Quality Issues

| Issue | Symptom | Fix |
|-------|---------|-----|
| Missing principle | User says "this used to be here" | Add to Tier 1 |
| Vague workflow | Steps unclear | Expand in Tier 3 |
| Broken script | Syntax error | Fix and retest |
| Low savings | <10% tokens | Don't compile, or be more aggressive |
| Confusion | User doesn't understand changes | Better documentation |

---

## 10. Continuous Improvement

After each compilation, note:

1. **What worked well** - Patterns to repeat
2. **What failed** - Patterns to avoid
3. **User feedback** - What users care about
4. **Token reality** - Estimated vs actual savings

Use this to improve future compilations.
