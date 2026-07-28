# table — 表格

```yaml
type: table
heads: [列1, 列2, 列3]
widths: ["40%", "30%", "30%"]   # 可选，列宽
rows:
  - [单元格, 单元格, 单元格]
footer: "备注文字"               # 可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `heads` | string[] | 表头，必填 |
| `widths` | string[] | 列宽百分比，可选 |
| `col_groups` | ColGroup[] | 分组列头，可选（见下） |
| `rows` | (string[] \| GroupRow)[] | 数据行，必填 |
| `footer` | string | 底部备注，可选 |
| `left_border` | string | 左侧竖线颜色 |

### ColGroup

```yaml
col_groups:
  - label: 基本信息
    span: 2        # 跨几列
  - label: Q1 考核
    span: 3
```

渲染为 `<thead>` 中的第一行，每组跨对应列数，颜色与页面 `color` 一致。

### 分组行（GroupRow）

```yaml
rows:
  - group: 技术团队       # 全行标题，accent 背景 + 白字
  - [张伟, P7, 98%]
  - group: 产品团队
  - [赵磊, P6, 90%]
```

`group` 键出现时，该行渲染为全列合并的分组标题行。

## 基础示例

```yaml
type: table
heads: [模块, 负责人, 状态, 上线日期]
widths: ["30%", "20%", "20%", "30%"]
rows:
  - [规则引擎, 张三, ✅ 已上线, 2026-05-01]
  - [执行引擎, 李四, 🚧 开发中, 2026-07-15]
  - [监控面板, 王五, 📋 规划中, TBD]
footer: "数据截至 2026-07-01"
```

## 分组行 + 分组列示例

```yaml
type: table
col_groups:
  - label: 基本信息
    span: 3
  - label: Q1 考核
    span: 2
  - label: Q2 考核
    span: 2
heads: [姓名, 部门, 职级, 完成率, 评分, 完成率, 评分]
rows:
  - group: 技术团队
  - [张伟, 前端, P7, 98%, A, 95%, A]
  - [李明, 后端, P6, 88%, B+, 91%, A-]
  - group: 产品团队
  - [赵磊, 产品, P7, 90%, A-, 88%, B+]
footer: "评分标准：A≥90% / B+≥85% / B≥80%"
```

## 文件链接

单元格内容支持 markdown 链接，`[显示文字](file:assets/<name>)`
点击弹框显示文件内容（`.md`/`.json`/`.yaml`/`.yml`）。`[]` 里可用别名，
不限于文件名：

```yaml
type: table
heads: ["文件", "说明"]
rows:
  - ["[SKILL.md](file:assets/SKILL.md)", "入口文档"]
  - ["[配置详情](file:assets/config.json)", "配置"]   # 别名示例
```

文件需放 `assets/` 子目录随 deck 上传，详见
[`blocks/image.md`](image.md) 的资源约定。

## 单元格换行

单元格内支持换行，用 `\n`（YAML 字符串里的换行）即可：

```yaml
rows:
  - ["第一行\n第二行", "说明"]
```

也支持 markdown 行内语法（加粗、链接等）。
