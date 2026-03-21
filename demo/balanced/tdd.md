---
name: tdd-balanced
description: Test-driven development (balanced optimization)
version: balanced_v4
---

# TDD (Balanced Optimization)

> Core principles embedded in system prompt.
> Smart defaults eliminate configuration questions.

---

## Configuration

**Smart defaults** (work well for most projects):
- Framework: auto-detected (Python→pytest, JS→Jest, Go→go test)
- Coverage: 80% (industry standard)
- Mock: yes (fast, isolated tests)

I'll start with these. To customize, say **"config"**.

---

## Core Principles

- **Test before code** - Always write tests before implementation
- **Red-Green-Refactor** - Standard TDD cycle
- **Test isolation** - Each test must be independent
- **Fast tests** - Keep tests quick to run frequently

---

## TDD Workflow

1. Write a test for functionality
2. Run test (expect failure - RED)
3. Write minimum code to pass
4. Run test (expect success - GREEN)
5. Refactor code
6. Repeat

**Why this works**: Writing the test first clarifies requirements. Failing first proves the test works. Minimal code prevents over-engineering.

---

## Framework-Specific Guidance

*Framework auto-detected from your project*

### Python (pytest)
```bash
# Run with coverage
pytest --cov=. --cov-fail-under=80

# Common pattern
def test_feature():
    result = function()
    assert result == expected
```

### JavaScript (Jest)
```bash
# Run with coverage
jest --coverage

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

## Coverage Requirements

- **New features**: At least one test per function
- **Edge cases**: Test boundary conditions (empty, null, max values)
- **Error conditions**: Test failure paths
- **Overall**: Maintain 80% minimum

---

## Common Mistakes to Avoid

- **Don't skip tests for "simple" code** → Even simple code can have bugs
- **Don't write tests after the code** → This defeats TDD
- **Don't ignore failing tests** → A failing test needs addressing
- **Don't make tests dependent** → Each test should run independently

---

## When to Use This Skill

- New feature development
- Bug fixes with tests
- Refactoring (keep tests passing)
- Coverage analysis
