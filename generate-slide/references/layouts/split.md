# split — 左右分栏页

标题 + 左右两个 block，中间有分隔线。适合对比、并列说明场景。

```yaml
layout: split
title: "页面标题"
ratio: "50/50"         # 左/右宽度比，默认 50/50
content_width: 800     # 内容区最大宽度（px），默认 800
background: ""         # 可选
left:
  type: <block-type>
  # ... block 具体参数
right:
  type: <block-type>
  # ... block 具体参数
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 页面标题，必填 |
| `ratio` | string | 左/右宽度比，如 `"40/60"`，默认 `"50/50"` |
| `content_width` | number | 内容区宽度上限（px），默认 800 |
| `background` | string | 背景色或图片路径 |
| `left` | object | 左侧内容块，见 blocks/ 下各文件 |
| `right` | object | 右侧内容块，见 blocks/ 下各文件 |

## 适用场景

- 方案对比（方案A vs 方案B）
- Before / After
- 问题 + 解法
- 指标 + 说明

## 示例

```yaml
layout: split
title: "重构前后对比"
ratio: "50/50"
left:
  type: bullets
  left_border: "#ef4444"
  items:
    - text: 重构前
      items:
        - 单体架构，耦合严重
        - 部署频率每月一次
        - 故障恢复平均 4 小时
right:
  type: bullets
  left_border: "#22c55e"
  items:
    - text: 重构后
      items:
        - 微服务，独立部署
        - 每日多次发布
        - 故障恢复平均 15 分钟
```

---

```yaml
layout: split
title: "核心指标"
ratio: "40/60"
left:
  type: kpi
  kpis:
    - value: "99.9%"
      label: SLA 可用性
      color: green
    - value: "18ms"
      label: P99 延迟
      color: blue
right:
  type: markdown
  content: |
    ## 关键改进

    - 引入多活架构，消除单点故障
    - 缓存命中率从 **62%** 提升至 **91%**
    - 数据库连接池优化，慢查询减少 **73%**
```
