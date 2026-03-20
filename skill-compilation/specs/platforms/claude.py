"""
Claude platform adapter.

Handles Claude Skill format (SKILL.md with frontmatter).
"""

import re
from pathlib import Path
from typing import List, Dict, Any
from .base import PlatformAdapter, Skill, ScriptableRule, CompiledOutput


class ClaudeAdapter(PlatformAdapter):
    """Adapter for Claude Skills."""

    @property
    def platform_name(self) -> str:
        return "claude"

    @property
    def input_extensions(self) -> List[str]:
        return [".md", "SKILL.md"]

    def parse_skill(self, path: Path) -> Skill:
        """Parse Claude SKILL.md file."""
        content = path.read_text()

        # Parse frontmatter
        frontmatter = {}
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter_match:
            for line in frontmatter_match.group(1).split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()

        # Remove frontmatter from content
        body_content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

        # Extract sections
        principles = self._extract_principles(body_content)
        rules = self._extract_rules(body_content)
        workflows = self._extract_workflows(body_content)
        decisions = self._extract_decisions(body_content)

        return Skill(
            name=frontmatter.get('name', path.parent.name),
            description=frontmatter.get('description', ''),
            content=content,
            principles=principles,
            rules=rules,
            workflows=workflows,
            decisions=decisions,
            metadata={"format": "claude", "frontmatter": frontmatter}
        )

    def _extract_principles(self, content: str) -> List[str]:
        """Extract core principles from content."""
        principles = []

        # Look for "Core Principles" section
        principles_match = re.search(
            r'## Core Principles\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )
        if principles_match:
            for line in principles_match.group(1).split('\n'):
                line = line.strip()
                if line.startswith('- ') or line.startswith('* '):
                    principles.append(line[2:])
                elif line and not line.startswith('#'):
                    principles.append(line)

        return principles

    def _extract_rules(self, content: str) -> List[Dict[str, Any]]:
        """Extract structured rules from content."""
        rules = []

        # Look for rule-like patterns
        # Format: - **Name**: Description
        rule_pattern = r'-\s*\*\*([^*]+)\*\*:\s*([^\n]+)'
        for match in re.finditer(rule_pattern, content):
            rules.append({
                "name": match.group(1).strip(),
                "description": match.group(2).strip()
            })

        return rules

    def _extract_workflows(self, content: str) -> List[Dict[str, Any]]:
        """Extract workflow sections."""
        workflows = []

        # Look for "Workflow" or "Step" sections
        workflow_match = re.search(r'## Workflow\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if workflow_match:
            steps = re.findall(r'###?\s*Step\s+\d+:\s*([^\n]+)', workflow_match.group(1))
            workflows.append({
                "name": "main",
                "steps": steps
            })

        return workflows

    def _extract_decisions(self, content: str) -> List[Dict[str, Any]]:
        """Extract decision points (questions to ask user)."""
        decisions = []

        # Look for question patterns
        # Format: "Ask the user for..." or "Check with user..."
        question_patterns = [
            r'Ask (?:the )?user (?:for|about|to):?\s*([^\n]+)',
            r'Check with user[:\s]+([^\n]+)',
            r'Confirm[:\s]+([^\n]+)',
        ]

        for pattern in question_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                decisions.append({
                    "question": match.group(1).strip(),
                    "context": self._get_line_context(content, match.start())
                })

        return decisions

    def _get_line_context(self, content: str, pos: int) -> str:
        """Get surrounding line for context."""
        start = content.rfind('\n', 0, pos - 100) + 1
        end = content.find('\n', pos + 100)
        return content[start:end].strip()

    def extract_tier1(self, skill: Skill) -> str:
        """Extract core principles for Claude CLAUDE.md format."""
        if not skill.principles:
            return ""

        principles_section = f"## {skill.name.title()} Principles\n\n"
        for principle in skill.principles[:5]:  # Top 5
            principles_section += f"- {principle}\n"

        return principles_section

    def extract_tier2(self, skill: Skill) -> str:
        """Generate session-level config."""
        config = {
            "session": {
                "skills": [skill.name],
                "loaded_at": "session_start",
                "reference_mode": True
            },
            "rules": skill.rules[:3]  # Key rules for session
        }
        return f"# Session config for {skill.name}\n" + str(config)

    def simplify_tier3(self, skill: Skill) -> str:
        """Simplify skill for on-demand loading."""
        # Keep only essential parts
        simplified = f"""---
name: {skill.name}
description: {skill.description}
compiled: true
---

# {skill.name.title()} (Optimized)

**This skill has been compiled.** Core principles are embedded in system prompt.

## When to Use

Use this skill when:
{chr(10).join(f"- {d.get('question', '')}" for d in skill.decisions[:3])}

## Quick Reference

Key workflows are loaded at session start. This file handles edge cases only.
"""
        return simplified

    def identify_scriptable_rules(self, skill: Skill) -> List[ScriptableRule]:
        """Identify rules that can be scripts."""
        scriptable = []

        # Common Claude patterns that can be scripted
        patterns = {
            "file_exists": r"Check (?:that|if) (?:file|test) exists?",
            "coverage": r"(?:coverage|test coverage) (?:of|above|>=) (\d+)%?",
            "git_clean": r"(?:git|repository) (?:is )?(?:clean|no changes)",
        }

        for rule in skill.rules:
            for pattern_name, pattern in patterns.items():
                if re.search(pattern, rule['description'], re.IGNORECASE):
                    scriptable.append(self._generate_script(rule, pattern_name))

        return scriptable

    def _generate_script(self, rule: Dict[str, Any], pattern_name: str) -> ScriptableRule:
        """Generate a script for a rule."""
        scripts = {
            "file_exists": ScriptableRule(
                name=rule['name'],
                check="file_exists",
                language="bash",
                code='''#!/bin/bash
[ -f "$1" ] && echo "PASS" || echo "FAIL: File not found"''',
                tier=2
            ),
            "coverage": ScriptableRule(
                name=rule['name'],
                check="coverage",
                language="python",
                code='''import subprocess
import sys
result = subprocess.run(["pytest", "--cov", "--cov-report=term"],
                       capture_output=True, text=True)
# Parse coverage from output
for line in result.stdout.split('\\n'):
    if 'TOTAL' in line or '%' in line:
        print(line)
        sys.exit(0 if int(line.split()[-1].replace('%', '')) >= 80 else 1)
''',
                tier=2
            ),
            "git_clean": ScriptableRule(
                name=rule['name'],
                check="git_clean",
                language="bash",
                code='''#!/bin/bash
[ -z "$(git status --porcelain)" ] && echo "PASS" || echo "FAIL: Working directory not clean"''',
                tier=2
            )
        }
        return scripts.get(pattern_name, ScriptableRule(
            name=rule['name'],
            check="generic",
            language="python",
            code=f"# Script for: {rule['description']}\nraise NotImplementedError",
            tier=3
        ))

    def batch_decisions(self, skill: Skill) -> List[Dict[str, Any]]:
        """Batch decision points for upfront collection."""
        # Group related decisions
        return [
            {
                "category": "initial_setup",
                "decisions": skill.decisions,
                "prompt": "Before we begin, I need to understand a few things:",
                "collect_all": True
            }
        ]

    def format_output(self, compiled: CompiledOutput, output_dir: Path) -> None:
        """Write compiled output for Claude platform."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Tier 1: For CLAUDE.md
        if compiled.tier1_principles:
            (output_dir / "CLAUDE.md.fragment").write_text(compiled.tier1_principles)

        # Tier 2: Session config
        if compiled.tier2_session:
            (output_dir / "session.yaml").write_text(compiled.tier2_session)

        # Tier 3: Optimized skill
        (output_dir / "SKILL.md").write_text(compiled.tier3_skill)

        # Scripts
        scripts_dir = output_dir / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        for script in compiled.scripts:
            ext = {"python": ".py", "bash": ".sh", "javascript": ".js"}
            (scripts_dir / f"{script.name}{ext.get(script.language, '')}").write_text(script.code)
            (scripts_dir / f"{script.name}{ext.get(script.language, '')}").chmod(0o755)

        # Report
        import json
        (output_dir / "report.json").write_text(
            json.dumps(compiled.report, indent=2)
        )
