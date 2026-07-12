# grid block

均匀卡片网格，适合特性列表、指标展示、步骤说明等均匀排列的内容。

## 必填字段

| 字段 | 类型 | 说明 |
|---|---|---|
| `type` | string | 固定为 `grid` |
| `items` | array | 卡片列表，每项为一个 cell |
| `items[].title` | string | 卡片标题 |

## 可选字段（block 级）

| 字段 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `columns` | number | `3` | 列数，行数自动计算 |
| `auto_index` | boolean | `false` | 无 icon/value 时自动显示序号 |

## 可选字段（cell 级）

| 字段 | 类型 | 说明 |
|---|---|---|
| `icon` | string | 图标（见下方列表）|
| `avatar` | string | 圆形头像图片路径/URL，与 icon 二选一，用于人物卡片 |
| `value` | string | 大数字，与 icon 二选一 |
| `body` | string \| string[] | 说明文字；传数组时渲染为项目列表 |
| `subtitle` | string | title 下方的副标题（如机构名、职位）|
| `footer` | string | 卡片底部信息（如日期、状态），带上边框分隔 |
| `cta` | string | 底部行动按钮文字（填充色胶囊样式，自动加 → 箭头）|
| `tag` | string | 右上角标签 |
| `color` | string | 卡片强调色（覆盖 block 颜色）|

## 可用图标（icon 字段）

| 名称 | 用途建议 |
|---|---|
| `Zap` | 速度、性能、电力 |
| `Shield` | 安全、防护、权限 |
| `Cpu` | 计算、处理器、算力 |
| `Globe` | 全球、网络、多区域 |
| `Database` | 数据库、存储 |
| `BarChart2` | 数据、监控、指标 |
| `Lock` | 加密、访问控制 |
| `Cloud` | 云服务、部署 |
| `Code2` | 代码、开发、API |
| `Users` | 团队、用户、协作 |
| `Layers` | 分层、架构 |
| `Settings` | 配置、管理 |
| `Search` | 搜索、查询 |
| `Bell` | 通知、告警 |
| `Star` | 推荐、评分、核心 |
| `CheckCircle` | 完成、验证、合规 |
| `AlertCircle` | 警告、风险 |
| `Info` | 说明、提示 |
| `ArrowRight` | 流程、指向、下一步 |
| `Rocket` | 发布、启动、上线 |
| `Brain` | AI、智能、推理 |
| `Network` | 网络、拓扑、连接 |
| `Server` | 服务器、基础设施 |
| `Terminal` | 命令行、运维 |
| `FileText` | 文档、报告 |
| `GitBranch` | 版本控制、分支 |
| `Package` | 依赖、模块、打包 |
| `Workflow` | 流程、自动化 |
| `Monitor` | 监控、屏幕、前端 |
| `Smartphone` | 移动端、App |
| `Key` | 密钥、认证 |
| `Eye` | 可观测性、监控 |
| `Target` | 目标、精准 |

也支持直接写 emoji（`"⚡"` `"🔥"` 等）或图片 URL。

## 示例

### 特性卡片（3 列，Lucide 图标）

```yaml
layout: single
title: "核心能力"
color: "#6366f1"
block:
  type: grid
  columns: 3
  items:
    - icon: Rocket
      title: "快速部署"
      body: "一键发布，秒级生效"
      tag: "核心"
    - icon: Shield
      title: "安全隔离"
      body: "多租户隔离，数据加密"
    - icon: BarChart2
      title: "实时监控"
      body: "P99、QPS 全覆盖"
```

### 指标卡片（2 列，大数字）

```yaml
layout: single
title: "本季度成果"
color: "#10b981"
block:
  type: grid
  columns: 2
  items:
    - value: "98.5%"
      title: "完成率"
      body: "较上季度提升 3.2%"
    - value: "12ms"
      title: "P99 延迟"
      body: "缓存优化后下降 40%"
```

### 步骤卡片（自动序号）

```yaml
layout: single
title: "实施路径"
color: "#f59e0b"
block:
  type: grid
  columns: 4
  auto_index: true
  items:
    - title: "需求分析"
      body: "梳理业务场景和技术约束"
    - title: "方案设计"
      body: "确定架构和关键接口"
    - title: "开发测试"
      body: "迭代交付，持续集成"
    - title: "上线运营"
      body: "灰度发布，监控回滚"
```

## 使用建议

- `columns` 建议 2–4，超过 4 列卡片内容会过于拥挤
- icon 和 value 二选一；都不填时可开启 `auto_index: true` 显示序号
- 卡片内容保持均匀：每张卡片字数相近，视觉更整齐
