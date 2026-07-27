# markdown — Markdown 文本块

```yaml
type: markdown
content: |
  Markdown 内容，支持标准语法
font_size: 0.85rem        # 可选，字体大小
```

## 支持语法

- `**加粗**`、`*斜体*`
- 无序列表 `- item`
- 有序列表 `1. item`
- 代码块 ` ```lang ``` `
- 引用 `> text`
- 表格
- 文件链接 `[文件名](file:assets/x.md)`，点击弹框展示文件内容

## 文件链接

用 `[文件名](file:assets/<name>)` 引用 `assets/` 下的文本文件，
点击后弹框显示内容。支持 `.md`（渲染富文本）、`.json`（格式化）、
`.yaml`/`.yml`（原样）。文件需随 deck 上传（放 `assets/` 子目录）。

```yaml
content: |
  详见 [SKILL.md](file:assets/SKILL.md) 与
  [config.json](file:assets/config.json)
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `content` | string | Markdown 文本，必填 |
| `font_size` | string | 字体大小，如 `0.85rem`，默认继承 |
| `left_border` | string | 左侧竖线颜色 |

## 示例

```yaml
type: markdown
font_size: 0.9rem
content: |
  ## 设计原则

  1. **单一职责**：每个模块只做一件事
  2. **开闭原则**：对扩展开放，对修改关闭

  ```python
  def process(rule: Rule) -> Result:
      return rule.evaluate(context)
  ```
```
