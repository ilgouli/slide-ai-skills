# linear — 线性流程图（SmartArt）

用于展示从左到右的线性步骤流程。

```yaml
type: linear
items:
  - label: 步骤名称
    detail: 说明文字     # 可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `items` | array | 步骤列表，必填，建议 3-7 个 |
| `items[].label` | string | 步骤名称，必填 |
| `items[].detail` | string | 步骤说明，可选 |
| `color` | string | 主色调 |

## 示例

```yaml
type: linear
color: blue
items:
  - label: 接入申请
    detail: 提交业务信息
  - label: 审核
    detail: 1-2个工作日
  - label: 集成开发
    detail: SDK 接入
  - label: 联调测试
    detail: 沙盒环境验证
  - label: 上线
    detail: 正式环境切换
```
