# radial — 辐射图（SmartArt）

用于展示以中心节点为核心向外辐射的关系图。

```yaml
type: radial
center: 中心节点名称
items:
  - label: 子节点名称
    detail: 说明文字     # 可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `center` | string | 中心节点文字，必填 |
| `items` | array | 外围节点列表，必填，建议 4-8 个 |
| `items[].label` | string | 节点名称，必填 |
| `items[].detail` | string | 节点说明，可选 |
| `color` | string | 主色调 |

## 示例

```yaml
type: radial
center: AI 平台
color: blue
items:
  - label: 数据管道
  - label: 模型训练
  - label: 推理服务
  - label: 监控告警
  - label: 特征工程
  - label: 实验管理
```
