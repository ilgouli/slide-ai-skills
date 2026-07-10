---
name: ppt-gap-analysis
description: 分析 PPT/PDF 的页面结构，统计 slide-ai 的布局/组件覆盖缺口
---

# ppt-gap-analysis

读取一份 PPT 或 PDF，逐页分析其布局结构，判断 slide-ai 当前能否覆盖，
记录无法映射的 gap，持续积累为开发优先级依据。

## 使用方式

```
/ppt-gap-analysis <文件路径>
```

示例：
```
/ppt-gap-analysis ~/Downloads/架构分享.pptx
/ppt-gap-analysis ~/Downloads/qcon-agent-memory.pdf
```

---

## 执行步骤

### 1. 准备 PDF

如果输入是 PPTX，先转换为 PDF：

```bash
libreoffice --headless --convert-to pdf <文件路径> --outdir /tmp/
```

PDF 文件即为分析输入；直接提供 PDF 则跳过此步。

### 2. 读取布局和组件参考

分析前必须阅读 slide-ai 当前支持的 layout 和 block，作为映射标准：

**布局（layouts）**
- `skill/generate-slide/references/layouts/title.md`
- `skill/generate-slide/references/layouts/single.md`
- `skill/generate-slide/references/layouts/split.md`
- `skill/generate-slide/references/layouts/header-body.md`
- `skill/generate-slide/references/layouts/compose.md`

**内容块（blocks）**
- `skill/generate-slide/references/blocks/bullets.md`
- `skill/generate-slide/references/blocks/markdown.md`
- `skill/generate-slide/references/blocks/kpi.md`
- `skill/generate-slide/references/blocks/table.md`
- `skill/generate-slide/references/blocks/image.md`
- `skill/generate-slide/references/blocks/arch.md`
- `skill/generate-slide/references/blocks/flow.md`
- `skill/generate-slide/references/blocks/swimlane.md`
- `skill/generate-slide/references/blocks/timeline.md`
- `skill/generate-slide/references/blocks/cycle.md`
- `skill/generate-slide/references/blocks/linear.md`
- `skill/generate-slide/references/blocks/radial.md`
- `skill/generate-slide/references/blocks/pyramid.md`
- `skill/generate-slide/references/blocks/funnel.md`
- `skill/generate-slide/references/blocks/matrix.md`

### 3. 逐页分析

使用 Read 工具读取 PDF，逐页判断：

- **layout**：最接近的 slide-ai layout（title / single / split /
  header-body / compose），无匹配填 `-`
- **block**：最接近的 slide-ai block，无匹配填 `-`
- **覆盖**：
  - `✅` 可直接映射，内容和结构都能表达
  - `⚠️` 勉强覆盖，有明显视觉或结构损失
  - `❌` 无法覆盖
- **gap**：覆盖为 ⚠️ 或 ❌ 时，简洁描述缺少什么
  （如"带决策分支的流程图"、"2×2 卡片网格"）

### 4. 生成本次报告

从文件名派生 slug（英文小写+连字符），写入
`docs/gap-reports/{slug}.md`：

```markdown
# {文件名}

分析日期：{YYYY-MM-DD}
总页数：N | 覆盖：A ✅ / B ⚠️ / C ❌ | 覆盖率：X%

## 逐页分类

| 页 | 标题 | layout | block | 覆盖 | gap |
|---|---|---|---|---|---|
| 1 | 封面 | title | - | ✅ | |
| 2 | 会议规划 | - | - | ❌ | 2×2 卡片网格 |

## 本次新增 Gap

- gap 描述 1
- gap 描述 2
```

### 5. 更新汇总报告

读取 `docs/gap-reports/summary.md`（不存在则新建），
将本次新发现的 gap 合并进频率统计，更新后写回：

```markdown
# Gap Summary

最后更新：{YYYY-MM-DD}
累计分析：N 份 PPT，M 页

## Gap 频率排名

| Gap 描述 | 出现次数 | 来源 |
|---|---|---|
| 带决策分支的流程图 | 3 | qcon-agent-memory, ... |
| 代码块 | 2 | ... |

## 覆盖率记录

| 文件 | 总页 | ✅ | ⚠️ | ❌ | 覆盖率 |
|---|---|---|---|---|---|
| qcon-agent-memory | 20 | 8 | 5 | 7 | 40% |
```

### 6. 输出摘要

告知用户：
- 本次分析了几页，覆盖率多少
- 新发现了哪些 gap
- 报告路径：`docs/gap-reports/{slug}.md`
- 汇总路径：`docs/gap-reports/summary.md`

---

## 注意事项

- gap 描述要具体，写清楚缺的是什么结构，不要写"不支持"
- 同一类 gap 用统一措辞，方便 summary 去重合并
- 覆盖率仅供参考，重要的是 gap 的类型和频率
