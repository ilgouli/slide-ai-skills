# single — 单 block 页

一个标题 + 一个 block，最常用的内容页布局。

```yaml
layout: single
title: "页面标题"
align: top                # top | center（默认 center）
content_width: 800        # 内容区最大宽度（px），默认 800
background: ""            # 可选
text_color: white         # 可选，影响标题和 block 内文字
block:
  type: <block-type>
  # ... block 具体参数
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 页面标题，必填 |
| `align` | `top` \| `center` | block 垂直对齐，默认居中 |
| `content_width` | number | 内容区宽度上限（px），默认 800 |
| `background` | string | 背景色或图片路径 |
| `text_color` | string | 标题和文字颜色 |
| `block` | object | 唯一内容块，见 blocks/ 下各文件 |

## 示例

```yaml
layout: single
title: "系统架构"
align: top
block:
  type: arch
  layers:
    - label: 前端
      items: [React, Tailwind]
    - label: 后端
      items: [FastAPI, SQLite]
```
