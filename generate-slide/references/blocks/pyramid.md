# pyramid — 金字塔图（SmartArt）

用于展示层级关系，从上到下由小到大排列。

```yaml
type: pyramid
items:
  - label: 顶层（最小）
  - label: 中层
  - label: 底层（最大）
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `items` | array | 层级列表，从上到下，必填，建议 3-5 层 |
| `items[].label` | string | 层级名称，必填 |
| `items[].detail` | string | 层级说明，可选 |
| `color` | string | 主色调 |

## 示例

```yaml
type: pyramid
color: blue
items:
  - label: 战略目标
    detail: 公司愿景与使命
  - label: 业务策略
    detail: 核心增长方向
  - label: 产品路线图
    detail: 季度 OKR
  - label: 功能迭代
    detail: Sprint 任务
  - label: 日常运营
    detail: 监控与维护
```
