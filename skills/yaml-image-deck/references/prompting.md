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

## 生圖尺寸與裁切

多數生圖模型**沒有 16:9 尺寸**。例如 gpt-image-2 只有三種：

| 尺寸 | 比例 | 對 16:9（1.778） |
|---|---|---|
| 1024x1024 | 1.000 | 差太多，不要用 |
| 1536x1024 | 1.500 | 最接近，**用這個** |
| 1024x1536 | 0.667 | 直式，不要用 |

`verify_images.py` 的比例容差只有 0.01，直接拿 1536x1024 去驗會**每一張都判 INVALID**。

處理方式：**選最接近的橫式尺寸生圖，再置中裁切成 16:9**。

```powershell
python .\scripts\crop_to_169.py --images-dir .\slides\images
```

1536x1024 會裁成 1536x864，**上下各切掉 80 px**。所以生圖 prompt 必須額外加上這段約束：

```text
Composition: reserve generous empty margins at the top and bottom edges.
Keep all text, faces, key subjects, and critical detail within the central
16:9 band of the frame. Nothing important may touch the top or bottom edge.
```

沒加這段就會裁掉標題或切到主體。**寧可構圖鬆一點，也不要貼邊。**

裁切只做置中裁切，不縮放、不重繪，所以不違反「本地工具不可取代 AI 生成畫面」的硬性規則。若之後改用原生支援 16:9 的生圖能力，這一步會自動略過（腳本偵測到已符合比例就跳過）。
