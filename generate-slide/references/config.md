# Slide 配置说明

每个 deck 是一个目录，包含 `_meta.yml` 和若干页面 YAML。

```
conf/slide/<deck>/
  _meta.yml       # deck 元信息
  page1.yml       # 页面
  page2.yml
```

## _meta.yml

```yaml
title: "演示标题"
author: liamzheng
theme: light          # light | dark
background: "/img/bg.jpg"   # 可选，默认背景图
slides:
  - page1
  - page2
```

---

## 页面 layout

### title / section / quote / qa

```yaml
layout: title
title: "标题"
subtitle: "副标题"
background: "#1e293b"   # 颜色或图片路径
text_color: white
```

### single — 单 block

```yaml
layout: single
title: "页面标题"
text_color: white       # 可选，影响标题和 block 内文字
align: top              # 默认居中，top = 顶部对齐
block:
  type: bullets
  # ...
```

### compose — 多 block 行列布局

```yaml
layout: compose
title: "页面标题"
gap: 24                 # 行间距（px），默认 16
align: top              # 默认居中
rows:
  - items:              # 单 block 行 = 普通垂直堆叠
      - type: kpi
        # ...
  - items:              # 多 block 行 = 横向排列
      - type: bullets
        # ...
      - type: markdown
        # ...
    ratios: "60/40"     # 行内宽度比，可选
    gap: 12             # 行内间距，可选
```

---

## 通用 block 字段

| 字段 | 说明 |
|------|------|
| `left_border` | 左侧竖线颜色，如 `"#ef4444"` |

---

## Block 类型

### bullets

```yaml
type: bullets
items:
  - 普通文字
  - text: 带子项
    items:
      - 子项1
```

### markdown

```yaml
type: markdown
content: |
  **加粗**、*斜体*、列表等 Markdown 语法
font_size: 0.85rem      # 可选
```

### kpi

```yaml
type: kpi
kpis:
  - value: "98.5%"
    label: 完成率
    color: green        # blue | green | yellow | gray
    sub: "+2.1% vs 上月"
```

### table

```yaml
type: table
heads: [指标, 本月, 上月]
widths: ["40%", "30%", "30%"]   # 可选
rows:
  - [取消率, 12.3%, 13.1%]
footer: "数据截至 2026-06-28"    # 可选
```

### image

```yaml
type: image
src: "/img/screenshot.png"
caption: 图片说明          # 可选
```

### arch — 架构层次图

```yaml
type: arch
layers:
  - label: 前端层
    items: [React, Tailwind]
  - label: 业务层
    items:
      - [模块A, 模块B]    # 嵌套数组 = 多行
      - [模块C]
    full_width: true      # 可选，该层横跨全宽
sidebar:                  # 可选，右侧竖向标注
  label: 权限控制
  row_start: 1            # 对应 layers 的行号（从1起）
  row_end: 3
```

### flow — ReactFlow 流程图

```yaml
type: flow
viewport:
  x: 20
  y: 50
  zoom: 0.8               # 初始缩放
nodes:
  - id: "1"
    label: 开始
    x: 160
    y: 0
    style: blue           # blue | green | yellow | gray
    type: diamond         # 可选，菱形判断节点
    detail: |             # 可选，悬浮说明
      多行文字
edges:
  - from: "1"
    to: "2"
    animated: true        # 可选，流动动画
    label: 条件           # 可选
    handle: yes           # yes | no，菱形节点出口
    type: step            # step | straight，默认平滑曲线
    style: green          # 可选
```

---

## SmartArt block

所有 SmartArt block 支持：
- `accent`：强调色（默认 `#3b82f6`）
- `left_border`：左侧竖线

### cycle — 循环流程

```yaml
type: cycle
center: 核心主题        # 可选，中心文字
numbered: false         # 默认 false
accent: "#22c55e"
items:
  - label: 步骤A
    detail: 补充说明    # 可选
```

### linear — 横向箭头流程

```yaml
type: linear
numbered: true          # 默认 true
accent: "#3b82f6"
items:
  - label: 需求
    detail: 用户访谈
  - label: 设计
  - label: 开发
  - label: 上线
```

### radial — 放射图

```yaml
type: radial
center: 核心策略        # 必填，中心文字
items:
  - label: 价格优化
    detail: 动态定价
```

### pyramid — 金字塔

```yaml
type: pyramid
inverted: false         # true = 倒三角漏斗形
items:
  - label: 愿景         # items[0] 在顶部
  - label: 目标
  - label: 策略
  - label: 执行
```

### funnel — 漏斗图

```yaml
type: funnel
items:
  - label: 曝光
    value: "120万"      # 可选，右侧标注
  - label: 点击
    value: "34万"
  - label: 下单
    value: "1.1万"
```

### matrix — 2×2 四象限

```yaml
type: matrix
x_axis:
  low: 低影响
  high: 高影响
y_axis:
  low: 低紧急
  high: 高紧急
cells:                  # 顺序：左上、右上、左下、右下
  - label: 重要紧急
    items: [BRG故障]
  - label: 重要不紧急
    items: [策略优化]
  - label: 不重要紧急
    items: [报表延迟]
  - label: 不重要不紧急
```
