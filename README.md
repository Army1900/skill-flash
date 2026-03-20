# Skill Flash

Tools for optimizing and integrating AI skills across multiple platforms.

## Overview

**Skill Flash** provides two complementary skills for managing AI agent capabilities:

- **skill-compilation** - Optimize skills into efficient three-tier architecture
- **skill-burning** - Intelligently integrate skills into project behavior

## Philosophy

> **慢编译、快执行**

Complex analysis upfront → Fast, accurate execution thereafter

Just like compiled languages (C++, Go) trade slower compilation for faster execution, these skills invest time in analysis to deliver optimal runtime performance.

## Skills

### skill-compilation

Optimize AI skills by restructuring into efficient three-tier architecture.

**Benefits:**
- Reduce token usage by 70%+
- Faster skill execution
- Automatic script generation
- Cross-platform conversion

**Use when:**
- A skill is too long / uses too many tokens
- You want faster skill execution
- You want to convert skills between platforms

**Output:**
- Tier 1: Core principles for system prompt (zero cost)
- Tier 2: Session configuration (one-time load)
- Tier 3: Optimized skill file (on-demand)
- Scripts: Executable rules

### skill-burning

Intelligently integrate skill principles into project behavior patterns.

**Benefits:**
- Skills become automatic (zero invocation cost)
- Seamless integration with existing guidelines
- Consistent behavior across platforms
- Permanent until rollback

**Use when:**
- You want skills to be "always on"
- You want team standards to be automatic
- You want to avoid repeated skill loading

**Output:**
- Updated project config files
- Principles blended with existing guidelines
- Natural integration (not simple append)

## Supported Platforms

| Platform | Config Files | Status |
|----------|--------------|--------|
| **Claude** | CLAUDE.md, SKILL.md | ✅ Full support |
| **OpenAI** | GPTs configuration | ✅ Full support |
| **Cursor** | .cursorrules | ✅ Full support |
| **Copilot** | .copilot-instructions.md | ✅ Full support |

## Quick Start

### Compile a Skill

```
You: "Optimize the TDD skill"

The skill will:
1. Analyze the skill structure
2. Extract core principles (Tier 1)
3. Generate session config (Tier 2)
4. Create optimized skill (Tier 3)
5. Generate executable scripts
6. Output with quality report
```

### Burn a Skill

```
You: "Burn TDD principles into this project"

The skill will:
1. Analyze existing project guidelines
2. Extract TDD core principles
3. Find natural integration points
4. Match project style and format
5. Update config files seamlessly
6. Verify quality and consistency
```

## Workflow

```
Original Skill
      ↓
skill-compilation (optimize structure)
      ↓
Core Principles + Optimized Skill
      ↓
skill-burning (integrate into project)
      ↓
Automatic Behavior
```

**Combine both:**
1. Compile skill → extract core principles
2. Burn principles → integrate into project
3. Result → Skills are automatic, zero cost

## Directory Structure

```
skill-flash/
├── README.md                    # This file
├── .gitignore
│
├── skill-compilation/           # Compilation tool
│   ├── README.md
│   ├── SKILL.md                 # Main guide
│   ├── examples/                # Complete examples
│   ├── specs/                   # Technical specs
│   │   ├── platforms/           # Platform guides
│   │   ├── code-examples.py     # Script templates
│   │   └── quality-checklist.md
│   ├── references/              # Detailed docs
│   └── templates/               # Output templates
│
└── skill-burning/               # Burning tool
    ├── README.md
    ├── SKILL.md                 # Main guide
    ├── examples/                # Complete examples
    ├── specs/                   # Technical specs
    │   ├── platforms/           # Platform guides
    │   ├── burning-strategies.md
    │   └── verification.md
    └── templates/               # Integration examples
```

## Examples

See `examples/` directories for:
- skill-compilation/examples/tdd-compilation.md
- skill-burning/examples/tdd-burning.md

## Quality Assurance

Both skills include comprehensive quality mechanisms:

- **Coverage checks** - Ensure no content is lost
- **Style matching** - Blend naturally with existing content
- **Verification** - Consistency and flow checks
- **Rollback** - Safe operations with backups

## Contributing

These skills are designed to be executed by LLMs. To improve:

1. Test with real projects and skills
2. Note where the LLM gets confused
3. Clarify those sections
4. Add more examples
5. Expand platform support

## License

MIT

## Repository

https://github.com/Army1900/skill-flash
