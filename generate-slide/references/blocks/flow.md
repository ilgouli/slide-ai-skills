# flow — ReactFlow 流程图

用于展示有分支的流程，支持菱形判断节点。

```yaml
type: flow
viewport:
  x: 0
  y: 0
  zoom: 0.8
nodes:
  - id: "1"
    label: 节点名称
    x: 100
    y: 0
    style: blue             # blue | green | yellow | gray
    type: diamond           # 可选，菱形判断节点
    detail: |               # 可选，悬浮说明
      多行文字
edges:
  - from: "1"
    to: "2"
    label: 条件             # 可选
    animated: true          # 可选，流动动画
    handle: yes             # yes | no，菱形节点出口方向
    type: step              # step | straight，默认平滑曲线
    style: green            # 可选
```

## 参数说明

### nodes

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 节点 ID，必填 |
| `label` | string | 节点文字，必填 |
| `x` / `y` | number | 节点位置，必填 |
| `style` | string | 颜色：`blue` \| `green` \| `yellow` \| `gray` |
| `type` | string | `diamond` = 菱形判断节点 |
| `detail` | string | 悬浮提示文字 |

### edges

| 字段 | 类型 | 说明 |
|------|------|------|
| `from` / `to` | string | 节点 ID，必填 |
| `label` | string | 边标签 |
| `animated` | bool | 流动动画，默认 false |
| `handle` | string | 菱形出口：`yes` \| `no` |
| `type` | string | `step`（折线） \| `straight`（直线） |

## 示例

```yaml
type: flow
viewport:
  x: 50
  y: 30
  zoom: 0.9
nodes:
  - id: start
    label: 收到请求
    x: 200
    y: 0
    style: blue
  - id: auth
    label: 鉴权通过？
    x: 200
    y: 100
    type: diamond
  - id: process
    label: 处理业务
    x: 200
    y: 220
    style: green
  - id: reject
    label: 返回 401
    x: 400
    y: 100
    style: gray
edges:
  - from: start
    to: auth
  - from: auth
    to: process
    handle: yes
    label: 是
  - from: auth
    to: reject
    handle: no
    label: 否
```
