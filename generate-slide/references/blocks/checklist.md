# checklist block

带勾选状态的任务/行动项列表，支持三态标注。

## schema

```yaml
type: checklist
show_progress: false   # 底部显示 "X / Y 已完成"
items:
  - text: 任务描述         # 必填
    status: done          # done | partial | blocked（优先于 checked）
    checked: true         # 兼容旧格式，status 未设时生效
    note: 补充说明         # 可选，小字显示在 text 下方
```

## 示例

```yaml
type: checklist
show_progress: true
items:
  - text: 需求评审
    status: done
  - text: 技术方案
    status: done
    note: 已通过架构委员会评审
  - text: 开发实现
    status: partial
    note: 核心模块完成，边缘场景待补
  - text: 安全审计
    status: blocked
    note: 等待安全团队排期
  - text: 上线发布
    note: 计划 Q3 末
```

## 视觉说明

| status | 图标 | 颜色 |
|---|---|---|
| `done` | ✓ CheckCircle | 绿色，文字删除线 |
| `partial` | − MinusCircle | 琥珀色 |
| `blocked` | ✗ XCircle | 红色，文字红色 |
| 未设（pending）| ○ Circle | 灰色 |

- `checked: true` 等价于 `status: done`（向后兼容）
- `note` — 浅灰小字，显示在条目文字下方
- `show_progress` — 底部显示完成进度（仅统计 done 状态）
