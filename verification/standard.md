# Skill Optimization Verification Standard

Automated, quantifiable verification framework for comparing skills before and after optimization.

## Overview

This standard provides automated metrics to verify that optimized skills maintain or improve quality while reducing cost.

## Verification Dimensions

```
┌─────────────────────────────────────────────────────────────┐
│  Quality Dimensions                                          │
│  1. Functional Completeness (40%) - Does it still work?      │
│  2. Token Efficiency (30%) - Is it cheaper?                 │
│  3. Execution Quality (20%) - Does it work better?          │
│  4. Safety (10%) - Is it safe to deploy?                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. Functional Completeness (40 points)

Verify the optimized skill preserves all essential functionality.

### 1.1 Content Coverage (20 points)

**Automated check:**

```python
def calculate_content_coverage(original_skill, optimized_skill):
    """
    Calculate how much original content is preserved.

    Returns:
        coverage_score: 0-20 points
    """
    # Extract key elements from both
    original_elements = extract_key_elements(original_skill)
    optimized_elements = extract_key_elements(optimized_skill)

    # Calculate coverage
    coverage = len(optimized_elements) / len(original_elements)

    # Score: 20 points * coverage
    return coverage * 20
```

**Key elements to extract:**
- Core principles (keywords: "always", "never", "must")
- Rules (statements starting with verbs)
- Workflows (numbered steps or sequences)
- Decision points (questions, "ask user")

**Scoring:**
```
Coverage ≥ 95%  → 20 points (excellent)
Coverage ≥ 85%  → 17 points (good)
Coverage ≥ 70%  → 14 points (acceptable)
Coverage < 70%  → 0 points (failed)
```

### 1.2 Equivalence Testing (20 points)

**Automated check using test cases:**

```python
def run_equivalence_tests(original_skill, optimized_skill, test_cases):
    """
    Run test cases on both skills and compare outputs.

    test_cases: List of (input, expected_behavior) tuples
    """
    results = {
        'passed': 0,
        'failed': 0,
        'inconsistent': 0
    }

    for input_scenario, expected in test_cases:
        original_output = simulate_skill(original_skill, input_scenario)
        optimized_output = simulate_skill(optimized_skill, input_scenario)

        # Compare outputs
        if outputs_equivalent(original_output, optimized_output):
            results['passed'] += 1
        elif original_output == expected:
            results['inconsistent'] += 1  # Only optimized is wrong
        else:
            results['failed'] += 1

    # Score: 20 points * (passed / total)
    return (results['passed'] / len(test_cases)) * 20
```

**Standard test cases per skill type:**

```yaml
# For TDD skill
test_cases:
  - input: "Add a new feature"
    expected_mentions: ["test", "before implementation"]
  - input: "Tests are failing"
    expected_action: "stop writing code"
  - input: "Coverage check"
    expected_threshold: "80%"

# For code review skill
test_cases:
  - input: "Review this PR"
    expected_checks: ["security", "style", "logic"]
  - input: "Found a bug"
    expected_action: "report issue"
```

**Scoring:**
```
100% pass  → 20 points
≥ 80% pass  → 16 points
≥ 60% pass  → 12 points
< 60% pass  → 0 points (failed)
```

---

## 2. Token Efficiency (30 points)

Verify the optimization actually reduces token cost.

### 2.1 Token Reduction (15 points)

```python
def calculate_token_reduction(original_tokens, optimized_tokens, session_usage):
    """
    Calculate token savings based on usage pattern.

    session_usage: Expected number of skill invocations per session
    """
    # Original cost per session
    original_session_cost = original_tokens * session_usage

    # Optimized cost (Tier 1 is free after first load)
    optimized_session_cost = optimized_tokens['tier1'] + \
                           (optimized_tokens['tier2'] + optimized_tokens['tier3']) * session_usage

    # Calculate reduction
    if original_session_cost == 0:
        return 0

    reduction = (original_session_cost - optimized_session_cost) / original_session_cost

    # Score: 15 points if reduction ≥ 50%
    return min(15, reduction * 30)
```

**Scoring:**
```
Reduction ≥ 70%  → 15 points (excellent)
Reduction ≥ 50%  → 12 points (good)
Reduction ≥ 30%  → 9 points (acceptable)
Reduction < 30%  → 0 points (failed - not worth it)
```

### 2.2 Efficiency Ratio (15 points)

```python
def calculate_efficiency_ratio(original_content, optimized_content):
    """
    Calculate information density (tokens per key concept).
    """
    original_concepts = count_key_concepts(original_content)
    optimized_concepts = count_key_concepts(optimized_content)

    original_density = len(original_content) / original_concepts
    optimized_density = len(optimized_content) / optimized_concepts

    # Ratio: how much more dense is the optimized version
    ratio = original_density / optimized_density

    # Score: 15 points for ≥ 2x density
    return min(15, ratio * 7.5)
```

**Scoring:**
```
Density ≥ 3x   → 15 points (excellent)
Density ≥ 2x   → 12 points (good)
Density ≥ 1.5x → 9 points (acceptable)
Density < 1.5x → 0 points (failed)
```

---

## 3. Execution Quality (20 points)

Verify the optimized skill executes better.

### 3.1 Response Time (10 points)

```python
def measure_response_time(skill, test_scenarios):
    """
    Measure how quickly the skill produces results.
    """
    times = []

    for scenario in test_scenarios:
        start = time.time()
        result = execute_skill(skill, scenario)
        end = time.time()
        times.append(end - start)

    avg_time = sum(times) / len(times)

    # Score based on improvement
    # Baseline: original skill average time
    # Target: at least 20% faster
```

**Scoring (if applicable):**
```
≥ 50% faster  → 10 points
≥ 30% faster  → 8 points
≥ 10% faster  → 6 points
No change     → 3 points
Slower        → 0 points
```

**Note:** For skills that don't "execute" in traditional sense, use:
- Time to parse and understand the skill
- Number of clarification questions needed

### 3.2 Determinism (10 points)

```python
def calculate_determinism(skill, test_cases):
    """
    Measure how consistently the skill produces the same output.
    """
    results = []

    for _ in range(5):  # Run 5 times
        for test_case in test_cases:
            result = execute_skill(skill, test_case)
            results.append(result)

    # Calculate consistency
    unique_results = len(set(results))
    total_results = len(results)

    consistency = 1 - (unique_results / total_results)

    # Score: 10 points for 100% consistent
    return consistency * 10
```

**Scoring:**
```
100% consistent  → 10 points
≥ 80% consistent  → 8 points
≥ 60% consistent  → 6 points
< 60% consistent  → 0 points
```

---

## 4. Safety (10 points)

Verify the optimization is safe to deploy.

### 4.1 Backup Verification (5 points)

```python
def check_backup_exists(optimized_skill):
    """
    Verify original skill is backed up.
    """
    backup_path = get_backup_path(optimized_skill)

    if path_exists(backup_path):
        # Verify backup is identical to original
        if files_identical(backup_path, original_skill):
            return 5  # Full points
        else:
            return 2  # Partial points (backup exists but wrong)
    else:
        return 0  # Failed
```

### 4.2 Rollback Capability (5 points)

```python
def check_rollback_capability(integration_record):
    """
    Verify rollback instructions exist and are valid.
    """
    record = read_integration_record(integration_record)

    checks = {
        'has_backup': record.get('backup_path') is not None,
        'has_instructions': record.get('rollback_steps') is not None,
        'backup_tested': test_backup_restore(record['backup_path'])
    }

    return sum(checks.values()) * (5 / len(checks))
```

---

## Overall Scoring

```python
def calculate_overall_score(metrics):
    """
    Calculate overall score from all dimensions.

    Returns:
        score: 0-100
        status: PASSED/FAILED/NEEDS_REVIEW
    """
    total = (
        metrics['functional_completeness'] +
        metrics['token_efficiency'] +
        metrics['execution_quality'] +
        metrics['safety']
    )

    # Determine status
    if total >= 80:
        status = "PASSED"
    elif total >= 60:
        status = "NEEDS_REVIEW"
    else:
        status = "FAILED"

    return total, status
```

**Status thresholds:**
```
PASSED        → Score ≥ 80, Safe to deploy
NEEDS_REVIEW  → Score 60-79, Review with user
FAILED        → Score < 60, Cannot deploy
```

---

## Automation Implementation

### Verification Script

```python
#!/usr/bin/env python3
"""
verify_skill_optimization.py

Automatically verify skill optimization quality.
"""

import json
import sys
from pathlib import Path

class SkillVerifier:
    def __init__(self, original_skill, optimized_skill, test_cases=None):
        self.original = original_skill
        self.optimized = optimized_skill
        self.test_cases = test_cases or []

    def verify(self):
        """Run all verification checks."""
        results = {
            'functional_completeness': self._verify_functionality(),
            'token_efficiency': self._verify_efficiency(),
            'execution_quality': self._verify_execution(),
            'safety': self._verify_safety()
        }

        total, status = self._calculate_score(results)
        results['total'] = total
        results['status'] = status

        return results

    def _verify_functionality(self):
        content_score = calculate_content_coverage(
            self.original, self.optimized
        )

        equivalence_score = run_equivalence_tests(
            self.original, self.optimized, self.test_cases
        )

        return content_score + equivalence_score

    def _verify_efficiency(self):
        reduction_score = calculate_token_reduction(
            count_tokens(self.original),
            count_tokens(self.optimized),
            session_usage=10
        )

        efficiency_score = calculate_efficiency_ratio(
            self.original, self.optimized
        )

        return reduction_score + efficiency_score

    def _verify_execution(self):
        # Time score
        time_score = measure_response_time(
            self.optimized, self.test_cases[:3]
        )

        # Determinism score
        determinism_score = calculate_determinism(
            self.optimized, self.test_cases[:3]
        )

        return time_score + determinism_score

    def _verify_safety(self):
        backup_score = check_backup_exists(self.optimized)
        rollback_score = check_rollback_capability(self.optimized)

        return backup_score + rollback_score

    def _calculate_score(self, results):
        total = sum(results.values())
        if total >= 80:
            return total, "PASSED"
        elif total >= 60:
            return total, "NEEDS_REVIEW"
        else:
            return total, "FAILED"


def main():
    if len(sys.argv) < 3:
        print("Usage: verify_skill_optimization.py <original> <optimized> [test_cases.json]")
        sys.exit(1)

    original = Path(sys.argv[1]).read_text()
    optimized = Path(sys.argv[2]).read_text()

    test_cases = None
    if len(sys.argv) >= 4:
        test_cases = json.loads(Path(sys.argv[3]).read_text())

    verifier = SkillVerifier(original, optimized, test_cases)
    results = verifier.verify()

    print(json.dumps(results, indent=2))

    # Exit with appropriate code
    if results['status'] == "PASSED":
        sys.exit(0)
    elif results['status'] == "NEEDS_REVIEW":
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
```

### Test Case Format

```json
{
  "skill_name": "tdd",
  "test_cases": [
    {
      "input": "Add a new feature",
      "expected_output": {
        "must_contain": ["test", "before", "implement"],
        "must_not_contain": ["skip test", "test later"]
      }
    },
    {
      "input": "Tests are failing",
      "expected_output": {
        "must_contain": ["stop", "fix test"],
        "action": "stop_coding"
      }
    }
  ]
}
```

---

## Report Format

```json
{
  "verification_date": "2025-01-15T10:30:00Z",
  "skill": "tdd",
  "original_path": "/path/to/original/SKILL.md",
  "optimized_path": "/path/to/optimized/SKILL.md",

  "scores": {
    "functional_completeness": {
      "content_coverage": 18,
      "equivalence_tests": 19,
      "total": 37,
      "max": 40
    },
    "token_efficiency": {
      "token_reduction": 14,
      "efficiency_ratio": 12,
      "total": 26,
      "max": 30
    },
    "execution_quality": {
      "response_time": 8,
      "determinism": 9,
      "total": 17,
      "max": 20
    },
    "safety": {
      "backup": 5,
      "rollback": 5,
      "total": 10,
      "max": 10
    }
  },

  "overall": {
    "total": 90,
    "max": 100,
    "percentage": 90,
    "status": "PASSED"
  },

  "recommendations": [
    "Optimization is safe to deploy",
    "Consider adding more test cases for edge scenarios",
    "Token efficiency could be improved further"
  ],

  "details": {
    "token_savings": {
      "original_per_session": 12000,
      "optimized_per_session": 2400,
      "savings": 9600,
      "percentage": 80
    },
    "coverage": {
      "original_elements": 45,
      "optimized_elements": 43,
      "coverage": 95.5
    }
  }
}
```

---

## Usage Examples

### Command Line

```bash
# Basic verification
python verify_skill_optimization.py original.md optimized.md

# With test cases
python verify_skill_optimization.py original.md optimized.md tdd_tests.json

# CI/CD integration
python verify_skill_optimization.py original.md optimized.md | jq '.overall.status'
```

### As Python Library

```python
from skill_verification import SkillVerifier

verifier = SkillVerifier(
    original_skill=original_text,
    optimized_skill=optimized_text,
    test_cases=test_cases
)

results = verifier.verify()

if results['status'] == 'PASSED':
    print("✅ Optimization verified")
else:
    print(f"❌ Optimization {results['status']}")
```

---

## Continuous Integration

### GitHub Actions Example

```yaml
name: Verify Skill Optimization

on: [pull_request]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Verify optimization
        run: |
          python verification/verify_skill_optimization.py \
            skills/original/tdd/SKILL.md \
            skills/optimized/tdd/SKILL.md \
            tests/tdd.json

      - name: Check status
        run: |
          STATUS=$(python verification/verify_skill_optimization.py ... | jq '.overall.status')
          if [ "$STATUS" != "PASSED" ]; then
            echo "Optimization verification failed"
            exit 1
          fi
```

---

## Minimum Standards

For an optimization to be considered "safe to deploy":

| Dimension | Minimum | Target |
|-----------|---------|--------|
| Functional Completeness | ≥ 34/40 | ≥ 38/40 |
| Token Efficiency | ≥ 20/30 | ≥ 25/30 |
| Execution Quality | ≥ 12/20 | ≥ 16/20 |
| Safety | 10/10 | 10/10 |
| **Overall** | **≥ 76/100** | **≥ 80/100** |

---

## Extending the Standard

To add new verification dimensions:

1. Define scoring criteria (0-N points)
2. Implement automated check function
3. Add to overall score calculation
4. Update minimum standards

Example:

```python
def verify_accessibility(skill):
    """Verify skill is accessible to users."""
    score = 0

    # Check for clear language
    if avg_word_length(skill) < 5:
        score += 2

    # Check for examples
    if has_examples(skill):
        score += 3

    return score
```
