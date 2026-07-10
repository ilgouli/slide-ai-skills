# code block

代码展示块，深色背景 + 语法高亮，适合技术分享类幻灯片展示代码片段。

## 必填字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `type` | string | 固定为 `code` |
| `language` | string | 语言标识符，如 `python` / `typescript` / `bash` / `json` / `yaml` / `java` / `sql` |
| `content` | string | 代码内容，使用 YAML 块标量（`|`）保留缩进 |

## 可选字段

| 字段 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `caption` | string | - | 顶部标题栏右侧说明文字 |
| `show_line_numbers` | boolean | `false` | 是否显示行号 |
| `left_border` | string | - | 继承自 BlockBase，左侧装饰线颜色 |

## 示例

### 基础代码块

```yaml
layout: single
block:
  type: code
  language: python
  content: |
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
```

### 带标题和行号

```yaml
layout: split
left:
  type: bullets
  items:
    - title: "递归实现"
      body: "简洁但存在重复计算"
    - title: "时间复杂度"
      body: "O(2^n)"
right:
  type: code
  language: python
  caption: "fibonacci.py"
  show_line_numbers: true
  content: |
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
```

### JSON 配置展示

```yaml
layout: single
block:
  type: code
  language: json
  caption: "schema.json"
  content: |
    {
      "label": "Agent",
      "id_field": "class_name",
      "extraction_logic": "Find classes inheriting BaseAgent"
    }
```

## 使用建议

- 代码不超过 20 行，超出部分在幻灯片中需要滚动
- 配合 `split` layout 使用效果最佳：左侧说明，右侧代码
- `language` 填写小写语言名，不支持的语言会降级为纯文本展示
