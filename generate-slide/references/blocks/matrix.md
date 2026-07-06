# matrix — 四象限矩阵图（SmartArt）

用于展示二维评估矩阵，如优先级/价值矩阵等。

```yaml
type: matrix
x_label: X 轴标签       # 可选
y_label: Y 轴标签       # 可选
quadrants:
  - label: 象限名称
    items:
      - 条目1
      - 条目2
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `x_label` | string | X 轴说明（低→高方向） |
| `y_label` | string | Y 轴说明（低→高方向） |
| `quadrants` | array | 四个象限，顺序：左上、右上、左下、右下 |
| `quadrants[].label` | string | 象限名称，必填 |
| `quadrants[].items` | string[] | 该象限内的条目列表 |
| `color` | string | 主色调 |

## 示例

```yaml
type: matrix
x_label: 实施难度（低 → 高）
y_label: 业务价值（低 → 高）
quadrants:
  - label: 快速赢得（优先做）
    items:
      - 简化注册流程
      - 错误提示优化
  - label: 重大项目（规划做）
    items:
      - 推荐算法重构
      - 多语言支持
  - label: 填充项（视情况）
    items:
      - 深色模式
  - label: 低价值高成本（暂缓）
    items:
      - 桌面端 App
```
