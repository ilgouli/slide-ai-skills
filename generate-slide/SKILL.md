---
name: generate-slide
description: 根据用户描述生成 slide-ai 格式的 YAML，上传到服务并返回访问链接
---

# generate-slide

根据用户的主题描述，生成一套完整的 PPT YAML 配置，上传到 slide-ai 后端服务。

## 使用方式

```
/generate-slide <主题描述>
```

示例：
```
/generate-slide 面纱规则系统技术介绍，包含背景、架构、算法三个部分
/generate-slide 2024年Q3业务数据汇报，5页
```

---

## 执行步骤

### 1. 理解需求

从用户描述中提取：
- 主题和受众
- 大致页数（未指定默认 5-8 页）
- 内容结构（章节划分）

### 2. 阅读参考资料

在生成前必须阅读：
- `skill/generate-slide/references/config.md` — 完整 YAML 配置说明
- `skill/generate-slide/examples/` — 各类组件示例

### 3. 规划页面结构

典型结构（可根据内容调整）：
```
1. title      — 封面
2. section    — 章节过渡页（如有多章节）
3. single     — 内容页（bullets / arch / cycle / linear 等）
4. ...
5. qa         — 结尾
```

选择组件原则：
- 流程、步骤 → `linear`
- 循环、迭代 → `cycle`
- 层级架构 → `arch`
- 对比、矩阵 → `matrix`
- 漏斗、转化 → `funnel`
- 层级递进 → `pyramid`
- 关键数据 → `kpi`
- 文字说明 → `bullets` / `markdown`

### 4. 生成 YAML 文件

**deck id**：用英文小写+连字符，如 `mask-master-intro`

**`_meta.yml`**：
```yaml
title: "PPT 标题"
author: <用户名>
slides:
  - title
  - section-1
  - page-1
  - ...
  - qa
```

每页单独一个 `.yml` 文件，文件名与 slides 列表对应。

严格遵循 `references/config.md` 中的 schema，不得使用文档未定义的字段。

### 5. 保存文件

将所有 YAML 文件写入当前工作目录的 `decks/<deck-id>/` 下：

```
decks/
└── <deck-id>/
    ├── _meta.yml
    ├── title.yml
    ├── page-1.yml
    └── ...
```

如需写到其他位置，记录完整路径，在下一步上传时作为第二个参数传入即可。

### 6. 上传到服务

使用 `skill/generate-slide/client.py` 上传：

```bash
# 默认从 decks/<deck-id>/ 读取
python skill/generate-slide/client.py <deck-id>

# 指定自定义目录
python skill/generate-slide/client.py <deck-id> /path/to/deck
```

输出示例：
```
[upload] mask-master-intro (decks/mask-master-intro) ...
[ok] 面纱规则系统介绍 · 6 页
[link] http://slide.liamzheng.cn/?deck=mask-master-intro
```

环境变量：
- `SLIDE_AI_URL` — 服务地址，默认 `http://slide.liamzheng.cn`

### 7. 返回结果

告知用户：
- 生成了几页
- 访问链接：`http://slide.liamzheng.cn/?deck=<deck-id>`
- 如需调整，可直接修改 `decks/<deck-id>/` 下的 YAML 文件

---

## 注意事项

- 内容要简洁，每页不超过 5 个要点
- 标题用中文，技术术语保留英文
- 优先使用图形化组件（arch/cycle/linear），避免纯文字堆砌
- `_meta.yml` 的 `slides` 列表顺序决定页面顺序，必须与文件名对应
