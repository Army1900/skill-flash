"""
Cursor platform adapter.

Handles Cursor .cursorrules format.
"""

import re
from pathlib import Path
from typing import List, Dict, Any
from .base import PlatformAdapter, Skill, ScriptableRule, CompiledOutput


class CursorAdapter(PlatformAdapter):
    """Adapter for Cursor AI rules (.cursorrules)."""

    @property
    def platform_name(self) -> str:
        return "cursor"

    @property
    def input_extensions(self) -> List[str]:
        return [".cursorrules", ".txt"]

    def parse_skill(self, path: Path) -> Skill:
        """Parse .cursorrules file."""
        content = path.read_text()

        # .cursorrules is typically line-based rules
        principles = []
        rules = []
        workflows = []
        decisions = []

        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Categorize rules
            if any(word in line.lower() for word in ['always', 'never', 'must']):
                principles.append(line)
            elif '?' in line or 'ask' in line.lower():
                decisions.append({"question": line})
            else:
                rules.append({"name": line[:30], "description": line})

        return Skill(
            name=path.stem,
            description=f"Cursor rules from {path.name}",
            content=content,
            principles=principles,
            rules=rules,
            workflows=workflows,
            decisions=decisions,
            metadata={"format": "cursor"}
        )

    def extract_tier1(self, skill: Skill) -> str:
        """Extract core cursor rules."""
        # Top 5 principles for cursor
        return "\n".join(f"- {p}" for p in skill.principles[:5])

    def extract_tier2(self, skill: Skill) -> str:
        """Generate .cursorrules-session config."""
        return f"# Session rules for {skill.name}\n" + \
               "\n".join(f"{r['description']}" for r in skill.rules[:3])

    def simplify_tier3(self, skill: Skill) -> str:
        """Simplify cursor rules."""
        return f"# {skill.name} (Optimized)\n\n" + \
               "\n".join(r['description'] for r in skill.rules[3:])

    def identify_scriptable_rules(self, skill: Skill) -> List[ScriptableRule]:
        """Cursor doesn't support scripts, but we can suggest VSCode tasks."""
        scriptable = []

        for rule in skill.rules:
            if 'lint' in rule['description'].lower():
                scriptable.append(ScriptableRule(
                    name=rule['name'],
                    check="vscode_task",
                    language="json",
                    code=f'''{{"label": "Run {rule['name']}", "type": "shell",
"command": "npm run lint"}}''',
                    tier=2
                ))

        return scriptable

    def batch_decisions(self, skill: Skill) -> List[Dict[str, Any]]:
        """Cursor doesn't have user prompts, but we can note them."""
        return [{"note": "Decisions should be made by user before cursor runs"}]

    def _extract_principles(self, content: str) -> List[str]:
        return []

    def _extract_rules(self, content: str) -> List[Dict[str, Any]]:
        return []

    def _extract_workflows(self, content: str) -> List[Dict[str, Any]]:
        return []

    def _extract_decisions(self, content: str) -> List[Dict[str, Any]]:
        return []

    def format_output(self, compiled: CompiledOutput, output_dir: Path) -> None:
        """Write optimized .cursorrules."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Core rules (for .cursorrules)
        (output_dir / ".cursorrules").write_text(compiled.tier1_principles)

        # VSCode tasks (if scripts generated)
        if compiled.scripts:
            import json
            tasks = {
                "version": "2.0.0",
                "tasks": [
                    {
                        "label": script.name,
                        "type": "shell",
                        "command": script.code
                    }
                    for script in compiled.scripts
                ]
            }
            (output_dir / ".vscode/tasks.json").write_text(json.dumps(tasks, indent=2))
