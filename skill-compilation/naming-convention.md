# Skill Folder Naming Convention

Skills are folders, not files. Use folder names to indicate compiled variants.

## Convention

```
[skill-name]-[strategy]/
├── SKILL.md              # Optimized skill content
├── scripts/              # Generated scripts
├── references/           # Supporting docs
└── examples/             # Simplified examples
```

## Examples

```
skills/
├── tdd/                      ← Original skill
│   ├── SKILL.md
│   ├── scripts/
│   └── examples/
│
├── tdd-balanced/              ← Compiled (recommended)
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── check_coverage.sh
│   │   └── validate_tests.py
│   └── examples/
│
├── tdd-aggressive/            ← Alternative strategy
│   ├── SKILL.md
│   └── scripts/
│
└── tdd-conservative/          ← Another alternative
    └── SKILL.md
```

## Usage Workflow

```
1. 编译
   compile_skill skills/tdd/
   → 生成 skills/tdd-balanced/

2. 对比
   diff skills/tdd/SKILL.md skills/tdd-balanced/SKILL.md

3. 使用
   # 方法1: 更新原技能文件夹
   cp -r skills/tdd-balanced/* skills/tdd/

   # 方法2: 切换到编译版本
   cd skills/tdd-balanced/

4. 清理
   rm -rf skills/tdd-balanced/
```

## Benefits

- ✅ Skills remain self-contained
- ✅ Scripts and examples stay with the skill
- ✅ Easy to compare entire skill folders
- ✅ Can have multiple variants side-by-side
- ✅ Original skill folder untouched
