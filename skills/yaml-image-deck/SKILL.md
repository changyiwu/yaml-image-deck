---
name: yaml-image-deck
description: 用一份 YAML 設計系統＋版型庫＋逐頁內容，生成風格一致的整頁圖片式簡報。當使用者要求「YAML 圖片簡報」、「NotebookLM 風格簡報」、「整頁都是圖的簡報」、「固定視覺語法的簡報」、「用黃金樣張鎖風格」、「批次生圖做投影片」時使用。支援 baked 全圖片與 plate 無字底圖＋可編輯文字兩種模式，主題不限學科。
---

# YAML Image Deck

把結構化內容變成風格一致的整頁圖片簡報。把 YAML 當成**設計合約與 prompt 編譯輸入**，不要當成像素級的排版程式碼。

## 通用性原則

本技能不綁定特定 Agent。所有需要外部能力的步驟，一律使用**當前環境已具備的工具**：

- **生圖**：使用當前 Agent 可用的內建生圖工具或生圖技能。除非使用者明確選擇 API／CLI 流程，否則不要求 API key。
- **打包**：使用當前環境可用的簡報產製方式（簡報技能、Python 套件、或請使用者手動匯入）。
- **缺能力時**：先向使用者回報缺什麼，再問要怎麼處理。不要默默改用替代方案。

## 設定軸

- `output_mode`：`baked` 或 `plate`。
- `planning_mode`：`quick` 或 `yaml_spec`。
- `generation_strategy`：`sequential` 或 `subagents`。
- `style_lock`：`none` 或 `golden_sample`。

預設用 `yaml_spec`、`sequential`、`golden_sample`。只有在使用者明確要求平行生成、且當前環境允許時，才使用 `subagents`。

## 硬性規則

- 每一頁的畫面都必須由生圖產生，才能進行打包。本地腳本可以裁切、驗證、拼接與封裝，但**不可取代 AI 生成的簡報畫面**。
- 每頁只講一個核心主張，可見中文字要短。
- 使用 16:9 目標畫布，關鍵內容留在 YAML 定義的安全區內。
- 每張最終圖片都要留在專案裡，不可只存在生圖工具的暫存輸出目錄。
- 交付前要肉眼檢查每一頁，以及整份拼接圖。

## 粗圓字體政策

預設視覺語言必須使用**粗圓的繁體中文字**：筆畫厚實、字腔飽滿、收筆圓潤、轉角低稜角，不可出現窄長的機械感字形。

`baked` 模式：每一個生圖 prompt 都要重複這段字體指示，並禁止尖角、窄體、高對比、科技模板感的中文字。

`plate` 模式：使用以下清單中**第一個實際已安裝**的字體：

1. `jf open 粉圓 2.1`
2. `GenSenRounded TW`
3. `源柔ゴシック` / `GenJyuuGothic`

三者都沒安裝時，要在最終打包前回報缺少粗圓中文字體，**不可默默改用尖角的預設字體**。確切的 prompt 用語讀 `references/prompting.md`。

## 工作流程

1. 確認溝通任務、受眾、核心結論與頁數。
2. 以 `assets/spec-template.yaml` 為底，建立或正規化 `spec.yaml`。
3. 為每頁指定語意關係與固定的 `layout.id`。讀 `references/layout-library.md`。
4. 驗證規格：

   ```powershell
   python .\scripts\validate_spec.py --spec .\spec.yaml
   ```

5. 依此順序編譯每頁 prompt：畫布與安全區 → 版型 → 頁面畫面 → 精確文字 → 全域風格 → 字體 → 參考圖 → 負面約束。
6. 先生成一頁具代表性的內容頁，當作黃金樣張檢查，通過後把路徑寫進 `design_system.style_reference`。
7. 其餘頁面一頁一次生圖呼叫。使用者明確要求平行生成時，讀 `references/subagent-batching.md`，並給每個 worker 相同的 YAML 與黃金樣張。
8. 檢查精確文字、版型、主體數量、安全區、粗圓字體與風格一致性。**只重生失敗的頁面。**
9. 若生圖能力不支援 16:9，置中裁切成 16:9（已符合比例的檔案會自動略過）：

   ```powershell
   python .\scripts\crop_to_169.py --images-dir .\slides\images
   ```

   生圖前要先在 prompt 加上「關鍵內容留在中央 16:9 範圍內」的構圖約束，否則裁切會切到標題或主體。詳見 `references/prompting.md` 的〈生圖尺寸與裁切〉。
10. 執行輸出驗證：

   ```powershell
   python .\scripts\verify_images.py --spec .\spec.yaml --images-dir .\slides\images
   ```

11. 用當前環境可用的方式打包：每頁嵌入一張滿版圖片，匯出後重新算圖、檢查拼接圖、跑溢出檢查。
12. 回報 PPTX 路徑、模式、來源圖片資料夾、規格路徑與最終 prompt 紀錄。

## 輸出模式

- `baked`：文字直接烤進圖片裡。適合快速展示、社群分享與視覺敘事。
- `plate`：生圖只產出**無文字**的設計底圖並保留文字區，之後再疊上可編輯的簡報文字。適合需要改稿、密集中文、公式、精確數據與長期維護的簡報。

只要正確性重要，公式、精確幾何、圖表與數字證據就保持原生可編輯。

## 參考文件

- 建立或修改 YAML 欄位前，讀 `references/schema.md`。
- 分配頁面版型前，讀 `references/layout-library.md`。
- 生圖前，讀 `references/prompting.md`。
- 使用者要求平行生成時，讀 `references/subagent-batching.md`。
- 打包與交付前，讀 `references/validation.md`。
