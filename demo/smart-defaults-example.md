# 智能默认优化示例

## 核心改进

从"表格收集"改为"智能默认 + 可选配置"

---

## 对比

### 之前：表格格式

```markdown
| Decision | Options | Default | Your Choice |
|----------|---------|---------|-------------|
| Framework | pytest, jest, go test | auto | |
| Coverage | 80%, 90%, 100% | 80% | |

Please provide your choices:
```

**问题**：
- 用户不知道输入格式
- AI 可能还是逐个问
- 表格显示问题

---

### 现在：智能默认

```markdown
## Configuration

**Smart defaults** (work well for most projects):
- Framework: auto-detected (Python→pytest, JS→Jest)
- Coverage: 80%
- Mock: yes

I'll start with these. To customize, say "config".
```

**优势**：
- ✅ 零配置启动（大部分情况）
- ✅ 明确的退出路径（"say config"）
- ✅ 需要时清晰指令

---

## 实际对话示例

### 场景 1：用户满意默认值

```
用户: 使用 TDD 添加用户登录功能

AI: [看到技能有智能默认]
    检测到 Python 项目，使用 pytest。
    覆盖率目标 80%，使用 mock 隔离测试。
    开始写测试...

[立即开始工作，零延迟]
```

**耗时：~0 秒**

---

### 场景 2：用户需要自定义

```
用户: 使用 TDD 添加用户登录功能

AI: 检测到 Python 项目，使用 pytest，覆盖率 80%。
    开始工作...

用户: 等等，我需要 90% 覆盖率

AI: 好的，覆盖率改为 90%。
    [继续工作]

[只有 1 次中断]
```

**耗时：~10 秒**

---

### 场景 3：用户主动配置

```
用户: config

AI: **Configuration options**:

    To change settings, provide in ONE message:
    ```
    framework, coverage%, mock_strategy
    ```
    Example: `jest, 90%, real`

    Or set individually:
    - Framework: pytest, jest, go test, junit
    - Coverage: 80%, 90%, 100%
    - Mock: mock, real, hybrid

用户: pytest, 90%, mock

AI: 收到。使用 pytest，90% 覆盖率，mock 策略。
    准备好后告诉我任务。

[1 次交互完成全部配置]
```

**耗时：~30 秒**

---

## 实现原理

### 编译时识别

```python
# 分析原始技能中的决策点

原始: "Ask user: Which testing framework?"
分析:
  - 能从上下文检测吗？能（语言、文件类型）
  - 有明显默认值吗？有（每个语言的主流框架）
  - → 智能默认

原始: "Ask user: What project name?"
分析:
  - 能从上下文检测吗？不能
  - 有明显默认值吗？没有
  - → 保留为运行时问题
```

### 生成输出

```markdown
## Configuration

**Smart defaults**:
- [可检测的决策]: auto-detected [说明]
- [有标准值的决策]: [业界标准] [说明]

I'll start with these. To customize, say "config".

---

[如果用户说 "config"]

**Configuration options**:

To change settings, provide in ONE message:
```
[格式说明]
```

[选项列表]

Your config:
```

---

## 设计原则

### 1. 默认优先

大部分用户不需要配置。好的默认值 > 强制选择。

```
❌ "请选择测试框架：pytest/unittest/nose2"
✅ "使用 pytest（Python 标准）。如需更改说 'config'"
```

### 2. 可检测则自动

能从项目检测的，不要问：

```
❌ "你的项目用什么语言？"
✅ [检测到 .py 文件] "使用 pytest"

❌ "你用 React 还是 Vue？"
✅ [检测到 package.json 中有 react] "使用 React hooks"
```

### 3. 退出路径清晰

让用户知道如何自定义：

```
✅ "To customize, say 'config'"
✅ "To change, say 'settings'"
✅ "For options, say 'help'"
```

### 4. 一次交互收集

用户主动配置时，一次性收集：

```
❌ "框架？" [用户回答] "覆盖率？" [用户回答]
✅ "提供配置：framework, coverage%"
   用户: "pytest, 90%"
```

---

## 适用决策类型

| 决策类型 | 处理方式 | 示例 |
|---------|---------|------|
| 可检测 | 智能默认 | 框架（检测语言） |
| 有标准 | 智能默认 | 覆盖率（80% 行业标准） |
| 无标准，常改 | 可选配置 | 日志级别 |
| 依赖任务 | 运行时询问 | "这个 API 需要认证吗？" |
| 项目特定 | 运行时询问 | "项目名称是什么？" |

---

## Token 节省

```
原始（逐个问）:
- 3 个问题 × 50 tokens = 150 tokens
- 加上用户响应 = ~300 tokens/交互

智能默认:
- 默认情况：0 tokens（立即开始）
- 需要配置：1 次交互 ~100 tokens

节省: 66-100%
```

---

## 速度提升

```
逐个问: 3 个问题 × 30 秒 = 90 秒
智能默认: 0 秒（大部分情况）

加速: 无限大（90 → 0）
```

---

## 实际效果

### 编译前（原始 TDD）

```
# Test-Driven Development

## Testing Frameworks
Before starting, determine which testing framework to use:
- Python: pytest or unittest
- JavaScript: Jest or Mocha
- Go: go test
- Java: JUnit
```

**执行时**：
```
AI: 哪个测试框架？
用户: pytest
AI: 好的，开始...
```

### 编译后（智能默认）

```
## Configuration

**Smart defaults**:
- Framework: auto-detected (Python→pytest, JS→Jest)
- Coverage: 80%
- Mock: yes

I'll start with these. To customize, say "config".
```

**执行时**：
```
AI: [检测到 Python] 使用 pytest，覆盖率 80%。
    开始写测试...
[立即工作]
```

---

## 总结

智能默认模式的核心价值：

1. **零配置启动** - 大部分用户无需任何配置
2. **明确退出路径** - 需要时清楚如何配置
3. **自动检测优先** - 能猜的就不问
4. **一次交互收集** - 配置时一次完成

相比表格格式：
- ✅ 更快（默认情况 0 秒 vs 30 秒）
- ✅ 更简单（无输入格式困惑）
- ✅ 更灵活（可检测 vs 固定表格）

这是**真正实用**的决策优化方案。
