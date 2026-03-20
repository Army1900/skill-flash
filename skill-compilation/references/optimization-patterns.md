# Optimization Patterns

Common patterns and techniques for optimizing AI skills.

## Pattern 1: Principle Extraction

### Before (500 tokens)
```
You must always write tests before writing code. This is called
Test-Driven Development (TDD). The cycle is: write a failing test,
write the minimum code to make it pass, refactor. Repeat this for
every feature. Never skip tests...
```

### After (50 tokens - in CLAUDE.md)
```markdown
## TDD
- Test before code
- Red → Green → Refactor
```

**Savings**: 450 tokens per session

---

## Pattern 2: Decision Batching

### Before
```
→ What framework?
→ [User answers]
→ What state management?
→ [User answers]
→ What styling?
→ [User answers]
```

### After (YAML)
```yaml
initial_questions:
  - framework: [React, Vue, Svelte]
    default: React
  - state_management: [Redux, Zustand, Context]
    default: Context
  - styling: [CSS, Tailwind, Styled Components]
    default: Tailwind

# Collect all at once, then execute
```

**Savings**: Reduces interaction overhead by 60%

---

## Pattern 3: Scriptable Rules

### Before (descriptive)
```
Check that test coverage is at least 80% before committing.
If it's lower, stop and add more tests.
```

### After (executable)
```bash
#!/bin/bash
# scripts/check_coverage.sh
COVERAGE=$(pytest --cov --cov-report=term | grep TOTAL | awk '{print $4}' | sed 's/%//')
if [ "$COVERAGE" -lt 80 ]; then
    echo "Coverage ${COVERAGE}% < 80%. Add more tests."
    exit 1
fi
echo "Coverage ${COVERAGE}% ✓"
```

**Benefits**:
- Deterministic (same result every time)
- Faster (no LLM interpretation)
- Testable independently

---

## Pattern 4: Structured Declarations

### Before (prose)
```
Make sure the code follows these security best practices:
1. Don't hardcode passwords
2. Use parameterized queries
3. Validate all inputs
4. Keep dependencies updated
```

### After (structured)
```yaml
rules:
  - name: no_secrets
    check: "grep -ri 'password\|api_key' {src_dir}"
    fail: "Potential secrets found"
    fix: "Use environment variables"

  - name: sql_injection
    check: "grep -ri \"SELECT.*$.*FROM\" {src_dir}"
    fail: "Potential SQL injection"
    fix: "Use parameterized queries"

  - name: input_validation
    check: "bandit -r {src_dir}"
    fail: "Security issues detected"
```

**Benefits**:
- Machine-readable
- Can generate fix suggestions
- Integrates with CI/CD

---

## Pattern 5: Hybrid Execution

```
┌─────────────────────────────────────┐
│  Task: Code Review                   │
└──────────┬──────────────────────────┘
           │
           ▼
┌──────────────────────┐
│  Script Layer        │
│  - Run linter        │ ← Deterministic, fast
│  - Check coverage    │
│  - Scan for secrets  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  AI Layer            │
│  - Analyze patterns  │ ← Complex judgment
│  - Suggest refactor  │
│  - Review logic      │
└──────────────────────┘
```

**Result**: Best of both worlds - speed + intelligence

---

## When to Use Each Pattern

| Pattern | Use When | Example |
|---------|----------|---------|
| Principle Extraction | High-frequency rules | TDD, Git workflow |
| Decision Batching | Multiple user inputs | Framework selection |
| Scriptable Rules | Clear pass/fail checks | Coverage, linting |
| Structured Declarations | Configurable rules | Security policies |
| Hybrid Execution | Mixed deterministic/complex | Code review |

---

## ROI Calculator

```python
# Estimate optimization benefit

def calculate_roi(
    skill_tokens: int,
    daily_invocations: int,
    principle_extraction: bool = True,
    scriptable_rules: int = 0
) -> dict:
    """
    Calculate return on investment for skill compilation.

    Args:
        skill_tokens: Original skill token count
        daily_invocations: How often skill is used per day
        principle_extraction: Whether Tier 1 optimization applies
        scriptable_rules: Number of rules that can be scripted

    Returns:
        Token savings and cost reduction estimates
    """
    tier1_savings = skill_tokens * 0.4 if principle_extraction else 0
    script_savings = scriptable_rules * 50  # ~50 tokens per rule

    per_use_savings = tier1_savings + script_savings
    daily_savings = per_use_savings * daily_invocations
    monthly_savings = daily_savings * 30

    return {
        "per_use_savings": per_use_savings,
        "daily_savings": daily_savings,
        "monthly_savings": monthly_savings,
        "payback_period": "1 week" if monthly_savings > 1000 else "1 month"
    }

# Example
calculate_roi(
    skill_tokens=1200,
    daily_invocations=10,
    principle_extraction=True,
    scriptable_rules=5
)
# → monthly_savings: 180,000 tokens
```
