# Code Examples for Skill Compilation

This file contains example scripts that can be generated during skill compilation.
These are reference implementations for the LLM to use when creating executable scripts.

## Bash Script Examples

### Check Test Coverage

```bash
#!/bin/bash
# check_coverage.sh - Verify test coverage threshold
set -e

COVERAGE=$(pytest --cov --cov-report=term 2>/dev/null | grep TOTAL | awk '{print $4}' | sed 's/%//')

if [ -z "$COVERAGE" ]; then
    echo "Unable to determine coverage"
    exit 1
fi

if [ "$COVERAGE" -lt 80 ]; then
    echo "FAIL: Coverage ${COVERAGE}% < 80%"
    exit 1
fi

echo "PASS: Coverage ${COVERAGE}%"
```

### Check for Hardcoded Secrets

```bash
#!/bin/bash
# check_secrets.sh - Scan for hardcoded secrets in code
set -e

# Common secret patterns
PATTERNS=(
    "password\s*=\s*['\"][^'\"]+['\"]"
    "api_key\s*=\s*['\"][^'\"]+['\"]"
    "secret\s*=\s*['\"][^'\"]+['\"]"
    "token\s*=\s*['\"][^'\"]+['\"]"
)

FOUND=0
for pattern in "${PATTERNS[@]}"; do
    if git grep -iE "$pattern" -- '*.py' '*.js' '*.ts' '*.env*' 2>/dev/null; then
        FOUND=1
    fi
done

if [ $FOUND -eq 1 ]; then
    echo "FAIL: Potential hardcoded secrets found"
    exit 1
fi

echo "PASS: No hardcoded secrets detected"
```

### Check Git Status

```bash
#!/bin/bash
# check_git_clean.sh - Verify working directory is clean
set -e

if [ -n "$(git status --porcelain)" ]; then
    echo "FAIL: Working directory has uncommitted changes"
    git status --short
    exit 1
fi

echo "PASS: Working directory is clean"
```

### Check File Exists

```bash
#!/bin/bash
# check_file_exists.sh - Verify required file exists
set -e

FILE="${1:-required_file.txt}"

if [ ! -f "$FILE" ]; then
    echo "FAIL: Required file not found: $FILE"
    exit 1
fi

echo "PASS: File exists: $FILE"
```

## Python Script Examples

### Validate Test File Exists

```python
#!/usr/bin/env python3
# validate_tests.py - Ensure test file exists for source file
import sys
from pathlib import Path

def check_test_exists(source_file):
    """Check if test file exists for source file."""
    source = Path(source_file)

    # Map source to test file (adjust patterns per project)
    test_mappings = [
        (lambda p: p.parent.parent / "tests" / f"{p.stem}_test.py"),
        (lambda p: p.parent / "test_" + p.name,
        (lambda p: p.with_name(f"{p.stem}_test.py"))
    ]

    for mapping in test_mappings:
        test_file = mapping(source)
        if test_file.exists():
            print(f"PASS: {test_file}")
            return True

    print(f"FAIL: No test file found for {source}")
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_tests.py <source_file>")
        sys.exit(1)

    sys.exit(0 if check_test_exists(sys.argv[1]) else 1)
```

### Check Code Coverage

```python
#!/usr/bin/env python3
# check_coverage.py - Parse and verify test coverage
import subprocess
import sys
import re

def extract_coverage(output: str) -> float:
    """Extract coverage percentage from pytest output."""
    # Try multiple patterns
    patterns = [
        r"TOTAL\s+\d+\s+\d+\s+(\d+)%",  # pytest-cov standard
        r"coverage:\s+(\d+)%",            # Alternative format
        r"(\d+)%\s+coverage",             # Yet another format
    ]

    for pattern in patterns:
        match = re.search(pattern, output)
        if match:
            return float(match.group(1))

    return 0.0

def main():
    threshold = 80.0
    if len(sys.argv) > 1:
        threshold = float(sys.argv[1])

    result = subprocess.run(
        ["pytest", "--cov", "--cov-report=term"],
        capture_output=True,
        text=True
    )

    coverage = extract_coverage(result.stdout)

    if coverage >= threshold:
        print(f"PASS: Coverage {coverage:.1f}% >= {threshold}%")
        return 0
    else:
        print(f"FAIL: Coverage {coverage:.1f}% < {threshold}%")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### Validate Code Structure

```python
#!/usr/bin/env python3
# validate_structure.py - Check project structure conventions
import sys
from pathlib import Path

def check_project_structure(root: Path) -> bool:
    """Verify required directories and files exist."""
    required = {
        "dirs": ["src", "tests"],
        "files": ["README.md", "pyproject.toml"],
    }

    issues = []

    # Check directories
    for dir_name in required["dirs"]:
        if not (root / dir_name).exists():
            issues.append(f"Missing directory: {dir_name}")

    # Check files
    for file_name in required["files"]:
        if not (root / file_name).exists():
            issues.append(f"Missing file: {file_name}")

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        return False

    print("PASS: Project structure is valid")
    return True

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    sys.exit(0 if check_project_structure(root) else 1)
```

## JavaScript/TypeScript Examples

### Check ESLint Passes

```javascript
#!/usr/bin/env node
// check_eslint.js - Verify ESLint passes
const { execSync } = require('child_process');
const process = require('process');

try {
  const output = execSync('npm run lint -- --format json', {
    encoding: 'utf-8',
    stdio: 'pipe'
  });

  const result = JSON.parse(output);
  const errorCount = result.reduce((sum, file) => sum + file.errorCount, 0);
  const warningCount = result.reduce((sum, file) => sum + file.warningCount, 0);

  if (errorCount > 0) {
    console.log(`FAIL: ${errorCount} ESLint errors found`);
    process.exit(1);
  }

  if (warningCount > 0) {
    console.log(`WARN: ${warningCount} ESLint warnings found`);
  }

  console.log('PASS: ESLint checks passed');
  process.exit(0);

} catch (error) {
  console.log(`FAIL: ESLint failed to run: ${error.message}`);
  process.exit(1);
}
```

### Check TypeScript Compiles

```javascript
#!/usr/bin/env node
// check_typescript.js - Verify TypeScript compilation
const { execSync } = require('child_process');
const process = require('process');

try {
  execSync('npx tsc --noEmit', {
    stdio: 'inherit'
  });

  console.log('PASS: TypeScript compilation successful');
  process.exit(0);

} catch (error) {
  console.log('FAIL: TypeScript compilation failed');
  process.exit(1);
}
```

## Usage in Skill Compilation

When compiling a skill, use these examples as templates. Adapt them to:

1. **Match the project's language** (Python, Bash, JavaScript, etc.)
2. **Fit the specific rule** (coverage threshold, file patterns, etc.)
3. **Follow project conventions** (test file locations, config files, etc.)

The LLM should generate similar scripts based on the identified scriptable rules in the source skill.
