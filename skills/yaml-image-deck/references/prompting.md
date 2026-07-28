# Prompt 編譯

每一頁的 prompt 都依此順序編譯：

1. 完整 16:9 簡報圖與安全區。
2. 版型區塊與閱讀順序。
3. 視覺主體、動作與關係。
4. 精確的可見文字。
5. 共用風格 token 與黃金樣張參考圖。
6. 粗圓字體政策。
7. 負面約束。

`baked` 模式使用以下字體區塊（維持英文，避免生圖模型誤讀）：

```text
Typography: bold rounded Traditional Chinese display lettering, thick even strokes,
soft terminals, generous counters, friendly proportions, low corner sharpness.
Avoid angular geometric Chinese type, condensed type, techno stencil forms,
sharp wedges, thin strokes, or high-contrast calligraphic forms.
Render the quoted text verbatim and add no other characters.
```

`plate` 模式不生成任何文字，並保留一塊乾淨的文字區，打包時再套用已確認安裝的粗圓中文字體。

每次都要明確指出：**輸出的就是簡報畫面本身，不是螢幕、投影幕、筆電或任何 mockup。**
