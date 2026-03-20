# Skill Compilation Tools

Tools for optimizing and integrating AI skills across multiple platforms.

## Skills Included

### skill-compilation
Optimize AI skills by restructuring into efficient three-tier architecture.

**Use when:**
- A skill is too long / uses too many tokens
- You want faster skill execution
- You want to convert skills between platforms

**Output:**
- Tier 1: Core principles for system prompt
- Tier 2: Session configuration
- Tier 3: Optimized skill file
- Scripts: Executable rules

### skill-burning
Intelligently integrate skill principles into project behavior.

**Use when:**
- You want skills to be automatic
- You want team standards to be "always on"
- You want to avoid repeated skill loading

**Output:**
- Updated project config files
- Principles blended with existing guidelines
- Natural integration (not append)

## Quick Start

### Compile a Skill

```
You: "Optimize the TDD skill at ~/.claude/plugins/tdd/SKILL.md"

The skill will:
1. Analyze the skill
2. Extract core principles
3. Generate optimized tiers
4. Create executable scripts
5. Output to directory
```

### Burn a Skill

```
You: "Burn the TDD skill into this project"

The skill will:
1. Analyze existing project guidelines
2. Extract skill principles
3. Find natural integration points
4. Match project style
5. Update config files
```

## Supported Platforms

- **Claude** - CLAUDE.md, SKILL.md
- **OpenAI** - GPTs configuration
- **Cursor** - .cursorrules
- **Copilot** - .copilot-instructions.md

## Directory Structure

```
skill-compilation/
├── SKILL.md              # Main compilation guide
├── README.md             # This file
├── specs/                # Technical specifications
│   ├── platforms/        # Platform-specific guides
│   ├── code-examples.py  # Script templates
│   └── quality-checklist.md
├── references/           # Detailed documentation
└── templates/            # Output templates

skill-burning/
├── SKILL.md              # Main burning guide
├── README.md             # This file
├── specs/                # Technical specifications
│   ├── burning-strategies.md
│   ├── verification.md
│   └── platforms/        # Platform-specific guides
└── templates/            # Integration examples
```

## Examples

See `templates/` directories for examples of:
- Optimized skill structure
- Integration before/after
- Platform-specific formats

## Workflow

```
Original Skill
      ↓
skill-compilation (optimize structure)
      ↓
Optimized Skill
      ↓
skill-burning (integrate into project)
      ↓
Automatic Behavior
```

## Contributing

These skills are designed to be executed by LLMs. To improve:

1. Test the skills with real examples
2. Note where the LLM gets confused
3. Clarify those sections
4. Add more examples

## License

MIT
