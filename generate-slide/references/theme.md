# theme — 主题配置

`_meta.yml` 的 `theme` 字段控制整个 deck 的视觉风格。
所有组件（布局、卡片、图表、表格等）均通过 CSS 变量响应主题。

## 预设主题

```yaml
theme: light          # 默认白色
theme: dark           # 深色
theme: apple-keynote  # 苹果发布会风（黑底）
theme: deep-blue      # 深海蓝（适合技术汇报）
```

## 覆盖变量

在预设基础上用 `vars` 覆盖任意变量：

```yaml
theme:
  preset: apple-keynote
  vars:
    --surface: "#ffffff"      # 幻灯片背景
    --card-bg: "#f5f5f7"      # 卡片背景
    --text-primary: "#1d1d1f" # 主文字
```

## 可用变量

| 变量 | 含义 |
|---|---|
| `--surface` | 幻灯片背景色 |
| `--card-bg` | 卡片/节点背景 |
| `--card-radius` | 卡片圆角 |
| `--border-color` | 边框、分割线、图表网格 |
| `--text-primary` | 主文字颜色 |
| `--text-secondary` | 次要文字、副标题 |
| `--accent` | 强调色（标题竖线、链接、按钮） |
| `--accent-light` | 强调色浅底（图标背景） |
| `--row-alt` | 表格隔行背景 |

## 示例

```yaml
# _meta.yml
title: "季度汇报"
author: liamzheng
theme: deep-blue
slides:
  - title
  - overview
  - detail
```

自定义暖色风格：

```yaml
theme:
  preset: light
  vars:
    --surface: "#faf7f0"
    --card-bg: "#f5f0e8"
    --accent: "#c2410c"
    --accent-light: "#c2410c1a"
    --border-color: "#e8dfd0"
```
