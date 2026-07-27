# compose — 多 block 行列布局

一个标题 + 多行内容，每行可包含一个或多个 block 横向排列。

```yaml
layout: compose
title: "页面标题"
align: top                # top | center（默认 center）
gap: 16                   # 行间距（px），默认 16
cell_title:               # 单元格标题样式（可选，配一次作用于全部）
  size: sm                # sm / base / lg，默认 sm
  accent: true            # 是否显示左竖线，默认 true
  color: ""               # 竖线+文字颜色，默认 var(--accent)
content_width: 900        # 内容区最大宽度，默认 800
background: ""
text_color: ""
rows:
  - items:
      - title: 核心指标     # 单元格标题（可选）
        block:
          type: <block-type>
          # ...
  - items:
      - type: bullets       # 不写 title 即无标题（老写法兼容）
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
| `rows[].items` | array | 本行的 block 列表，必填。支持直接 InnerBlock 或 `{ title, block }` 形态 |
| `rows[].ratios` | string | 行内宽度比，如 `"60/40"`，仅多 block 行有效 |
| `rows[].gap` | number | 行内 block 间距（px） |
| `gap` | number | 行间距（px），默认 16 |
| `cell_title` | object / false | 单元格标题样式，配一次作用于全部。`false` 关闭标题 |
| `cell_title.size` | string | 标题字号：`sm`/`base`/`lg`，默认 `sm` |
| `cell_title.accent` | boolean | 是否显示左竖线，默认 `true` |
| `cell_title.color` | string | 竖线+文字颜色，默认 `var(--accent)` |

## 单元格标题

每个 item 可加 `title` 显示在 block 上方（小字 + 左竖线，和页面标题呼应）。
样式在 slide 顶层用 `cell_title` 配一次，作用于全部单元格，无需每个重复：

```yaml
layout: compose
title: 本季度数据
cell_title:
  size: sm
  accent: true
rows:
  - items:
      - title: 核心指标
        block:
          type: kpi
          kpis:
            - value: "98.5%"
              label: 完成率
      - title: 改进措施
        block:
          type: bullets
          items:
            - 完成率提升 3.2%
    ratios: "55/45"
```

不写 `cell_title` 时默认 `accent: true, size: sm`；写 `cell_title: false` 关闭所有标题。

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
