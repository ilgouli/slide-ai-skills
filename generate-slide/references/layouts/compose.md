# compose — 多 block 行列布局

一个标题 + 多行内容，每行可包含一个或多个 block 横向排列。

```yaml
layout: compose
title: "页面标题"
align: top                # top | center（默认 center）
gap: 16                   # 行间距（px），默认 16
content_width: 900        # 内容区最大宽度，默认 800
background: ""
text_color: ""
rows:
  - items:
      - type: <block-type>
        # ...
  - items:
      - type: bullets
        # ...
      - type: kpi
        # ...
    ratios: "60/40"       # 行内宽度比，可选
    gap: 12               # 行内间距（px），可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `rows` | array | 行列表，必填 |
| `rows[].items` | array | 本行的 block 列表，必填 |
| `rows[].ratios` | string | 行内宽度比，如 `"60/40"`，仅多 block 行有效 |
| `rows[].gap` | number | 行内 block 间距（px） |
| `gap` | number | 行间距（px），默认 16 |

## 示例：KPI + 说明双列

```yaml
layout: compose
title: "本季度数据"
rows:
  - items:
      - type: kpi
        kpis:
          - value: "98.5%"
            label: 完成率
            color: green
          - value: "12ms"
            label: P99 延迟
            color: blue
  - items:
      - type: bullets
        items:
          - 完成率较上季度提升 3.2%
          - 延迟下降源于缓存优化
      - type: markdown
        content: |
          **下一步**
          - 扩容至双机房
          - 灰度新版本
    ratios: "55/45"
```
