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

MIT License。
