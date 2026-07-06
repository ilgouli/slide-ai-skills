# timeline — 时间线（SmartArt）

用于展示按时间顺序排列的里程碑或阶段。支持横向（奇偶节点上下交替）和竖向（奇偶节点左右交替）两种布局。

```yaml
type: timeline
direction: horizontal   # horizontal（默认）| vertical
items:
  - date: "2024 Q1"
    label: 阶段名称
    detail: 说明文字     # 可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `direction` | string | `horizontal`（默认）\| `vertical` |
| `items` | array | 时间节点列表，必填 |
| `items[].date` | string | 时间标注，必填 |
| `items[].label` | string | 节点名称，必填 |
| `items[].detail` | string | 节点说明，可选 |
| `accent` | string | 主色调（点、线、日期），如 `#3b82f6` |

## 横向（horizontal）

节点等间距排列在水平轴上，奇偶节点的卡片上下交替，适合 3-7 个里程碑。

```yaml
type: timeline
direction: horizontal
accent: "#3b82f6"
items:
  - date: "2024 Q1"
    label: 立项
    detail: 需求评审 + 技术选型
  - date: "2024 Q2"
    label: 开发
    detail: 核心模块完成
  - date: "2024 Q3"
    label: 灰度
    detail: 覆盖 20% 用户
  - date: "2024 Q4"
    label: 全量
    detail: SLA 99.9%
```

## 竖向（vertical）

节点沿垂直轴排列，奇偶节点的日期和内容左右交替，适合 5-10 个事件、条目较多时。

```yaml
type: timeline
direction: vertical
accent: "#8b5cf6"
items:
  - date: "2020"
    label: 公司成立
    detail: 天使轮融资 500 万
  - date: "2021"
    label: 产品上线
    detail: 首批 1,000 用户
  - date: "2022"
    label: A 轮融资
    detail: 5,000 万，估值 3 亿
  - date: "2023"
    label: 出海
    detail: 进入东南亚市场
  - date: "2024"
    label: 盈利
    detail: 年营收突破 1 亿
```
