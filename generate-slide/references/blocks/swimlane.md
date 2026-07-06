# swimlane — 泳道图

用于展示跨角色/跨系统的流程，节点按泳道分行排列，支持箭头连接。

```yaml
type: swimlane
lanes:
  - label: 泳道名称
    nodes:
      - id: "n1"
        label: 节点名称
        shape: rounded    # rounded | diamond | pill
        color: blue       # blue | green | yellow | gray
edges:
  - from: "n1"
    to: "n2"
    label: 边标签         # 可选
```

## 参数说明

### lanes

| 字段 | 类型 | 说明 |
|------|------|------|
| `label` | string | 泳道名称，显示在左侧，必填 |
| `nodes` | array | 该泳道内的节点列表 |

### nodes

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 节点唯一 ID，用于 edges 引用，必填 |
| `label` | string | 节点文字，必填 |
| `col` | number | 节点所在列（从 1 起），必填 |
| `shape` | string | 节点形状：`rounded`（默认）\| `diamond`（判断）\| `pill` |
| `color` | string | 节点颜色：`blue` \| `green` \| `yellow` \| `gray` |

### edges

| 字段 | 类型 | 说明 |
|------|------|------|
| `from` / `to` | string | 节点 ID，必填 |
| `label` | string | 边标签，可选 |

## 示例

```yaml
type: swimlane
lanes:
  - label: 用户
    nodes:
      - id: start
        label: 提交申请
        col: 1
        color: blue
      - id: confirm
        label: 确认结果
        col: 4
        color: green
  - label: 系统
    nodes:
      - id: validate
        label: 格式校验
        col: 2
      - id: check
        label: 规则匹配？
        col: 3
        shape: diamond
  - label: 人工审核
    nodes:
      - id: review
        label: 人工复审
        col: 3
        color: yellow
edges:
  - from: start
    to: validate
  - from: validate
    to: check
  - from: check
    to: confirm
    label: 通过
  - from: check
    to: review
    label: 存疑
  - from: review
    to: confirm
```
