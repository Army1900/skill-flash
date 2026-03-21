# 批量决策点优化示例

## 问题：反复询问降低效率

### 原始技能 (Sequential Questions)

```markdown
# TDD Skill

## Framework Selection
When starting, ask user: Which testing framework?
Options: pytest, unittest, nose2

[User answers: pytest]

## Coverage Requirements
Ask user: What target coverage?
Options: 80%, 90%, 100%

[User answers: 90%]

## Mock Strategy
Ask user: Mock or real dependencies?
Options: mock, real, hybrid

[User answers: mock]

## Test Style
Ask user: Unit or integration tests?

[User answers: unit]

[...Finally starts working...]
```

**问题分析**：
- 4 个问题 = 4 次往返
- 每次等待用户响应
- 中断工作流程
- 总耗时：~4-8 分钟（取决于用户响应速度）

---

## 解决方案：批量收集决策

### 编译后技能 (Batched Decisions)

```markdown
# TDD Skill (Optimized)

## Initial Configuration ⚡

Before starting, I'll collect all preferences at once:

| Decision | Options | Default | Your Choice |
|----------|---------|---------|-------------|
| Framework | pytest, unittest, nose2 | pytest | |
| Coverage | 80%, 90%, 100% | 80% | |
| Mock strategy | mock, real, hybrid | mock | |
| Test style | unit, integration, both | both | |

**Please provide your choices (or press Enter for defaults)**:

```

**用户一次性响应**：
```
1. Framework: [Enter → 使用默认 pytest]
2. Coverage: 90%
3. Mock strategy: [Enter → 使用默认 mock]
4. Test style: [Enter → 使用默认 both]
```

**立即开始工作，无中断！**

---

## 对比分析

### Token 消耗

| 版本 | 决策收集 Token | 总 Token |
|------|--------------|----------|
| 原始 | 4 × 50 = 200 | 648 |
| 编译 | 1 × 80 = 80 | 549 |
| **节省** | **120 tokens (60%)** | **99 tokens (15%)** |

### 执行时间

| 版本 | 决策收集时间 | 假设用户响应时间 |
|------|-------------|-----------------|
| 原始 | 4 次往返 | ~4-8 分钟 |
| 编译 | 1 次收集 | ~30 秒 |
| **加速** | **4x** | **8-16x** |

### 用户体验

| 指标 | 原始 | 编译 |
|------|------|------|
| 上下文切换 | 4 次 | 1 次 |
| 中断感 | 强 | 弱 |
| 默认值使用 | 困难 | 简单 |
| 批量操作 | 不支持 | 支持 |

---

## 实现细节

### 步骤 1: 识别独立决策

分析原始技能，找出可以批量收集的问题：

```
✅ 可批量（无依赖）：
  - 框架选择
  - 覆盖率目标
  - Mock 策略
  - 测试风格

❌ 不可批量（有依赖）：
  - "如果选择 pytest，使用 fixtures 吗？" → 依赖框架选择
  - "集成测试需要数据库？" → 依赖测试风格
```

### 步骤 2: 生成表格格式

```markdown
| Decision | Options | Default | Your Choice |
|----------|---------|---------|-------------|
| Framework | pytest, unittest, nose2 | pytest | |
| Coverage | 80%, 90%, 100% | 80% | |
```

**优势**：
- 视觉清晰，一目了然
- 支持默认值
- 支持部分填写（跳过的使用默认）
- 用户可以预览所有决策

### 步骤 3: 处理条件决策

保留有依赖的问题在流程中：

```markdown
## Initial Decisions
1. Framework [pytest]:

## Runtime Decisions (Conditional)
If framework == "pytest":
  → Ask: Use pytest fixtures? [yes]:
```

---

## 编译前后对比

### 编译前：原始 TDD Skill

```markdown
---
name: tdd
description: Test-driven development workflow
---

# TDD Workflow

## Step 1: Choose Framework
Ask user: Which testing framework?
- pytest (recommended)
- unittest (built-in)
- nose2 (legacy)

## Step 2: Set Coverage Target
Ask user: What coverage target?
- 80% (minimum)
- 90% (good)
- 100% (excellent)

## Step 3: Determine Mock Strategy
Ask user: How to handle dependencies?
- mock (fast, isolated)
- real (slow, realistic)
- hybrid (balanced)

## Step 4: Write First Test
Now write a test for the feature...
```

### 编译后：TDD Skill (Optimized with Batched Decisions)

```markdown
---
name: tdd-balanced
description: Test-driven development (optimized)
has_initial_decisions: true
---

# TDD Workflow (Optimized)

## Initial Configuration ⚡

Collected once at start, then execution flows without interruption:

**Testing Setup**:
| Decision | Options | Default | Your Choice |
|----------|---------|---------|-------------|
| Framework | pytest, unittest, nose2 | pytest | |
| Coverage | 80%, 90%, 100% | 80% | |
| Mock strategy | mock, real, hybrid | mock | |

Provide your choices or press Enter for defaults.

---

## Core Workflow

[Using collected configuration, execute TDD cycle]

### Test First (Using [framework])

Write a test for the functionality:
- If pytest: Use `def test_()` syntax
- If unittest: Use `unittest.TestCase` classes

### Verify Coverage (Target: [coverage]%)

After implementation, check coverage meets target:
```bash
pytest --cov --cov-fail-under=[coverage]
```

### Handle Dependencies (Strategy: [mock_strategy])

- mock: Use pytest-mock for isolation
- real: Use actual dependencies
- hybrid: Mix based on test type
```

---

## 验证效果

### 测试场景

**任务**：使用 TDD 添加一个用户登录功能

**原始技能执行**：
```
AI: Which framework?
User: pytest
AI: What coverage?
User: 90%
AI: Mock strategy?
User: mock
AI: Test style?
User: unit
AI: OK, let's start...
[开始写代码]
```
耗时：~5 分钟（4 次往返）

**编译后技能执行**：
```
AI: Testing Setup:
    Framework [pytest]:
    Coverage [80%]: 90%
    Mock strategy [mock]:

User: [按 Enter 两次，输入 90%]

AI: Got it. Starting TDD with pytest, 90% coverage, mock strategy...
[立即开始写代码]
```
耗时：~30 秒（1 次交互）

**加速：10x**

---

## 使用建议

### 适合批量收集的决策

✅ **工具/框架选择**
- 框架（React/Vue/Svelte）
- 测试工具（pytest/jest/go test）
- 构建工具（webpack/vite/turbopack）

✅ **配置参数**
- 覆盖率目标（80%/90%/100%）
- 日志级别（debug/info/warn）
- 环境选项（dev/staging/prod）

✅ **风格偏好**
- 代码风格（Prettier/ESLint/custom）
- 命名约定（camelCase/snake_case）
- 文件组织（flat/nested）

### 不适合批量收集的决策

❌ **依赖上下文的条件问题**
- "如果使用 React，需要 TypeScript 吗？"（依赖框架）
- "集成测试需要数据库吗？"（依赖测试类型）

❌ **依赖任务细节的问题**
- "这个函数应该返回什么？"（依赖具体需求）
- "如何处理这个错误？"（依赖具体场景）

❌ **依赖执行结果的反馈**
- "测试通过了吗？"（需要运行后才知道）
- "性能可以接受吗？"（需要测量后才知道）

---

## 高级技巧

### 1. 分组决策

把相关决策分组，减少认知负担：

```markdown
## Testing Setup
1. Framework [pytest]:
2. Coverage [80%]:

## Code Quality
3. Linter [eslint]:
4. Formatter [prettier]:
```

### 2. 条件默认值

根据常见组合设置智能默认：

```yaml
defaults:
  minimal:
    framework: pytest
    coverage: "80%"
    mock_strategy: real

  strict:
    framework: pytest
    coverage: "100%"
    mock_strategy: mock

# Ask user: Use minimal or strict defaults?
```

### 3. 配置文件持久化

```markdown
## Configuration

First time? Provide your preferences:
[决策表格]

Existing config found at `.tdd-config.yaml`:
```yaml
framework: pytest
coverage: "90%"
```
Load existing config? [Y/n]:
```

---

## 总结

批量决策点优化的核心价值：

1. **速度提升**：N 个问题 → 1 次交互 = N倍加速
2. **Token 节省**：减少往返对话的冗余 token
3. **体验改善**：减少中断，保持心流
4. **默认友好**：表格格式让默认值更明显

**适用场景**：
- ✅ 有多个独立配置选项的技能
- ✅ 用户可能重复使用相同配置
- ✅ 初始化阶段需要收集多个决策

**实现成本**：
- 识别独立决策：低（分析技能内容）
- 生成批量格式：低（模板化）
- 用户体验提升：高

这是编译优化中**性价比最高**的改进之一。
