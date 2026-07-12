# chart block

数据图表，支持 bar / bar-h / line / pie / donut / area / scatter。

## schema

```yaml
type: chart
chart_type: bar        # 见下方类型说明
title: 可选标题        # 图表上方小标题
x_key: name            # x 轴 / 分类字段名（默认 name）
y_key: y               # scatter 专用：y 轴字段名
series:                # bar/line/area/bar-h 必填
  - name: 系列名
    data_key: 数据字段  # data 中对应的 key
    color: "#7C3AED"   # 可选，覆盖调色板
data:                  # 数据数组
  - name: Q1
    value: 42
colors: []             # 可选，覆盖默认调色板
height: 280            # 图表高度（px），默认 280
legend: true           # 是否显示图例，默认 true
x_label: X轴说明       # 可选轴标签
y_label: Y轴说明
stack: false           # bar/area 是否堆叠，默认 false
```

## chart_type 说明

| 值 | 图表类型 | 必填字段 |
|---|---|---|
| `bar` | 竖向柱状图 | x_key + series + data |
| `bar-h` | 横向条形图 | x_key + series + data |
| `line` | 折线图 | x_key + series + data |
| `area` | 面积图 | x_key + series + data |
| `pie` | 饼图 | x_key (名称字段) + series[0].data_key (值字段) + data |
| `donut` | 环形图 | 同 pie |
| `scatter` | 散点图 | x_key + y_key + data |

## 示例

### bar — 多系列柱状图

```yaml
type: chart
chart_type: bar
title: 季度营收对比（百万元）
x_key: quarter
series:
  - name: "2023"
    data_key: y2023
  - name: "2024"
    data_key: y2024
data:
  - quarter: Q1
    y2023: 42
    y2024: 58
  - quarter: Q2
    y2023: 55
    y2024: 71
```

### bar-h — 横向排名

```yaml
type: chart
chart_type: bar-h
x_key: region
series:
  - name: 销售额
    data_key: sales
data:
  - region: 华东
    sales: 320
  - region: 华南
    sales: 280
  - region: 华北
    sales: 240
```

### line — 趋势折线

```yaml
type: chart
chart_type: line
x_key: month
series:
  - name: iOS
    data_key: ios
  - name: Android
    data_key: android
data:
  - month: 1月
    ios: 12
    android: 18
  - month: 2月
    ios: 14
    android: 21
```

### pie / donut — 占比

```yaml
type: chart
chart_type: donut
x_key: name
series:
  - name: 金额
    data_key: value
data:
  - name: 订阅
    value: 45
  - name: 广告
    value: 28
  - name: 其他
    value: 27
```

### area — 堆叠面积

```yaml
type: chart
chart_type: area
stack: true
x_key: week
series:
  - name: 搜索
    data_key: search
  - name: 直接
    data_key: direct
data:
  - week: W1
    search: 30
    direct: 20
  - week: W2
    search: 35
    direct: 22
```

### scatter — 相关性散点

```yaml
type: chart
chart_type: scatter
x_key: spend
y_key: cvr
x_label: 广告投入（万元）
y_label: 转化率（%）
data:
  - spend: 5
    cvr: 2.1
  - spend: 12
    cvr: 4.2
  - spend: 25
    cvr: 6.1
```

## 调色板

默认 8 色（与主题紫色系一致）：
`#7C3AED` `#3B82F6` `#10B981` `#F59E0B`
`#EF4444` `#8B5CF6` `#06B6D4` `#84CC16`

用 `colors` 字段覆盖：
```yaml
colors: ["#1e40af", "#dc2626", "#059669"]
```
