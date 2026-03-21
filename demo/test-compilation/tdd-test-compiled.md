---
name: tdd-compiled
description: Test-driven development (compiled)
version: test_v1
---

# TDD Skill (Compiled)

## Configuration

**Smart defaults**:
- Framework: auto-detected (Python→pytest, JS→Jest, Go→go test)
- Coverage: 80%
- Mock: yes (for fast, isolated tests)

I'll start with these. To customize, say **"config"**.

---

## Core Principles

- **Test before code** - Always write tests before implementation
- **Red-Green-Refactor** - Write failing test, make it pass, improve
- **Test isolation** - Each test runs independently
- **Fast tests** - Keep tests quick to run frequently

---

## TDD Workflow

1. Write a test for functionality
2. Run test (expect failure - RED)
3. Write minimum code to pass
4. Run test (expect success - GREEN)
5. Refactor code
6. Repeat

---

## When to Use

- New feature development
- Bug fixes with tests
- Refactoring (keep tests passing)

---

## Framework-Specific Guidance

*Framework auto-detected from your project*

### Python (pytest)
```bash
pytest --cov=. --cov-fail-under=80
```

### JavaScript (Jest)
```bash
jest --coverage
```

### Go (go test)
```bash
go test -cover
```

---

## Coverage Requirements

- At least one test per function
- Test edge cases (empty, null, max values)
- Test error conditions
- Maintain 80% minimum

---

## Common Mistakes

- Don't skip tests for "simple" code
- Don't write tests after the code
- Don't ignore failing tests
- Don't make tests dependent
