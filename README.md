# YAML Image Deck

用一份 YAML 同時固定視覺語法、版型庫與逐頁內容，再由 AI 逐頁生成 NotebookLM 風格的圖片式簡報。

## 核心能力

- 通用主題，不限定學科。
- `baked` 全圖片與 `plate` 無字底圖兩種模式。
- 黃金樣張鎖定風格。
- 可選 Subagent 分批生圖。
- 固定骨架＋受控版型，不讓每頁隨機排版。
- 預設使用粗圓、飽滿、低稜角的繁體中文字體語言。

## 通用性

本技能不綁定任何特定 Agent。生圖、生檔與打包一律交給**當前環境已具備的能力**：

- 生圖：使用當前 Agent 可用的內建生圖工具或生圖技能。
- 打包：使用當前環境可用的簡報產製方式（簡報技能、Python 套件、或手動匯入）。
- 若當前環境缺少生圖能力，先向使用者回報，不要用本地繪圖腳本假裝成 AI 生成的簡報畫面。

## 安裝

把 `skills/yaml-image-deck/` 整個資料夾複製到你的 Agent 讀取技能的目錄下即可，例如：

| Agent | 技能目錄 |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` |
| Antigravity | `~/.gemini/config/skills/` |

只想用在單一專案時，也可以放進該專案的技能目錄，不必安裝到全域。

安裝後可說：

> 用 yaml-image-deck，把這份內容做成固定視覺語法、版型會依內容變化的圖片簡報。

## 驗證

```powershell
python .\skills\yaml-image-deck\scripts\validate_spec.py --spec .\skills\yaml-image-deck\assets\spec-template.yaml
```

## 出處與授權

本專案是**改作版本**，原始著作為三師爸 Sense Bar 的 [mathruffian-dot/yaml-image-deck](https://github.com/mathruffian-dot/yaml-image-deck)（2026-07-10 發布，MIT License）。

原始設計——YAML 設計合約、受控版型庫、黃金樣張鎖風格、粗圓中文字體政策——皆由原作者提出。

本版本由 changyiwu 修改，變更如下：

- 移除 Codex 綁定，改為不限特定 Agent 的通用技能；生圖與打包一律使用當前環境已具備的能力。
- 移除寫死的全域安裝器指令，改為四家 Agent 的技能目錄對照表。
- `agents/openai.yaml` 更名為中性的 `agents/interface.yaml`。
- 所有文件改寫為繁體中文（YAML 欄位名、版型 ID 與生圖 prompt 保持英文）。

依 MIT License 規定，原始著作權聲明與授權條款完整保留於 [LICENSE](LICENSE)：Copyright (c) 2026 三師爸 Sense Bar。本改作版本同樣以 MIT License 釋出。
