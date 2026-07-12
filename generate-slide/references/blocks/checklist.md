# checklist block

带勾选状态的任务/行动项列表。

## schema

```yaml
type: checklist
show_progress: false   # 底部显示 "X / Y 已完成"
items:
  - text: 任务描述     # 必填
    checked: true      # 默认 false
    note: 补充说明     # 可选，小字显示在 text 下方
```

## 示例

```yaml
type: checklist
show_progress: true
items:
  - text: 需求评审
    checked: true
  - text: 技术方案
    checked: true
    note: 已通过架构委员会评审
  - text: 开发实现
    checked: false
  - text: 上线发布
    checked: false
```

## 视觉说明

- `checked: true` — 绿色勾选图标，文字带删除线
- `checked: false` — 灰色空圆图标，文字正常显示
- `note` — 浅灰小字，显示在条目文字下方
- `show_progress` — 底部显示完成进度计数
