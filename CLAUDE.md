@agents.md

<!--
  本檔是「橋接檔」：Claude Code 只讀 CLAUDE.md，不讀 agents.md，
  所以用第一行的 @agents.md 把跨 Agent 專案藍圖 import 進來。
  專案內容一律寫進 agents.md，這裡只放 Claude Code 專屬規範，避免兩份分叉。
-->

## Claude Code 專屬

- 本專案要生圖時，使用 `claude-draw` 技能（gpt-image-2）。但**不可把這個綁定寫進 `skills/yaml-image-deck/` 裡的任何檔案**——技能本體必須保持不綁定 Agent。
