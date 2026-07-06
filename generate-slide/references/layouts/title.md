# 简单布局：title / section / quote / qa

这四种布局结构简单，无 block 内容。

---

## title — 封面

```yaml
layout: title
title: "PPT 标题"
subtitle: "副标题（可选）"
background: "#1e293b"     # 颜色值或图片路径，可选
text_color: white         # 可选
```

用途：封面页，通常第一页。

---

## section — 章节过渡

```yaml
layout: section
title: "第一章：背景"
subtitle: "说明文字（可选）"
background: "#0f172a"
```

用途：多章节 PPT 的章节分隔页。

---

## quote — 引言

```yaml
layout: quote
text: "好的架构不是设计出来的，而是演化出来的。"
author: "— 某人"          # 可选
background: "#1e293b"
```

用途：突出一句话或金句。

---

## qa — 结尾

```yaml
layout: qa
text: "Q & A"             # 可选，默认显示 Q&A
background: "#020617"
```

用途：结尾页，通常最后一页。
