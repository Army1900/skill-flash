# Skill Flash 完整使用指南

完整指南：如何使用 skill-optimization 和 skill-burning 工具来管理和优化你的 AI 技能。

---

## 📚 项目概览

```
skill-flash/
├── skill-compilation/       # 技能编译工具
│   ├── SKILL.md             # 编译技能的主文件
│   └── naming-convention.md # 命名规范
│
├── skill-burning/           # 技能烧录工具
│   └── SKILL.md             # 烧录技能的主文件
│
├── verification/            # 验证工具
│   ├── verify.py            # 验证脚本
│   ├── standard.md          # 验证标准
│   └── explanation-impact.md
│
└── demo/                    # 示例和演示
    ├── original/
    ├── optimized/
    └── balanced/
```

---

## 🎯 核心概念

### 什么是 Skill Optimization（技能编译）？

**目的**：让技能消耗更少 token，执行更快

**原理**：
```
原始技能 (1000+ tokens)
  ↓ 编译
核心原则 (嵌入系统提示，0 token)
脚本化规则 (自动执行，不消耗 token)
简化技能 (只处理边缘情况，~300 tokens)
```

**收益**：
- Token 节省：15-40%
- 执行速度：脚本自动执行
- 质量保证：验证工具确保不丢失功能

### 什么是 Skill Burning（技能烧录）？

**目的**：让技能成为项目的自动行为

**原理**：
```
项目现有指南
  ↓ 分析风格和结构
技能原则
  ↓ 融合集成
更新后的指南
```

**收益**：
- 技能自动应用，无需手动调用
- 自然融入项目风格
- 跨平台一致性

---

## 🚀 快速开始

### 场景1：编译一个技能

```
你: "帮我优化 TDD 技能"

模型使用 skill-compilation：
1. 读取 skills/tdd/SKILL.md
2. 分析结构和内容
3. 询问优化策略（默认：balanced）
4. 生成 skills/tdd-balanced/ 文件夹
   - SKILL.md（优化后的内容）
   - scripts/（生成的脚本）
5. 验证质量
6. 生成报告

你：
- 查看 skills/tdd-balanced/SKILL.md
- 对比：diff skills/tdd/SKILL.md skills/tdd-balanced/SKILL.md
- 满意则：cp -r skills/tdd-balanced/* skills/tdd/
```

### 场景2：烧录技能到项目

```
你: "把 TDD 原则烧录到这个项目"

模型使用 skill-burning：
1. 读取项目配置（CLAUDE.md, .cursorrules 等）
2. 分析项目风格和结构
3. 读取 TDD 技能原则
4. 找到集成点
5. 匹配风格
6. 更新配置文件
7. 验证质量

你：
- 查看更新后的配置
- 验证技能现在自动应用
- 如有问题，使用备份回滚
```

### 场景3：验证优化效果

```
你: "验证这个优化是否成功"

运行验证工具：
python3 verification/verify.py \
  skills/tdd/SKILL.md \
  skills/tdd-balanced/SKILL.md

输出：
- 功能完整性：分数
- Token 效率：分数
- 安全性：分数
- 总分：PASSED/FAILED
```

---

## 📋 详细使用指南

### 第一步：准备你的技能

你的技能应该是一个文件夹，包含：

```
your-skill/
├── SKILL.md             # 主文件（必需）
├── scripts/             # 可选的脚本
├── examples/            # 可选的示例
└── references/          # 可选的参考文档
```

### 第二步：编译技能

**方式1：通过对话（推荐）**

```
你: "使用 skill-compilation 优化我的 TDD 技能"

模型会：
1. 读取 skills/tdd/SKILL.md
2. 默认使用 balanced 策略
3. 生成 skills/tdd-balanced/
```

**方式2：直接调用技能**

```
# 在支持技能的 AI 工具中
/skill-compilation skills/tdd/

或

# 在 Claude 中启用技能
```

### 第三步：查看和选择

```bash
# 查看原始技能
cat skills/tdd/SKILL.md

# 查看编译后的技能
cat skills/tdd-balanced/SKILL.md

# 对比差异
diff skills/tdd/SKILL.md skills/tdd-balanced/SKILL.md

# 查看生成的脚本
ls skills/tdd-balanced/scripts/

# 查看报告
cat skills/tdd-balanced/report.md
```

### 第四步：选择使用的版本

**选项A：替换原始技能**
```bash
cp -r skills/tdd-balanced/* skills/tdd/
```

**选项B：使用编译版本**
```bash
# 在你的工具中，将技能路径改为：
skills/tdd-balanced/SKILL.md
```

**选项C：尝试不同策略**
```bash
# 生成多个版本
skills/tdd-aggressive/
skills/tdd-conservative/

# 对比选择
diff skills/tdd/SKILL.md skills/tdd-aggressive/SKILL.md
diff skills/tdd/SKILL.md skills/tdd-balanced/SKILL.md
```

---

## 🔧 实际工作流

### 工作流 1：优化现有技能

```
1. 识别需要优化的技能
   → 技能文件很大（>500 行）
   → Token 消耗高

2. 运行 skill-compilation
   → 选择优化策略

3. 验证优化结果
   → python3 verification/verify.py ...

4. 测试编译后的技能
   → 确保功能正常

5. 部署编译后的技能
   → 替换原技能或使用新路径
```

### 工作流 2：从零创建新技能

```
1. 创建技能文件夹
   mkdir -p skills/my-skill

2. 编写 SKILL.md
   # 遵循现有技能格式

3. 使用 skill-burning 烧录到项目
   # 融合到项目行为模式中

4. 验证烧录效果
   # 确保自然集成

5. 使用技能
   # 现在技能成为自动行为
```

### 工作流 3：维护技能

```
1. 技能变得太大？
   → 使用 skill-compilation 优化

2. 需要跨平台转换？
   → skill-compilation 支持 Claude/OpenAI/Cursor

3. 功能丢失了？
   → 使用 verification 工具检查
   → 对比原版本修复

4. 需要回退？
   → 使用备份的原始技能
```

---

## 📊 优化策略对比

| 策略 | Token 节省 | 解释能力 | 推荐场景 |
|------|-----------|---------|---------|
| **conservative** | ~5% | ✅ 完整保留 | 保守优化 |
| **balanced** | ~15% | ✅ 保留关键 | ⭐ 默认推荐 |
| **aggressive** | ~40% | ⚠️ 可能丢失 | Token 紧张时 |

---

## 🎓 典型使用案例

### 案例1：开发团队优化技能

```
问题：团队使用的 TDD skill 太长，每次调用消耗大量 token

步骤：
1. 使用 skill-compilation 编译技能
2. 验证功能完整性
3. 团队测试编译后的技能
4. 满意后替换原技能
5. 团队节省 token，提高效率
```

### 案例2：跨项目统一标准

```
问题：不同项目有不同的代码审查流程

步骤：
1. 使用 skill-burning 将统一标准烧录到各项目
2. 每个项目保持自己的风格
3. 统一的核心原则自动应用
4. 项目特色得到保留
```

### 案例3：技能迁移

```
问题：将 Claude skill 转换为 Cursor 格式

步骤：
1. 使用 skill-compilation
2. 选择目标平台：Cursor
3. 自动转换格式
4. 验证转换效果
5. 部署到 Cursor 项目
```

---

## ⚠️ 常见问题

### Q1: 编译后的技能丢失了功能？

**A**: 使用验证工具检查：
```bash
python3 verification/verify.py \
  skills/tdd/SKILL.md \
  skills/tdd-balanced/SKILL.md

如果 status 是 FAILED，检查：
- 功能完整性分数
- 丢失了什么内容
- 考虑使用更保守的策略
```

### Q2: 如何回退到原始技能？

**A**: 总是保留原始文件夹：
```bash
# 方式1：重新使用原始
cp -r skills/tdd/* skills/tdd-balanced/

# 方式2：如果备份了
cp -r skills/tdd.backup/* skills/tdd/

# 方式3：删除编译版本
rm -rf skills/tdd-balanced/
```

### Q3: 能多次编译同一个技能吗？

**A**: 可以，每次生成不同文件夹：
```bash
skills/tdd-balanced/    # 第一次编译
skills/tdd-aggressive/  # 第二次尝试
skills/tdd-v2/         # 改进后再次编译
```

### Q4: 如何对比两个版本？

**A**: 使用 diff 或可视化工具：
```bash
# 比较核心文件
diff skills/tdd/SKILL.md skills/tdd-balanced/SKILL.md

# 或者比较整个文件夹
diff -r skills/tdd/ skills/tdd-balanced/

# 可视化对比（IDE 支持）
```

### Q5: 编译会影响技能的功能吗？

**A**: 平衡优化不会，激进优化可能会。验证工具会告诉你：
- 功能完整性：40/40 分
- 如果 <40 分，说明有功能丢失
- 应该使用更保守的策略

---

## 🎯 推荐使用路径

### 新手路径

```
1. 学习阶段：使用现有技能，了解效果
2. 优化阶段：编译技能，选择 balanced 策略
3. 验证阶段：确认功能完整
4. 部署阶段：替换原技能，开始使用
5. 维护阶段：根据需要调整
```

### 高级路径

```
1. 分析：识别哪些技能需要优化
2. 实验：尝试不同的优化策略
3. 对比：使用验证工具对比效果
4. 定制：根据项目需求调整
5. 自动化：集成到 CI/CD 流程
```

---

## 📖 进一步学习

### 相关文档

- `skill-compilation/SKILL.md` - 编译工具详细指南
- `skill-burning/SKILL.md` - 烧录工具详细指南
- `verification/standard.md` - 验证标准
- `demo/balanced/tdd.md` - 平衡优化示例

### 实践建议

1. **从示例开始**：先看 demo/ 中的例子
2. **小步尝试**：先编译简单技能
3. **验证习惯**：优化后总是验证
4. **保留备份**：永远保留原始版本
5. **记录经验**：记录什么优化有效

---

## 🤝 获取帮助

如果遇到问题：

1. **检查验证结果**：确保验证通过
2. **对比原始版本**：看是否有内容丢失
3. **尝试不同策略**：保守 → 平衡 → 激进
4. **查看示例**：demo/ 文件夹有完整示例

---

## 🚀 开始使用

```
你: "帮我编译这个技能"
→ 模型使用 skill-compilation

你: "验证一下优化效果"
→ 运行 verification/verify.py

你: "把技能烧录到这个项目"
→ 模型使用 skill-burning

就这么简单！
```
