# funnel — 漏斗图（SmartArt）

用于展示逐层筛选或转化的漏斗流程。

```yaml
type: funnel
items:
  - label: 顶部（最宽）
    value: "10,000"     # 可选，显示数值
  - label: 中层
    value: "2,000"
  - label: 底部（最窄）
    value: "300"
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `items` | array | 漏斗层级列表，从上到下，必填，建议 3-6 层 |
| `items[].label` | string | 层级名称，必填 |
| `items[].value` | string | 显示数值，可选 |
| `color` | string | 主色调 |

## 示例

```yaml
type: funnel
color: blue
items:
  - label: 曝光
    value: "500,000"
  - label: 点击
    value: "25,000"
  - label: 注册
    value: "3,200"
  - label: 激活
    value: "1,100"
  - label: 付费
    value: "280"
```
