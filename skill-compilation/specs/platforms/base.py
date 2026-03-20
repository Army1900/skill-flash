"""
Base platform adapter interface.

All platform adapters must implement this interface.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from pathlib import Path


@dataclass
class Skill:
    """Universal skill representation."""
    name: str
    description: str
    content: str
    principles: List[str]          # Core principles (Tier 1)
    rules: List[Dict[str, Any]]    # Structured rules
    workflows: List[Dict[str, Any]]  # Multi-step workflows
    decisions: List[Dict[str, Any]]  # Decision points
    metadata: Dict[str, Any]


@dataclass
class ScriptableRule:
    """A rule that can be converted to an executable script."""
    name: str
    check: str                      # What to check
    language: str                   # python, bash, javascript
    code: str                       # Executable code
    tier: int                       # 1, 2, or 3


@dataclass
class CompiledOutput:
    """Output from skill compilation."""
    tier1_principles: str            # For embedding in system prompt
    tier2_session: str               # Session-level config
    tier3_skill: str                 # Optimized skill file
    scripts: List[ScriptableRule]    # Generated scripts
    report: Dict[str, Any]           # Optimization report


class PlatformAdapter(ABC):
    """Abstract base class for platform adapters."""

    @property
    @abstractmethod
    def platform_name(self) -> str:
        """Platform identifier."""
        pass

    @property
    @abstractmethod
    def input_extensions(self) -> List[str]:
        """Supported input file extensions."""
        pass

    @abstractmethod
    def parse_skill(self, path: Path) -> Skill:
        """Parse a skill file into universal Skill format."""
        pass

    @abstractmethod
    def extract_tier1(self, skill: Skill) -> str:
        """Extract core principles for Tier 1 (internalized)."""
        pass

    @abstractmethod
    def extract_tier2(self, skill: Skill) -> str:
        """Generate session-level config for Tier 2."""
        pass

    @abstractmethod
    def simplify_tier3(self, skill: Skill) -> str:
        """Simplify skill for Tier 3 (on-demand)."""
        pass

    @abstractmethod
    def identify_scriptable_rules(self, skill: Skill) -> List[ScriptableRule]:
        """Identify rules that can be converted to scripts."""
        pass

    @abstractmethod
    def batch_decisions(self, skill: Skill) -> List[Dict[str, Any]]:
        """Extract and organize decision points for batch collection."""
        pass

    @abstractmethod
    def format_output(self, compiled: CompiledOutput, output_dir: Path) -> None:
        """Format and write compiled output for this platform."""
        pass

    def estimate_tokens(self, text: str) -> int:
        """Estimate token count (rough approximation)."""
        # Simple heuristic: ~4 chars per token
        return len(text) // 4

    def generate_report(self, original: Skill, compiled: CompiledOutput) -> Dict[str, Any]:
        """Generate optimization report."""
        original_tokens = self.estimate_tokens(original.content)

        tier1_tokens = self.estimate_tokens(compiled.tier1_principles)
        tier2_tokens = self.estimate_tokens(compiled.tier2_session)
        tier3_tokens = self.estimate_tokens(compiled.tier3_skill)

        return {
            "platform": self.platform_name,
            "original_tokens": original_tokens,
            "compiled_tokens": {
                "tier1": tier1_tokens,
                "tier2": tier2_tokens,
                "tier3": tier3_tokens,
                "total": tier1_tokens + tier2_tokens + tier3_tokens
            },
            "scripts_generated": len(compiled.scripts),
            "optimization_ratio": round(
                (tier1_tokens + tier2_tokens + tier3_tokens) / original_tokens, 2
            ),
            "recommendations": self._generate_recommendations(original, compiled)
        }

    def _generate_recommendations(self, original: Skill, compiled: CompiledOutput) -> List[str]:
        """Generate optimization recommendations."""
        recommendations = []

        if len(compiled.scripts) > 0:
            recommendations.append(
                f"Generated {len(compiled.scripts)} executable scripts "
                f"for faster, deterministic execution"
            )

        if compiled.tier1_principles:
            recommendations.append(
                "Core principles extracted for system prompt embedding (zero token cost)"
            )

        if len(compiled.scripts) == 0 and len(original.rules) > 5:
            recommendations.append(
                "Consider adding more structured rules to enable script generation"
            )

        return recommendations
