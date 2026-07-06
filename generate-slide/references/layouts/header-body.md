# header-body — 顶部说明 + 主体内容页

标题 + 顶部一行说明文字（副标题/背景交代）+ 主体 block。适合需要先给出上下文再展示内容的场景。

```yaml
layout: header-body
title: "页面标题"
header:
  text: "顶部说明文字（一行）"
content_width: 800     # 内容区最大宽度（px），默认 800
background: ""         # 可选
body:
  type: <block-type>
  # ... block 具体参数
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 页面标题，必填 |
| `header.text` | string | 顶部说明/副标题，必填，建议一行 |
| `content_width` | number | 内容区宽度上限（px），默认 800 |
| `background` | string | 背景色或图片路径 |
| `body` | object | 主体内容块，见 blocks/ 下各文件 |

## 与 single 的区别

- `single`：标题直接接内容，无额外说明层
- `header-body`：标题下先有一行上下文说明（灰色带左侧竖线），再展示内容

## 适用场景

- 需要先交代背景/结论再展示数据
- 引用约束条件后展示方案
- 章节内容页需要补充小标题

## 示例

```yaml
layout: header-body
title: "告警收敛策略"
header:
  text: "背景：高峰期单日触发告警超 3,000 条，大量为噪声，导致 oncall 疲劳"
body:
  type: bullets
  items:
    - text: 分级收敛
      items:
        - P0 告警实时推送，不合并
        - P1/P2 按 5 分钟窗口聚合
    - text: 智能去噪
      items:
        - 相同根因 30 分钟内只推一条
        - 自动关联上下游依赖关系
    - 效果：告警量降低 **87%**，误报率 < 2%
```

---

```yaml
layout: header-body
title: "技术选型结果"
header:
  text: "评估维度：性能、社区活跃度、团队熟悉程度、迁移成本"
body:
  type: table
  heads: [方案, 性能, 社区, 迁移成本, 结论]
  rows:
    - [方案 A (现有), 一般, 高, 低, 保留]
    - [方案 B (候选), 优秀, 高, 中, 采用]
    - [方案 C (候选), 优秀, 低, 高, 放弃]
```
