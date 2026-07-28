# compose — 多 block 行列布局

一个标题 + 多行内容，每行可包含一个或多个 block 横向排列。

```yaml
layout: compose
title: "页面标题"
align: top                # top | center（默认 center）
fill: false                # 行均分高度、单元格撑满（网格场景），默认 false
row_ratios: ""            # 行间高度比，如 "1/2"，需配合 fill，默认均分
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
| `rows[].separator` | `'arrow'` | 替代 `items`，在该位置渲染 ↓ 箭头分隔符 |
| `rows[].color` | string | 箭头颜色：`blue` / `green` / `yellow` / `red` / 任意 CSS 色值 |
| `rows[].size` | string | 箭头大小：`sm` / `md`（默认）/ `lg` |
| `rows[].items` | array | 本行的 block 列表。支持直接 InnerBlock、`{ title, block }` 形态，或 `{ separator: 'arrow', color?, size? }` |
| `rows[].ratios` | string | 行内宽度比，如 `"60/40"`，仅多 block 行有效 |
| `rows[].gap` | number | 行内 block 间距（px） |
| `gap` | number | 行间距（px），默认 16 |
| `fill` | boolean | 行均分高度、单元格撑满，适合 2×2 等网格场景。默认 false |
| `row_ratios` | string | 行间高度比，如 `"1/2"`、`"1/3/1"`，需配合 `fill`。默认均分 |
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

## 示例：2×2 网格（fill 撑满）

多行内容不多时，默认会挤在中心。加 `fill: true` 让行均分高度、单元格撑满：

```yaml
layout: compose
title: "季度概览"
fill: true
cell_title:
  size: sm
  accent: true
rows:
  - items:
      - title: 核心指标
        block:
          type: kpi
          kpis:
            - value: "98%"
              label: 完成率
            - value: "12ms"
              label: 延迟
      - title: 改进措施
        block:
          type: bullets
          items:
            - 完成率提升
            - 延迟下降
  - items:
      - title: 架构变化
        block:
          type: bullets
          items:
            - 多活架构
            - 缓存优化
      - title: 下一步
        block:
          type: bullets
          items:
            - 扩容双机房
            - 灰度新版本
```

`fill: true` 适合 2×2、2×3 等网格场景；内容多的单行布局保持默认（不 fill）即可。

## 示例：行高比（row_ratios）

`fill: true` 默认行均分高度。用 `row_ratios` 指定各行高度比，如
第一行 1 份、第二行 2 份：

```yaml
layout: compose
title: "季度概览"
fill: true
row_ratios: "1/2"        # 第一行:第二行 = 1:2
rows:
  - items:
      - title: 核心指标
        block:
          type: kpi
          kpis:
            - value: "98%"
              label: 完成率
  - items:
      - title: 详细说明
        block:
          type: bullets
          items:
            - 完成率提升
            - 延迟下降
            - 缓存优化
            - 架构升级
```

注意：`row_ratios` 需配合 `fill: true` 才生效（非 fill 模式行高度由内容决定）。
数量需与 `rows` 行数一致。


## 示例：separator 箭头分隔符

`rows` 中插入 `separator: arrow` 渲染 ↓ 箭头；`items` 中插入渲染 → 箭头。
支持 `color`（`blue`/`green`/`yellow`/`red`/CSS 色值）和 `size`（`sm`/`md`/`lg`）。

**行间 ↓ 箭头**（左右分栏，右侧两段内容间加箭头）：

```yaml
layout: compose
title: "用户下单路径"
content_width: 960
align: top
rows:
  - items:
      - type: flow
        # ... 流程图
      - type: bullets
        items:
          - text: "用户特点"
            items: ["需求明确", "价格敏感"]
    ratios: "60/40"
  - separator: arrow            # 行间 ↓ 箭头
    color: blue                 # 可选颜色
    size: lg                    # 可选大小
  - items:
      - type: markdown
        content: ""             # 左列占位保持对齐
      - type: bullets
        items:
          - text: "策略启发"
            items: ["地理位置召回", "价格优势特征"]
    ratios: "60/40"
```

**列间 → 箭头**（同一行 block 之间）：

```yaml
layout: compose
title: "处理流程"
rows:
  - items:
      - type: bullets
        items: ["输入数据", "数据清洗"]
      - separator: arrow        # 列间 → 箭头
        color: green
      - type: bullets
        items: ["特征提取", "模型推理"]
    ratios: "45/10/45"
```
