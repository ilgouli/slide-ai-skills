# cycle — 循环图（SmartArt）

用于展示循环/迭代流程。

```yaml
type: cycle
items:
  - label: 阶段名称
    detail: 说明文字     # 可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `items` | array | 循环节点列表，必填，建议 3-6 个 |
| `items[].label` | string | 节点名称，必填 |
| `items[].detail` | string | 节点说明，可选 |
| `color` | string | 主色调，如 `blue`、`green` |

## 示例

```yaml
type: cycle
color: blue
items:
  - label: 需求分析
    detail: 收集用户反馈
  - label: 设计
    detail: 原型 + 技术方案
  - label: 开发
    detail: Sprint 迭代
  - label: 测试
    detail: 自动化 + 人工验收
  - label: 上线
    detail: 灰度发布
  - label: 监控
    detail: 指标 + 告警
```
