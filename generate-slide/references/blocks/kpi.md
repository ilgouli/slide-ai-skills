# kpi — 关键指标卡片

```yaml
type: kpi
kpis:
  - value: "98.5%"
    label: 完成率
    color: green
    sub: "+2.1% vs 上月"
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `kpis` | array | 指标列表，必填，建议 2-4 个 |
| `kpis[].value` | string | 主数值，必填 |
| `kpis[].label` | string | 指标名称，必填 |
| `kpis[].color` | string | 颜色：`blue` \| `green` \| `yellow` \| `gray` |
| `kpis[].sub` | string | 副文字，如环比变化 |

## 示例

```yaml
type: kpi
kpis:
  - value: "1,240"
    label: 日活用户
    color: blue
    sub: "+8% WoW"
  - value: "12ms"
    label: P99 延迟
    color: green
    sub: "目标 <20ms ✓"
  - value: "99.95%"
    label: 可用性
    color: green
  - value: "3.2"
    label: 告警次数
    color: yellow
    sub: "较上月 -40%"
```
