# arch — 架构层次图

用于展示系统分层架构，如前端/后端/数据库分层。

```yaml
type: arch
layers:
  - label: 层名称
    sub: 层副标注           # 可选
    items: [节点A, 节点B]   # 简单写法
    full_width: false       # 可选，该层横跨全宽
sidebar:                    # 可选，右侧跨行竖向标注
  label: 标注文字
  row_start: 1              # 对应 layers 行号（从 1 起）
  row_end: 3
```

## items 四种写法

```yaml
# 1. 字符串数组 — 单行节点
items: [React, TypeScript, Vite]

# 2. 嵌套数组 — 多行节点
items:
  - [模块A, 模块B, 模块C]
  - [模块D, 模块E]

# 3. 对象数组 — 带样式
items:
  - label: API Gateway
    shape: rounded          # rounded | rect | cylinder
    color: blue             # blue | green | yellow | gray | default

# 4. 嵌套对象数组 — 多行带样式
items:
  - - label: 主库
      color: blue
      shape: cylinder
    - label: 从库
      color: gray
      shape: cylinder
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `layers` | array | 层列表，必填，从上到下排列 |
| `layers[].label` | string | 层名称，必填 |
| `layers[].sub` | string | 层名称副标注 |
| `layers[].items` | array | 节点列表，见上方四种写法 |
| `layers[].groups` | array | 分组（带 items 和 color），可选 |
| `layers[].full_width` | bool | 横跨全宽，默认 false |
| `sidebar` | object | 右侧竖向标注，可选 |

## 完整示例

```yaml
type: arch
layers:
  - label: 接入层
    items: [Nginx, CDN]
  - label: 应用层
    items:
      - [用户服务, 订单服务, 支付服务]
      - [通知服务, 搜索服务]
  - label: 数据层
    items:
      - - label: MySQL
          shape: cylinder
          color: blue
        - label: Redis
          shape: cylinder
          color: green
        - label: Elasticsearch
          shape: cylinder
          color: yellow
  - label: 基础设施
    items: [Kubernetes, Prometheus, Grafana]
    full_width: true
sidebar:
  label: 权限控制
  row_start: 2
  row_end: 3
```
