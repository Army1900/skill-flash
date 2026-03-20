#!/usr/bin/env python3
"""
Skill Optimization Verification Tool

Automatically verify that optimized skills maintain quality while reducing cost.

Usage:
    python verify.py <original_skill> <optimized_skill> [test_cases.json]
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple


def count_tokens(text: str) -> int:
    """Estimate token count (chars ÷ 4)."""
    return len(text) // 4


def extract_key_elements(skill: str) -> Dict[str, List[str]]:
    """Extract key elements from a skill."""
    elements = {
        'principles': [],
        'rules': [],
        'workflows': [],
        'decisions': []
    }

    lines = skill.split('\n')

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        # Extract principles (always, never, must)
        if any(word in line.lower() for word in ['always', 'never', 'must']):
            elements['principles'].append(line)

        # Extract rules (imperative statements)
        elif re.match(r'^-?\s*[A-Z][a-z]+.*:', line):
            elements['rules'].append(line)

        # Extract workflows (numbered steps)
        elif re.match(r'^\d+\.', line):
            elements['workflows'].append(line)

        # Extract decisions (questions)
        elif '?' in line or 'ask' in line.lower():
            elements['decisions'].append(line)

    return elements


def calculate_content_coverage(original: str, optimized: str) -> Dict[str, Any]:
    """Calculate how much original content is preserved."""
    original_elements = extract_key_elements(original)
    optimized_elements = extract_key_elements(optimized)

    coverage_scores = {}

    for key in original_elements:
        original_count = len(original_elements[key])
        optimized_count = len(optimized_elements[key])

        if original_count > 0:
            coverage = (optimized_count / original_count) * 100
            coverage_scores[key] = {
                'original': original_count,
                'optimized': optimized_count,
                'coverage': coverage,
                'score': coverage / 5  # 20 points max
            }
        else:
            coverage_scores[key] = {'original': 0, 'optimized': 0, 'coverage': 100, 'score': 20}

    total_coverage = sum(s['score'] for s in coverage_scores.values())
    coverage_scores['total'] = min(20, total_coverage)

    return coverage_scores


def count_key_concepts(skill: str) -> int:
    """Count key concepts in skill."""
    concepts = set()

    # Technical terms
    technical = re.findall(r'\b(test|coverage|refactor|workflow|principle|rule)\b', skill, re.I)
    concepts.update(technical)

    # Action words
    actions = re.findall(r'\b(write|run|check|verify|ensure|maintain)\b', skill, re.I)
    concepts.update(actions)

    # Numbers/metrics
    metrics = re.findall(r'\b\d+%\b', skill)
    concepts.update(metrics)

    return len(concepts)


def calculate_token_efficiency(original: str, optimized: str) -> Dict[str, Any]:
    """Calculate token efficiency metrics."""
    original_tokens = count_tokens(original)
    optimized_tokens = count_tokens(optimized)

    # Token reduction (assume 10 invocations per session)
    session_usage = 10
    original_session = original_tokens * session_usage
    optimized_session = optimized_tokens * session_usage

    reduction = (original_session - optimized_session) / original_session * 100

    # Score: 15 points if ≥ 50% reduction
    reduction_score = min(15, max(0, reduction * 0.3))

    # Efficiency ratio (information density)
    original_concepts = count_key_concepts(original)
    optimized_concepts = count_key_concepts(optimized)

    if original_concepts > 0 and optimized_concepts > 0:
        original_density = original_tokens / original_concepts
        optimized_density = optimized_tokens / optimized_concepts
        ratio = original_density / optimized_density
        efficiency_score = min(15, ratio * 7.5)
    else:
        efficiency_score = 0

    return {
        'token_reduction': {
            'original_per_session': original_session,
            'optimized_per_session': optimized_session,
            'savings': original_session - optimized_session,
            'percentage': reduction,
            'score': reduction_score
        },
        'efficiency_ratio': {
            'original_density': original_tokens / max(original_concepts, 1),
            'optimized_density': optimized_tokens / max(optimized_concepts, 1),
            'ratio': original_density / max(optimized_density, 1),
            'score': efficiency_score
        },
        'total': reduction_score + efficiency_score,
        'max': 30
    }


def calculate_safety(optimized_path: str) -> Dict[str, Any]:
    """Check safety measures."""
    backup_path = Path(str(optimized_path) + '.backup')

    backup_score = 5 if backup_path.exists() else 0

    # Check for integration record
    record_path = Path(optimized_path).parent / '.claude' / 'integration-record.md'
    rollback_score = 5 if record_path.exists() else 0

    return {
        'backup': {'exists': backup_path.exists(), 'score': backup_score},
        'rollback': {'exists': record_path.exists(), 'score': rollback_score},
        'total': backup_score + rollback_score,
        'max': 10
    }


def calculate_overall_score(metrics: Dict) -> Tuple[int, str]:
    """Calculate overall score and status."""
    total = (
        metrics['functional_completeness']['total'] +
        metrics['token_efficiency']['total'] +
        metrics['safety']['total']
    )

    max_score = (
        metrics['functional_completeness']['max'] +
        metrics['token_efficiency']['max'] +
        metrics['safety']['max']
    )

    percentage = (total / max_score) * 100

    if total >= 80:
        status = "PASSED"
    elif total >= 60:
        status = "NEEDS_REVIEW"
    else:
        status = "FAILED"

    return total, status, percentage


def verify_skill(original_path: str, optimized_path: str) -> Dict[str, Any]:
    """Run full verification."""
    original = Path(original_path).read_text()
    optimized = Path(optimized_path).read_text()

    metrics = {
        'functional_completeness': calculate_content_coverage(original, optimized),
        'token_efficiency': calculate_token_efficiency(original, optimized),
        'safety': calculate_safety(optimized_path)
    }

    total, status, percentage = calculate_overall_score(metrics)

    return {
        'verification_date': Path.cwd().name,
        'original_path': original_path,
        'optimized_path': optimized_path,
        'scores': metrics,
        'overall': {
            'total': total,
            'max': 100,
            'percentage': percentage,
            'status': status
        },
        'recommendations': generate_recommendations(metrics, status)
    }


def generate_recommendations(metrics: Dict, status: str) -> List[str]:
    """Generate recommendations based on scores."""
    recommendations = []

    if status == "PASSED":
        recommendations.append("✅ Optimization is safe to deploy")
    elif status == "NEEDS_REVIEW":
        recommendations.append("⚠️ Review optimization with user before deploying")
    else:
        recommendations.append("❌ Optimization failed quality checks")

    # Token efficiency recommendations
    token_reduction = metrics['token_efficiency']['token_reduction']['percentage']
    if token_reduction < 30:
        recommendations.append("Token savings are minimal - consider if optimization is worth it")
    elif token_reduction > 70:
        recommendations.append("Excellent token savings")

    # Content coverage recommendations
    coverage = metrics['functional_completeness']['total']
    if coverage < 17:
        recommendations.append("Significant content may be missing - review carefully")

    # Safety recommendations
    if metrics['safety']['total'] < 10:
        recommendations.append("Create backup before deploying")

    return recommendations


def main():
    if len(sys.argv) < 3:
        print("Usage: python verify.py <original_skill> <optimized_skill>")
        print("\nExample:")
        print("  python verify.py skills/original/tdd/SKILL.md skills/optimized/tdd/SKILL.md")
        sys.exit(1)

    original_path = sys.argv[1]
    optimized_path = sys.argv[2]

    if not Path(original_path).exists():
        print(f"Error: Original skill not found: {original_path}")
        sys.exit(1)

    if not Path(optimized_path).exists():
        print(f"Error: Optimized skill not found: {optimized_path}")
        sys.exit(1)

    results = verify_skill(original_path, optimized_path)

    print(json.dumps(results, indent=2))

    # Exit with appropriate code
    if results['overall']['status'] == "PASSED":
        sys.exit(0)
    elif results['overall']['status'] == "NEEDS_REVIEW":
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
