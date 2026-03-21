---
name: tdd-balanced
description: Test-driven development (balanced optimization)
version: balanced_v3
has_initial_decisions: true
---

# TDD (Balanced Optimization with Batched Decisions)

> Core principles are embedded in system prompt.
> Critical explanations preserved for reasoning quality.
> **All preferences collected upfront to avoid interruptions** ⚡

---

## Initial Configuration

Before starting work, I'll collect all preferences at once:

**Testing Setup**:

| Decision | Options | Default | Your Choice |
|----------|---------|---------|-------------|
| Framework | pytest, jest, go test, junit | auto* | |
| Coverage target | 80%, 90%, 100% | 80% | |
| Mock strategy | mock, real, hybrid | mock | |
| Test style | unit, integration, both | both | |

*Framework defaults by language: Python→pytest, JS→Jest, Go→go test, Java→JUnit

**Please provide your choices (or press Enter to use defaults)**:
1. Framework:
2. Coverage target:
3. Mock strategy:
4. Test style:

Once collected, execution proceeds without interruption.

---

## Core Principles

- **Test before code** - Always write tests before implementation
- **Red-Green-Refactor** - Standard TDD cycle
- **Test isolation** - Each test must be independent
- **Fast tests** - Keep tests quick to run frequently
- **Coverage standard** - Maintain configured minimum (default: 80%)

---

## TDD Workflow

1. Write a test for functionality (using [framework])
2. Run test (expect failure - RED)
3. Write minimum code to pass
4. Run test (expect success - GREEN)
5. Refactor code
6. Verify coverage meets [coverage target]%
7. Repeat

**Why this works**: Writing the test first clarifies requirements. Failing first proves the test works. Minimal code prevents over-engineering.

---

## Framework-Specific Guidance

*Using configured framework: [framework]*

### Python (pytest)
```bash
# Run with coverage
pytest --cov=. --cov-fail-under=[coverage]

# Common pattern
def test_feature():
    # Arrange
    result = function()
    # Assert
    assert result == expected
```

### JavaScript (Jest)
```bash
# Run with coverage
jest --coverage --coverageThreshold='{"global":{"lines":[coverage]}}'

# Common pattern
test('feature', () => {
  expect(function()).toBe(expected);
});
```

### Go (go test)
```bash
# Run with coverage
go test -cover -coverprofile=coverage.out
go tool cover -func=coverage.out
```

### Java (JUnit)
```java
@Test
public void testFeature() {
    assertEquals(expected, function());
}
```

---

## Common Mistakes to Avoid

- **Don't skip tests for "simple" code** → Even simple code can have bugs in edge cases
- **Don't write tests after the code** → This defeats TDD and results in fewer tests
- **Don't ignore failing tests** → A failing test indicates a problem that needs addressing
- **Don't make tests dependent on each other** → Each test should run independently

---

## When to Use This Skill

- New feature development
- Bug fixes with tests
- Refactoring (keep tests passing)
- Coverage analysis

---

## Coverage Requirements

Based on your configured target of **[coverage target]%**:

- **New features**: At least one test per function
- **Edge cases**: Test boundary conditions (empty, null, max values)
- **Error conditions**: Test failure paths
- **Overall**: Maintain [coverage target]% minimum

---

## Mock Strategy

*Using configured strategy: [mock strategy]*

### Mock
Fast, isolated tests. Use for:
- External API calls
- Database operations
- File system operations

```python
# pytest-mock example
def test_api_call(mocker):
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.status_code = 200
    # Test behavior, not implementation
```

### Real
Slower, realistic tests. Use for:
- Integration testing
- End-to-end workflows
- Critical business logic

### Hybrid
Balanced approach. Mock for unit tests, real for integration tests.

---

## Questions for Implementation

When implementing with TDD:
- What's the simplest code that will make the test pass?
- Are there edge cases I should test for?
- Is my code testable?
- Am I testing behavior, not implementation?
