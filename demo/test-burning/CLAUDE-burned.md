# My Project

## Project Overview
This is a web API project for user management.

## Development Approach

**Test-Driven Development (TDD)**:
- **Write tests before code** - Always start with a failing test
- **Red-Green-Refactor** - Write test, make it pass, improve code
- **Test isolation** - Each test runs independently
- **Fast tests** - Keep tests quick to run frequently
- **80% coverage** - Maintain minimum code coverage

## Code Style
- Use clear variable names
- Functions should be under 50 lines
- Add comments for complex logic
- Follow PEP 8 for Python

## API Design
- Use RESTful conventions
- Return appropriate status codes
- Include error messages in responses

## Data Handling
- Validate all inputs
- Sanitize database queries
- Log important operations

## Testing

**Auto-detected frameworks**:
- Python: pytest with `pytest --cov=. --cov-fail-under=80`
- JavaScript: Jest with coverage enabled

**Coverage requirements**:
- At least one test per function
- Test edge cases (empty, null, max values)
- Test error conditions
