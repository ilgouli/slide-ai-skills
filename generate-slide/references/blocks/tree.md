# tree block

树形层级图，自动布局，适合组织架构、技术分类、知识体系等树状结构。

## schema

```yaml
type: tree
nodes:
  - id: root          # 唯一 ID，必填
    label: 根节点      # 显示文字，必填
    subtitle: 张三     # 可选，副标注（小字）
    color: blue        # 可选，节点颜色
                       # blue|green|yellow|red|gray|default
  - id: child
    label: 子节点
    parent: root       # 父节点 ID；根节点不填
  - id: grandchild
    label: 孙节点
    parent: child
accent: "#7C3AED"      # 可选，slide 级颜色自动传入
```

## 参数说明

| 字段 | 类型 | 说明 |
|---|---|---|
| `nodes` | array | 节点列表，必填 |
| `nodes[].id` | string | 节点唯一标识 |
| `nodes[].label` | string | 节点显示文字 |
| `nodes[].subtitle` | string | 副标注，显示在 label 下方 |
| `nodes[].color` | string | 节点颜色，默认继承 slide `color` |
| `nodes[].parent` | string | 父节点 id；不填则为根节点 |

## 示例：组织架构

```yaml
type: tree
nodes:
  - id: ceo
    label: CEO
    subtitle: 张伟
    color: blue
  - id: cto
    label: CTO
    parent: ceo
  - id: cfo
    label: CFO
    parent: ceo
  - id: fe
    label: 前端组
    subtitle: 8人
    parent: cto
  - id: be
    label: 后端组
    subtitle: 12人
    parent: cto
```

## 示例：技术分类

```yaml
type: tree
nodes:
  - id: root
    label: AI 技术
    color: blue
  - id: ml
    label: 机器学习
    parent: root
  - id: dl
    label: 深度学习
    parent: root
  - id: cv
    label: 计算机视觉
    parent: dl
  - id: nlp
    label: 自然语言处理
    parent: dl
```

## 视觉说明

- 自动计算节点位置，叶节点均匀分布，父节点居中于子节点上方
- 折线连接父子节点（elbow connector）
- 根节点默认使用 slide `color` 描边；可用 `color: blue` 等单独指定
- SVG viewBox 自适应容器宽高
