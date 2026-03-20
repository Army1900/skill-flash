---
name: tdd
description: Test-driven development workflow
---

# Test-Driven Development

## Overview
Test-Driven Development (TDD) is a software development process that relies on very short development cycles: requirements are turned into very specific test cases, then the software is improved to pass the tests.

## Core Principles

### The Golden Rule of TDD
Always write tests before writing code. This is the most fundamental principle of test-driven development.

### Test Isolation
Each test should be independent of other tests. Tests should not rely on the execution order of other tests.

### Fast Tests
Keep tests fast so they can be run frequently during development.

### Coverage Standards
Maintain at least 80% code coverage to ensure quality.

## TDD Workflow

The standard TDD workflow consists of the following steps:

1. Add a test for a small piece of functionality
2. Run all tests and see the new test fail
3. Write the minimum code to make the test pass
4. Run all tests and see them all pass
5. Refactor the code if needed
6. Repeat

This is often referred to as "Red-Green-Refactor":
- **Red**: Write a failing test
- **Green**: Write code to make it pass
- **Refactor**: Improve the code while keeping tests green

## When to Use TDD

Use TDD for:
- New feature development
- Bug fixes
- Refactoring existing code
- Critical functionality that requires reliability

## Testing Frameworks

Before starting, determine which testing framework to use:
- Python: pytest or unittest
- JavaScript: Jest or Mocha
- Go: go test
- Java: JUnit

## Common Mistakes to Avoid

### Don't skip tests for "simple" code
Even simple code can have bugs. Always write tests.

### Don't write tests after the code
This defeats the purpose of TDD and often results in fewer tests.

### Don't ignore failing tests
A failing test indicates a problem. Address it before moving on.

### Don't make tests dependent on each other
Each test should be able to run independently.

## Coverage Requirements

For each new feature:
- Write at least one test for the main functionality
- Write tests for edge cases
- Write tests for error conditions
- Maintain overall project coverage above 80%

## Refactoring

Refactoring is improving the structure of code without changing its behavior. Always have passing tests before refactoring, and keep them passing during refactoring.

## Questions to Consider

When implementing with TDD, consider:
- What is the simplest code that will make the test pass?
- Are there edge cases I should test for?
- Is my code testable?
- Am I testing the right things?
