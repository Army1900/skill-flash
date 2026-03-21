# File Naming Convention

Simple, strategy-based naming for compiled skills.

## Convention

```
[skill-name].[strategy].md
```

## Examples

```
Original File:
  tdd.md

Compiled Variants:
  tdd.balanced.md      ← Recommended (15% savings)
  tdd.aggressive.md    ← Max savings (~40%)
  tdd.conservative.md  ← Safe (~5% savings)

Usage:
  # Compare
  diff tdd.md tdd.balanced.md

  # Use optimized version
  cp tdd.balanced.md tdd.md

  # Try different strategy
  cp tdd.aggressive.md tdd.md

  # Cleanup
  rm tdd.balanced.md tdd.aggressive.md
```

## Strategy Definitions

| Strategy | Savings | Trade-off | Use When |
|----------|---------|-----------|----------|
| **balanced** | ~15% | Keeps key explanations | Default choice |
| **aggressive** | ~40% | May lose explanations | Token-critical situations |
| **conservative** | ~5% | Very safe, minimal changes | Risk-averse scenarios |

## Directory Structure

```
project/
├── skills/
│   ├── tdd.md              ← Original
│   ├── tdd.balanced.md     ← Compiled (recommended)
│   └── tdd.report.md       ← Compilation report
```

## Alternative: Directory-Based

If you prefer organization by variant:

```
skills/
├── tdd.md                  ← Original
├── compiled/
│   ├── balanced/
│   │   └── tdd.md
│   ├── aggressive/
│   │   └── tdd.md
│   └── conservative/
│       └── tdd.md
```

Choose the style that fits your workflow.

## Quick Reference

```
Single skill, single strategy:
  skill.balanced.md

Single skill, all strategies:
  skill.balanced.md
  skill.aggressive.md
  skill.conservative.md

Comparison:
  diff skill.md skill.balanced.md
```
