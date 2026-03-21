#!/bin/bash
# check_coverage.sh - Verify test coverage meets threshold
set -e

# Default threshold
COVERAGE_THRESHOLD=${1:-80}

echo "Checking test coverage (threshold: ${COVERAGE_THRESHOLD}%)..."

# Detect language and run appropriate command
if [ -f "pytest.ini" ] || [ -f "pyproject.toml" ] || grep -q "pytest" requirements.txt 2>/dev/null; then
    echo "Detected Python project with pytest"
    pytest --cov=. --cov-fail-under=$COVERAGE_THRESHOLD

elif [ -f "package.json" ] && grep -q "jest" package.json 2>/dev/null; then
    echo "Detected JavaScript project with Jest"
    jest --coverage --coverageThreshold="{\"global\":{\"lines\":${COVERAGE_THRESHOLD}}}"

elif [ -f "go.mod" ]; then
    echo "Detected Go project"
    go test -cover -coverprofile=coverage.out
    go tool cover -func=coverage.out | grep total | awk '{if ($3+0 < '$COVERAGE_THRESHOLD') exit 1}'
    echo "Coverage meets ${COVERAGE_THRESHOLD}% threshold"

else
    echo "⚠️  Could not detect project type"
    echo "Please manually verify coverage is ≥ ${COVERAGE_THRESHOLD}%"
    exit 0
fi

echo "✅ PASS: Coverage meets ${COVERAGE_THRESHOLD}% threshold"
