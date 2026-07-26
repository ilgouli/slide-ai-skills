# image — 图片

```yaml
type: image
src: "assets/screenshot.png"
caption: "图片说明"       # 可选
```

## 参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `src` | string | 图片路径或 URL，必填 |
| `caption` | string | 图片说明文字，可选 |

## 本地图 vs 网图

- **本地图**：图片放在 deck 目录的 `assets/` 子目录下，
  `src` 写相对路径 `assets/<文件名>`。上传时随 deck 一起入库，
  在线分享链接可直接访问。
- **网图**：`src` 写完整 URL（`http://`/`https://` 开头），
  透传不处理。

## 背景图

slide 的 `background` 字段同样支持本地图和网图：

```yaml
background: assets/cover.png       # 本地图
background: https://...            # 网图
```

## 示例

```yaml
type: image
src: assets/arch-diagram.png
caption: "图1：系统整体架构"
```

## 约束

- 支持格式：`.png` / `.jpg` / `.jpeg` / `.svg` / `.gif` / `.webp`
- 单图上限 5 MB，超过会跳过并警告
- 图片必须放在 `assets/` 子目录，`assets/` 平铺不嵌套子目录
