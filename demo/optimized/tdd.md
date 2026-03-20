---
name: tdd
description: Test-driven development (optimized)
optimized: true
---

# TDD (Optimized)

> Core principles are embedded in system prompt. This handles edge cases.

## Core Principles

- **Test before code** - Always write tests before implementation
- **Red-Green-Refactor** - Standard TDD cycle
- **Test isolation** - Each test must be independent
- **Fast tests** - Keep tests quick to run frequently
- **Coverage standard** - Maintain 80% minimum

## TDD Workflow

1. Write a test for functionality
2. Run test (expect failure - RED)
3. Write minimum code to pass
4. Run test (expect success - GREEN)
5. Refactor code
6. Repeat

## Common Mistakes to Avoid

- Don't skip tests for "simple" code
- Don't write tests after the code
- Don't ignore failing tests
- Don't make tests dependent on each other

## When to Use

Use this skill for:
- New feature development
- Bug fixes with tests
- Refactoring (keep tests passing)
- Choosing testing frameworks

## Framework Selection

Ask user: Which testing framework?
- Python: pytest
- JavaScript: Jest
- Go: go test
- Java: JUnit

## Coverage Requirements

- New features: At least one test per function
- Edge cases: Test boundary conditions
- Error conditions: Test failure paths
- Overall: Maintain 80% minimum coverage

## Questions to Consider

When implementing with TDD:
- What's the simplest code to pass?
- Are there edge cases to test?
- Is my code testable?
- Am I testing the right things?
