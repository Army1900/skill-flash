---
name: tdd-compiled
description: Test-driven development (compiled,实用性优先)
version: test_v2
---

# TDD Skill (Compiled - Practical)

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

1. **Write a test** for the functionality
2. **Run test** - Expect failure (RED)
3. **Write code** - Minimum to make test pass
4. **Run test** - Expect success (GREEN)
5. **Refactor** - Improve structure while tests stay green
6. **Repeat**

---

## Refactoring Guidelines

**What is refactoring**: Improving code structure without changing behavior.

**Safe refactoring**:
- Only refactor when all tests are green
- Make small, incremental changes
- Run tests after each change
- Stop immediately if a test fails

**When to refactor**:
- After making a test pass
- When you see duplicate code
- When code can be clearer

---

## When to Use

- New feature development
- Bug fixes with tests
- Refactoring existing code (keep tests passing)

---

## Framework-Specific Guidance

*Framework auto-detected from your project*

### Python (pytest)
```bash
# Run with coverage
pytest --cov=. --cov-fail-under=80

# Run specific test
pytest tests/test_login.py

# Run with verbose output
pytest -v
```

### JavaScript (Jest)
```bash
# Run with coverage
jest --coverage

# Run specific test
jest login.test.js

# Watch mode
jest --watch
```

### Go (go test)
```bash
# Run with coverage
go test -cover -coverprofile=coverage.out
go tool cover -func=coverage.out

# Run specific test
go test -run TestLogin
```

---

## Coverage Requirements

- **Per feature**: At least one test per function
- **Edge cases**: Test boundary conditions (empty, null, max values)
- **Error conditions**: Test failure paths
- **Overall**: Maintain 80% minimum

---

## Quality Checklist

Before considering code complete, ask yourself:

- [ ] Is this the simplest code that makes the test pass?
- [ ] Have I tested edge cases (empty, null, boundaries)?
- [ ] Is my code testable and well-structured?
- [ ] Am I testing behavior, not implementation details?

---

## Common Mistakes

- **Don't skip tests for "simple" code** → Even simple code can have bugs
- **Don't write tests after the code** → This defeats TDD and results in fewer tests
- **Don't ignore failing tests** → A failing test indicates a problem that needs addressing
- **Don't make tests dependent** → Each test should run independently
- **Don't refactor without tests** → Always have green tests before refactoring
