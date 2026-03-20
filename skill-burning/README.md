# Skill Burning Tools

Intelligently integrate AI skill principles into project behavior patterns.

## What is Skill Burning?

**Skill Burning** = Understanding project behavior + Seamlessly integrating new principles

Unlike simple appending, skill burning:
- Analyzes existing guidelines first
- Finds natural integration points
- Matches project style and format
- Blends principles seamlessly

## When to Use

### Use skill-burning when:
- ✅ You want skills to be "automatic"
- ✅ You want team standards always on
- ✅ You want to avoid repeated skill loading
- ✅ You have project guidelines to enhance

### Use skill-compilation when:
- ✅ A skill is too large
- ✅ You want to optimize token usage
- ✅ You want to convert between platforms

## Quick Start

### Basic Usage

```
You: "Burn the TDD skill into this project"

The skill will:
1. Read your existing guidelines (CLAUDE.md, .cursorrules, etc.)
2. Analyze your project's style and structure
3. Extract core TDD principles
4. Find natural integration points
5. Match your writing style
6. Update config files seamlessly
```

### Specify Depth

```
You: "Burn the code review skill, light integration"
→ Adds only core principles

You: "Burn the testing skill, deep integration"
→ Adds principles + workflows + triggers
```

## How It Works

### 1. Analysis Phase

Read existing behavior files:
- CLAUDE.md
- .cursorrules
- .copilot-instructions.md
- README.md, CONTRIBUTING.md

Build a profile:
- Writing style (tone, voice, format)
- Existing categories
- Structure patterns
- Gaps in coverage

### 2. Integration Phase

Find integration points:
- Related sections
- Matching categories
- Natural flow

Match style:
- Tone (formal/casual/technical)
- Voice (imperative/descriptive)
- Format (bullets/numbered/sections)

### 3. Verification Phase

Check:
- No contradictions
- No redundancy
- Natural flow
- Style consistency
- User approval

## Supported Platforms

| Platform | Config Files | Integration Approach |
|----------|--------------|---------------------|
| **Claude** | CLAUDE.md | Add to relevant sections |
| **Cursor** | .cursorrules | Add to categories or flat list |
| **Copilot** | .copilot-instructions.md | Add to relevant sections |
| **Universal** | README.md, docs/ | Add to guidelines section |

## Examples

### Before Integration

```markdown
# CLAUDE.md

## Working Patterns
- Use feature branches
- Code reviews required

## Testing
- Run tests before commit
```

### After Burning TDD

```markdown
# CLAUDE.md

## Working Patterns
- Use feature branches
- Code reviews required
- Write tests before code ← NEW
- Test-driven development ← NEW

## Testing
- Write tests before implementation ← NEW
- Run tests before commit
- Maintain 80% coverage ← NEW
```

Notice how TDD principles are **blended in**, not appended.

## Key Principles

1. **Analyze first** - Understand before changing
2. **Blend, don't append** - Find natural points
3. **Match style** - Feel like it was always there
4. **Minimal disruption** - Change only what's needed
5. **Verify flow** - Read end-to-end
6. **Get approval** - User validates changes

## Safety

Every burning operation:
- Creates backups (.backup files)
- Documents changes (integration record)
- Provides rollback instructions
- Gets user approval before finalizing

## Directory Structure

```
skill-burning/
├── SKILL.md                      # Main burning guide
├── README.md                     # This file
├── specs/
│   ├── burning-strategies.md     # Detailed strategies
│   ├── verification.md           # How to verify
│   └── platforms/
│       ├── claude-burn.md        # Claude specifics
│       └── cursor-burn.md        # Cursor specifics
└── templates/
    ├── claude/
    │   └── integration-example.md
    └── cursor/
        └── integration-example.md
```

## Comparison: Compilation vs Burning

| Aspect | Compilation | Burning |
|--------|-------------|---------|
| Goal | Optimize tokens | Make automatic |
| Output | Multiple files | Config updates |
| Duration | Per session | Permanent |
| Best For | Large skills | Core principles |
| Changes | Creates new structure | Enhances existing |

**Can combine both:**
1. Compile skill (extract core principles)
2. Burn principles (integrate into project)

## Workflow

```
Original Skill
      ↓
skill-compilation (extract core)
      ↓
Core Principles
      ↓
skill-burning (integrate)
      ↓
Automatic Behavior
```

## Contributing

To improve these skills:

1. Test with real projects
2. Note where integration feels unnatural
3. Add strategies for common patterns
4. Expand platform support

## License

MIT
