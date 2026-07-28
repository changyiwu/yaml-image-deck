# YAML 結構

分成四層：

1. `deck`：受眾、目的、模式、頁數、輸出。
2. `canvas` 與 `design_system`：固定比例、安全區、配色、視覺方向、粗圓字體、負面 prompt。
3. `layout_router` 與 `layout_library`：受控的版型選擇。
4. `slides`：逐頁的教學或溝通內容。

必要的頂層欄位：

```yaml
schema_version: "yaml_image_deck_v1"
deck: {}
canvas: {}
design_system: {}
layout_router: {}
slides: []
validation: {}
```

必要的頁面欄位：

```yaml
- page: 1
  role: "cover"
  core_point: "One claim"
  semantic_structure: "focus"
  layout: {id: "cover_hero", variant: "left_title_right_visual"}
  visible_text: {title: "Short title"}
  visual: "Concrete image brief"
  output: "slides/images/page_01.png"
```

生圖 prompt 用**百分比**描述區塊位置。只有 `plate` 模式才在獨立的 `overlay_blocks` 區塊使用簡報座標。

**欄位名稱與 enum 值一律保持英文**，內容可以用受眾的語言。
