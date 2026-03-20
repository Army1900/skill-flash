# Verification Report Example

Example output from the skill optimization verification tool.

## Command

```bash
python verification/verify.py \
  skill-compilation/examples/original/tdd/SKILL.md \
  skill-compilation/examples/optimized/tdd/SKILL.md
```

## Output

```json
{
  "verification_date": "2025-01-15T10:30:00Z",
  "original_path": "skill-compilation/examples/original/tdd/SKILL.md",
  "optimized_path": "skill-compilation/examples/optimized/tdd/SKILL.md",

  "scores": {
    "functional_completeness": {
      "principles": {
        "original": 5,
        "optimized": 5,
        "coverage": 100.0,
        "score": 20.0
      },
      "rules": {
        "original": 8,
        "optimized": 7,
        "coverage": 87.5,
        "score": 17.5
      },
      "workflows": {
        "original": 3,
        "optimized": 3,
        "coverage": 100.0,
        "score": 20.0
      },
      "decisions": {
        "original": 2,
        "optimized": 2,
        "coverage": 100.0,
        "score": 20.0
      },
      "total": 77.5,
      "max": 80
    },

    "token_efficiency": {
      "token_reduction": {
        "original_per_session": 12000,
        "optimized_per_session": 2400,
        "savings": 9600,
        "percentage": 80.0,
        "score": 15.0
      },
      "efficiency_ratio": {
        "original_density": 26.67,
        "optimized_density": 8.0,
        "ratio": 3.33,
        "score": 15.0
      },
      "total": 30.0,
      "max": 30
    },

    "safety": {
      "backup": {
        "exists": true,
        "score": 5
      },
      "rollback": {
        "exists": true,
        "score": 5
      },
      "total": 10,
      "max": 10
    }
  },

  "overall": {
    "total": 117.5,
    "max": 120,
    "percentage": 97.9,
    "status": "PASSED"
  },

  "recommendations": [
    "✅ Optimization is safe to deploy",
    "Excellent token savings (80% reduction)",
    "All core functionality preserved",
    "Safety measures in place"
  ]
}
```

## Interpretation

### Status: PASSED ✅

The optimization has achieved a score of 97.9/100, which exceeds the minimum threshold of 80/100.

### Breakdown

| Dimension | Score | Max | Percentage |
|-----------|-------|-----|------------|
| Functional Completeness | 77.5 | 80 | 96.9% |
| Token Efficiency | 30.0 | 30 | 100% |
| Safety | 10 | 10 | 100% |

### Key Metrics

**Token Savings:**
- Per session: 9,600 tokens saved
- Percentage: 80% reduction
- Break-even: Optimization pays for itself after 1 use

**Content Coverage:**
- Principles: 100% (5/5 preserved)
- Rules: 87.5% (7/8 preserved)
- Workflows: 100% (3/3 preserved)
- Decisions: 100% (2/2 preserved)

**Safety:**
- Backup created: ✅
- Rollback documented: ✅

---

## Example: FAILED Optimization

```json
{
  "overall": {
    "total": 52,
    "max": 120,
    "percentage": 43.3,
    "status": "FAILED"
  },

  "recommendations": [
    "❌ Optimization failed quality checks",
    "Significant content may be missing - only 60% coverage",
    "Token savings are minimal (15% reduction)",
    "Consider re-optimizing with different parameters"
  ]
}
```

---

## Example: NEEDS_REVIEW Optimization

```json
{
  "overall": {
    "total": 68,
    "max": 120,
    "percentage": 56.7,
    "status": "NEEDS_REVIEW"
  },

  "recommendations": [
    "⚠️ Review optimization with user before deploying",
    "Good token savings (65% reduction)",
    "One rule may be missing from optimized version",
    "Verify that missing content is intentional"
  ]
}
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Verify Skill Optimization

on:
  pull_request:
    paths:
      - 'skills/**/SKILL.md'

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Run verification
        id: verify
        run: |
          python verification/verify.py \
            skills/original/tdd/SKILL.md \
            skills/optimized/tdd/SKILL.md \
            > verification_result.json

      - name: Check status
        run: |
          STATUS=$(jq -r '.overall.status' verification_result.json)
          SCORE=$(jq '.overall.percentage' verification_result.json)

          echo "Verification Status: $STATUS"
          echo "Score: $SCORE%"

          if [ "$STATUS" != "PASSED" ]; then
            echo "❌ Skill optimization verification failed"
            jq '.recommendations' verification_result.json
            exit 1
          fi

          echo "✅ Skill optimization verified"

      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const result = JSON.parse(fs.readFileSync('verification_result.json', 'utf8'));

            const comment = `## Skill Optimization Verification

            **Status**: ${result.overall.status}
            **Score**: ${result.overall.percentage.toFixed(1)}%

            ### Breakdown
            - Functional Completeness: ${result.scores.functional_completeness.total}/${result.scores.functional_completeness.max}
            - Token Efficiency: ${result.scores.token_efficiency.total}/${result.scores.token_efficiency.max}
            - Safety: ${result.scores.safety.total}/${result.scores.safety.max}

            ### Recommendations
            ${result.recommendations.map(r => '- ' + r).join('\n')}
            `;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

---

## Test Case Development Guide

When creating test cases for a skill:

### 1. Identify Core Scenarios

What are the main use cases for this skill?

```yaml
scenarios:
  - common_usage: "Most frequent invocation"
  - edge_case: "Unusual but valid situation"
  - error_handling: "When something goes wrong"
```

### 2. Define Expected Behavior

For each scenario, define:

```json
{
  "input": "What the user says/does",
  "expected_output": {
    "must_contain": ["required keywords"],
    "must_not_contain": ["forbidden keywords"],
    "expected_action": "what should happen"
  }
}
```

### 3. Validate Against Original

Run the test against the original skill first to establish baseline.

### 4. Compare with Optimized

Run the same test against optimized skill and compare.

---

## Running Verification

### Basic Usage

```bash
# Verify an optimized skill
python verification/verify.py original/SKILL.md optimized/SKILL.md
```

### With Test Cases

```bash
# Use custom test cases
python verification/verify.py \
  original/SKILL.md \
  optimized/SKILL.md \
  test_cases.json
```

### Batch Verification

```bash
# Verify all optimized skills in a directory
for skill in skills/optimized/*/SKILL.md; do
  original=${skill/optimized/original}
  python verification/verify.py "$original" "$skill"
done
```
