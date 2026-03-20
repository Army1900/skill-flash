"""
OpenAI GPTs platform adapter.

Handles OpenAI GPTs configuration format (JSON).
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any
from .base import PlatformAdapter, Skill, ScriptableRule, CompiledOutput


class OpenAIAdapter(PlatformAdapter):
    """Adapter for OpenAI GPTs."""

    @property
    def platform_name(self) -> str:
        return "openai"

    @property
    def input_extensions(self) -> List[str]:
        return [".json"]

    def parse_skill(self, path: Path) -> Skill:
        """Parse OpenAI GPT config JSON."""
        content = path.read_text()
        data = json.loads(content)

        # OpenAI GPTs structure
        instructions = data.get("instructions", "")
        name = data.get("name", path.stem)
        description = data.get("description", "")

        # Parse instructions for structure
        principles = self._extract_principles(instructions)
        rules = self._extract_rules(instructions)
        workflows = self._extract_workflows(instructions)
        decisions = self._extract_decisions(instructions)

        return Skill(
            name=name,
            description=description,
            content=instructions,
            principles=principles,
            rules=rules,
            workflows=workflows,
            decisions=decisions,
            metadata={"format": "openai", "config": data}
        )

    def _extract_principles(self, content: str) -> List[str]:
        """Extract principles from instructions."""
        principles = []

        # Look for bullet points or numbered lists at the start
        for match in re.finditer(r'^[\s]*(?:[-*]|\d+\.)\s+(.+?)$', content, re.MULTILINE):
            principle = match.group(1).strip()
            if len(principle) < 200:  # Keep it concise
                principles.append(principle)

        return principles[:10]  # Top 10

    def _extract_rules(self, content: str) -> List[Dict[str, Any]]:
        """Extract rules from instructions."""
        rules = []

        # Look for "must", "should", "always", "never" patterns
        patterns = [
            r'(?:must|should|always|never) (.+?)(?:\.|$)',
            r'Make sure to (.+?)(?:\.|$)',
            r'Ensure (.+?)(?:\.|$)',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                rule_text = match.group(1).strip()
                if len(rule_text) > 10 and len(rule_text) < 200:
                    rules.append({
                        "name": rule_text[:30] + "...",
                        "description": rule_text
                    })

        return rules

    def _extract_workflows(self, content: str) -> List[Dict[str, Any]]:
        """Extract workflows."""
        workflows = []

        # Look for "steps:", "workflow:", or numbered sequences
        step_matches = re.findall(r'(?:step\s+\d+[:.]|^\d+\.)\s*([^\n]+)', content, re.IGNORECASE)
        if len(step_matches) > 2:
            workflows.append({
                "name": "main",
                "steps": step_matches
            })

        return workflows

    def _extract_decisions(self, content: str) -> List[Dict[str, Any]]:
        """Extract decision points."""
        decisions = []

        # Look for "ask user", "request", "confirm" patterns
        patterns = [
            r'(?:ask|request|prompt) (?:the )?user (?:for|to|about) (.+?)(?:\.|$)',
            r'(?:confirm|verify) (.+?) (?:with user)?',
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                decisions.append({
                    "question": match.group(1).strip()
                })

        return decisions

    def extract_tier1(self, skill: Skill) -> str:
        """Extract for OpenAI system message."""
        if not skill.principles:
            return ""

        return f"# Core Principles for {skill.name}\n\n" + \
               "\n".join(f"- {p}" for p in skill.principles[:5])

    def extract_tier2(self, skill: Skill) -> str:
        """Generate actions config."""
        actions = []

        for rule in skill.rules[:3]:
            actions.append({
                "name": rule['name'],
                "description": rule['description']
            })

        return json.dumps({"actions": actions}, indent=2)

    def simplify_tier3(self, skill: Skill) -> str:
        """Simplify instructions."""
        return f"""# {skill.name} (Optimized)

Core principles are embedded in system prompt.

## Remaining Instructions

{chr(10).join(f"- {r['description']}" for r in skill.rules[5:])}
"""

    def identify_scriptable_rules(self, skill: Skill) -> List[ScriptableRule]:
        """Identify scriptable rules (function calling in OpenAI)."""
        scriptable = []

        for rule in skill.rules[:5]:
            # Check if rule could be a function call
            if any(word in rule['description'].lower() for word in
                   ['check', 'verify', 'validate', 'search', 'calculate']):
                scriptable.append(ScriptableRule(
                    name=rule['name'],
                    check="function_call",
                    language="python",
                    code=f"# OpenAI Function: {rule['name']}\n" +
                         f'def {rule["name"].lower().replace(" ", "_")}(args):\n' +
                         f'    """{rule["description"]}"""\n' +
                         f'    pass\n',
                    tier=2
                ))

        return scriptable

    def batch_decisions(self, skill: Skill) -> List[Dict[str, Any]]:
        """Batch decisions for initial form."""
        return [
            {
                "type": "form",
                "title": "Getting Started",
                "fields": [
                    {
                        "name": f"field_{i}",
                        "label": d.get('question', '')[:50],
                        "type": "text"
                    }
                    for i, d in enumerate(skill.decisions[:5])
                ]
            }
        ]

    def format_output(self, compiled: CompiledOutput, output_dir: Path) -> None:
        """Write GPT config output."""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Write optimized config
        config = {
            "name": "Optimized GPT",
            "instructions": compiled.tier3_skill,
            "system_prompt_addition": compiled.tier1_principles,
            "actions": json.loads(compiled.tier2_session) if compiled.tier2_session else []
        }

        (output_dir / "gpt-config.json").write_text(json.dumps(config, indent=2))

        # Write functions (if any)
        if compiled.scripts:
            functions_dir = output_dir / "functions"
            functions_dir.mkdir(exist_ok=True)
            for script in compiled.scripts:
                (functions_dir / f"{script.name}.py").write_text(script.code)

        # Report
        (output_dir / "report.json").write_text(
            json.dumps(compiled.report, indent=2)
        )
