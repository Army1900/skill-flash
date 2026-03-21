---
name: tdd
description: Test-driven development (balanced)
version: balanced_v2
---

# TDD (Balanced Optimization)

> Core principles are embedded in system prompt.
> Critical explanations preserved for reasoning quality.

## Core Principles

- **Test before code** - Always write tests before implementation
- **Red-Green-Refactor** - Standard TDD cycle
- **Test isolation** - Each test must be independent (tests shouldn't depend on execution order)
- **Fast tests** - Keep tests quick to run frequently
- **Coverage standard** - Maintain 80% minimum (ensures quality while allowing flexibility)

## TDD Workflow

1. Write a test for functionality
2. Run test (expect failure - RED)
3. Write minimum code to pass
4. Run test (expect success - GREEN)
5. Refactor code
6. Repeat

**Why this works:** Writing the test first clarifies requirements. Failing first proves the test works. Minimal code prevents over-engineering.

## Common Mistakes to Avoid

- **Don't skip tests for "simple" code** → Even simple code can have bugs in edge cases
- **Don't write tests after the code** → This defeats TDD and results in fewer tests
- **Don't ignore failing tests** → A failing test indicates a problem that needs addressing
- **Don't make tests dependent on each other** → Each test should run independently

## When to Use This Skill

- New feature development
- Bug fixes with tests
- Refactoring (keep tests passing)
- Choosing testing frameworks
- Coverage analysis

## Framework Selection

Ask user: Which testing framework?
- Python: pytest
- JavaScript: Jest
- Go: go test
- Java: JUnit

## Coverage Requirements

- **New features**: At least one test per function
- **Edge cases**: Test boundary conditions (empty, null, max values)
- **Error conditions**: Test failure paths
- **Overall**: Maintain 80% minimum

**Why 80%**: Ensures most code is tested while allowing some flexibility for untestable code like UI or random functions.

## Questions for Implementation

When implementing with TDD, consider:
- What's the simplest code that will make the test pass?
- Are there edge cases I should test for?
- Is my code testable?
- Am I testing the right things (behavior, not implementation)?
