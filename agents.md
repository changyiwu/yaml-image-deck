# YAML Image Deck（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。
> Claude Code 不讀 `agents.md`，改由 `CLAUDE.md` 的 `@agents.md` import 本檔；Claude 專屬規範寫在 `CLAUDE.md`。

## 專案簡介

本專案是一個**可安裝的 Agent 技能包**，不是簡報成品。核心是用一份 YAML 當「設計合約」，同時鎖住畫布骨架、視覺語法、受控版型與逐頁內容，讓 AI 逐頁生成風格一致的整頁圖片式簡報（NotebookLM 風格），避免每頁排版隨機漂移。

技能本身**不綁定任何特定 Agent**：生圖與打包一律使用當前環境已具備的能力，可安裝到 Claude Code、Codex、OpenCode、Antigravity 等任一技能目錄。

**出處**：改寫自同作者的原始版本 [mathruffian-dot/yaml-image-deck](https://github.com/mathruffian-dot/yaml-image-deck)（2026-07-10，MIT，著作權人同為「三師爸 Sense Bar」）。差異說明寫在 `README.md` 的〈出處與授權〉。

## 關鍵時程

<!-- 目前無外部時程 -->

## 目標與路線圖

- [x] 階段一：技能骨架完成（SKILL.md、參考文件、範本規格、驗證腳本、CI）
- [x] 階段二：去除 Codex 綁定，改為全 Agent 通用；文件全面繁體中文化
- [ ] 階段三：實際跑一份完整簡報驗收流程（golden sample → 全頁生圖 → 打包 → 拼接圖檢查）
- [ ] 階段四：依實跑結果回頭修正 prompt 與版型庫

## 資料夾結構

```
yaml-image-deck/
├── agents.md                          專案藍圖（本檔，跨 Agent）
├── handoff.md                         交接檔（開工必讀、收工必更新）
├── CLAUDE.md                          橋接檔（@agents.md，供 Claude Code 讀取）
├── README.md                          專案說明與安裝方式
├── LICENSE                            MIT（Copyright 三師爸 Sense Bar）
├── .gitignore
├── .github/workflows/validate.yml     CI：安裝 PyYAML+Pillow → 跑 tools/validate_repo.py
├── tools/validate_repo.py             檢查 SKILL.md frontmatter、interface.yaml、範本規格
└── skills/yaml-image-deck/            ← 技能本體（要安裝的就是這層）
    ├── SKILL.md                       主指令：設定軸、硬性規則、字體政策、11 步流程
    ├── agents/interface.yaml          通用介面設定（顯示名稱、預設 prompt）
    ├── assets/spec-template.yaml      3 頁範例規格，複製後改
    ├── references/
    │   ├── schema.md                  YAML 四層結構與必要欄位
    │   ├── layout-library.md          12 個受控版型，依資訊關係路由
    │   ├── prompting.md               prompt 編譯順序與粗圓字體 prompt 區塊
    │   ├── subagent-batching.md       平行生圖的分工規則
    │   └── validation.md              退回重生條件與交付前檢查
    └── scripts/
        ├── validate_spec.py           驗 YAML 結構、頁碼連號、版型 ID 合法
        └── verify_images.py           驗圖片存在與 16:9 比例
```

## 同步層級（本專案初始化至第 3 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（GDrive） | `agents.md`＋`handoff.md`＋`CLAUDE.md`（橋接） | 每個 session |
| L2 | GitHub | https://github.com/changyiwu/yaml-image-deck （公開） | 指定時 |
| L3 | Obsidian | `yaml-image-deck/專案工作流程.md` | 有需要時 |

## 工作約定

- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構

## 本專案專屬約定

- **不綁定 Agent**：新增內容時不可寫死特定 Agent 的工具名、指令語法或安裝路徑。需要外部能力時，一律描述成「使用當前環境可用的 X」。
- **文件語言**：所有 `.md` 用繁體中文；YAML 的**欄位名與 enum 值保持英文**（`schema.md` 有明訂），只有內容值用中文。
- **生圖 prompt 保持英文**：`prompting.md` 裡給生圖模型的 typography 區塊維持英文原文，避免模型誤讀。
- **改動技能後要跑驗證**：`python tools/validate_repo.py`（CI 也會跑同一支）。
- 修改 `agents/interface.yaml` 檔名或 `SKILL.md` frontmatter 時，記得同步改 `tools/validate_repo.py` 的檢查。
