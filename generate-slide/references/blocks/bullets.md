# bullets — 要点列表

```yaml
type: bullets
items:
  - 普通文字条目
  - text: 带子项的条目
    items:
      - 子项 1
      - 子项 2
  - 另一条普通文字
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `items` | array | 条目列表，必填 |
| `items[].text` | string | 条目文字（有子项时用此写法） |
| `items[].items` | array | 子条目列表，最多一层嵌套 |
| `left_border` | string | 左侧竖线颜色，如 `"#3b82f6"` |

## 示例

```yaml
type: bullets
left_border: "#3b82f6"
items:
  - 系统支持多租户架构
  - text: 核心模块
    items:
      - 规则引擎：基于 AST 的表达式求值
      - 执行引擎：异步任务队列
  - 已通过 SOC2 Type II 审计
```
