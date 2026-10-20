# Awesome openpilot [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | 繁體中文

> 精選 openpilot 生態地圖：分支、車款移植、CAN／DBC 工具、硬體、資料工具、模型與文件。

**狀態：** 2026-10 整理，歡迎貢獻。

**免責聲明：** openpilot 及其分支是**駕駛輔助（L2）**，不是自動駕駛，必須全程專注、隨時接手。安裝或修改風險自負，請遵守當地法規。本清單不代表 comma.ai 或本清單背書。

---

## 從這裡開始

別人會轉發的是這幾個。下面是圍繞它們的地圖，不是產品目錄。

- **[sunnypilot](https://github.com/sunnypilot/sunnypilot)** — openpilot 的開源分支，功能與車款支援更多。
- **[FrogPilot](https://github.com/FrogAi/FrogPilot)** — 高度可自訂、社群主導的 openpilot 分支。
- **[dragonpilot](https://github.com/dragonpilot/dragonpilot)** — 老牌的 openpilot 衍生駕駛輔助系統。
- **[openpilot-cabana](https://github.com/deanlee/openpilot-cabana)** — 獨立的 CAN／CAN FD 分析工具，延續 Cabana。
- **[Openpilot-Deepdive](https://github.com/OpenDriveLab/Openpilot-Deepdive)** — 深入研究 openpilot 駕駛模型的專案。

---

## 目錄

- [官方核心（comma.ai）](#官方核心commaai)
- [分支與發行版](#分支與發行版)
- [硬體與移植](#硬體與移植)
- [CAN、DBC 與資料工具](#candbc-與資料工具)
- [行車紀錄、UI 與周邊](#行車紀錄ui-與周邊)
- [自架後端與安裝工具](#自架後端與安裝工具)
- [模型、訓練與研究](#模型訓練與研究)
- [文件與學習](#文件與學習)
- [閉源／商業（對照用）](#閉源商業對照用)
- [相關列表](#相關列表)
- [貢獻](#貢獻)
- [授權](#授權)

---

## 官方核心（comma.ai）

- **[openpilot](https://github.com/commaai/openpilot)** — 上游本體。
- **[opendbc](https://github.com/commaai/opendbc)** — 車用 CAN 的 Python API 與 DBC。
- **[panda](https://github.com/commaai/panda)** — panda CAN 介面的韌體。
- **[connect](https://github.com/commaai/connect)** — 管理裝置與行程的網頁 App。
- **[comma-steering-control](https://github.com/commaai/comma-steering-control)** — 約 12,500 小時的轉向資料集。

## 分支與發行版

- **[sunnypilot](https://github.com/sunnypilot/sunnypilot)** — 功能豐富、車款廣的分支。
- **[FrogPilot](https://github.com/FrogAi/FrogPilot)** — 可自訂的社群分支。
- **[FrogPilot-Resources](https://github.com/FrogAi/FrogPilot-Resources)** — FrogPilot 下載的模型、主題等資源。
- **[dragonpilot](https://github.com/dragonpilot/dragonpilot)** — openpilot 衍生分支。
- **[StarPilot](https://github.com/firestar5683/StarPilot)** — 每月更新的開源分支。
- **[openpilot](https://github.com/j-vanetten/openpilot)** — jvePilot：FCA 車款混合 ACC。
- **[openpilot](https://github.com/BogGyver/openpilot)** — 給 pre-AP／AP1／AP2 Tesla 的分支。
- **[zoompilot](https://github.com/zoompilot/zoompilot)** — 以 Mazda 為主的分支。
- **[openpilot](https://github.com/crwusiz/openpilot)** — 韓國社群常用分支。
- **[openpilot](https://github.com/kisapilot/openpilot)** — 韓國社群分支。
- **[openpilot](https://github.com/jixiexiaoge/openpilot)** — 整合多個分支功能。
- **[flowpilot](https://github.com/flowdriveai/flowpilot)** — 可在 Android 手機執行的衍生系統。

## 硬體與移植

- **[RKPilot](https://github.com/MM-X/RKPilot)** — 在 RK3588／香橙派上跑 openpilot。
- **[jetlink](https://github.com/zoompilot/jetlink)** — 在 Jetson Orin Nano、macOS、iOS 跑駕駛模型。
- **[openpilot-ext-radar-addon](https://github.com/eFiniLan/openpilot-ext-radar-addon)** — 外接雷達強化縱向控制。
- **[BrakeModule](https://github.com/killinen/BrakeModule)** — BMW E39 煞車控制模組。
- **[c3-faux-touch-keyboard](https://github.com/nelsonjchen/c3-faux-touch-keyboard)** — 便宜巨集鍵盤韌體，代按 comma 3 螢幕。
- **[mount-install-templates](https://github.com/ophwug/mount-install-templates)** — comma three／3X／four 安裝模板。
- **[ars510-radar](https://github.com/ds-sebastian/ars510-radar)** — 解碼 RAV4 2022+ 等 Toyota 的 ARS510 前雷達並接入 openpilot。
- **[edgepilot](https://github.com/cwal1220/edgepilot)** — 在 Sipeed MaixCAM2（AX630C NPU）上跑 openpilot 駕駛模型與橫向控制，搭配 Panda CAN。
- **[End-To-End-Self-Driving](https://github.com/Sontran0118/End-To-End-Self-Driving)** — 在 Jetson Orin Nano 上跑 openpilot，透過自製 STM32F407 panda 控制 2023 Mazda CX-5。

## CAN、DBC 與資料工具

- **[openpilot-cabana](https://github.com/deanlee/openpilot-cabana)** — CAN／CAN FD 分析器。
- **[PlotJuggler](https://github.com/PlotJuggler/PlotJuggler)** — 常用於 openpilot log 的時序視覺化工具。
- **[CanLab](https://github.com/Sherin-SEF-AI/CanLab)** — 逆向 CAN 擷取資料的桌面 App。
- **[strym](https://github.com/jmscslgroup/strym)** — 即時 CAN 記錄、分析與視覺化。
- **[make_cabana_route](https://github.com/projectgus/make_cabana_route)** — 把本地 CAN log 轉成 Cabana route。
- **[OpenpilotToolkit](https://github.com/spektor56/OpenpilotToolkit)** — 與 openpilot 裝置互動的工具組。
- **[pandacapture](https://github.com/suburbazine/pandacapture)** — 用 comma Red／Black Panda 擷取 CAN、即時儀表與刷韌體。
- **[AutoDistill](https://github.com/bbbenji/AutoDistill)** — 從 CAN 擷取自動逆向、產生 openpilot 車款移植。
- **[panda-socketcan](https://github.com/I-CAN-hack/panda-socketcan)** — 給 comma.ai White／Black／Red panda 的 CANnectivity 韌體，透過 Linux 內建 gs_usb 驅動以 SocketCAN 使用其 CAN 通道。

## 行車紀錄、UI 與周邊

- **[comma-sync](https://github.com/sourylime/comma-sync)** — 同步並拼接 comma 行車影像。
- **[opview](https://github.com/eFiniLan/opview)** — 用手機透過 WebRTC 看行車 UI。
- **[Comma4-UI-Streamer](https://github.com/peterclampton/Comma4-UI-Streamer)** — 把 comma 4 UI 串流到瀏覽器。
- **[OpenPilotSiriShortcuts](https://github.com/twilsonco/OpenPilotSiriShortcuts)** — 設定導航目的地的 iOS 捷徑。
- **[eon-custom-themes](https://github.com/Coltonton/eon-custom-themes)** — EON／LEON／Two 開機畫面與主題。
- **[sunnyconf](https://github.com/Falseclock/sunnyconf)** — 透過區網用 Android App 調整 sunnypilot 參數的裝置端服務。
- **[sunnyconf-app](https://github.com/Falseclock/sunnyconf-app)** — sunnyconf 的原生 Android 客戶端：區網設定 sunnypilot 並瀏覽行程。
- **[roadviewer-ha](https://github.com/Qualified4/roadviewer-ha)** — 上傳並重播 openpilot 日誌的 Home Assistant App，同步顯示影像、車道與雷達。
- **[delamain](https://github.com/vonhex/delamain)** — 給 comma 上 sunnypilot 的自架 AI 行車助手（語音與遙測）。
- **[oceanfront-view](https://github.com/moistpope/oceanfront-view)** — 給 Fisker Ocean 中控螢幕的 Tesla 風格 HUD，由跑 sunnypilot 的 comma 裝置即時供資料。

## 自架後端與安裝工具

- **[connect-killer](https://github.com/MoreTore/connect-killer)** — openpilot 連線功能的自架後端。
- **[retropilot-server](https://github.com/florianbrede-ayet/retropilot-server)** — 替代 comma 後端與儀表板。
- **[openpilot-installer-generator](https://github.com/sshane/openpilot-installer-generator)** — 產生自訂分支安裝程式。
- **[comma-analytics](https://github.com/clickityclickclickclick/comma-analytics)** — 自架 Grafana 儀表板，分析 comma／openpilot 行程。

## 模型、訓練與研究

- **[Openpilot-Deepdive](https://github.com/OpenDriveLab/Openpilot-Deepdive)** — 駕駛模型深入研究。
- **[openpilot.distill](https://github.com/YassineYousfi/openpilot.distill)** — 用自己的行程蒸餾模型。
- **[openpilot-local-finetune](https://github.com/klebeer/openpilot-local-finetune)** — 在筆電上用自己的行程微調 openpilot 駕駛模型。
- **[openpilot_carla_model_finetuner](https://github.com/jagoff2/openpilot_carla_model_finetuner)** — 在 CARLA 收集置中行駛樣本、微調 openpilot 駕駛模型並匯出到 comma 3X。
- **[openpilot-desktop](https://github.com/luzijun360/openpilot-desktop)** — 在 Mac 或 Windows 上對行車影片跑 openpilot 駕駛模型，疊出 comma 同款車道線與路徑。
- **[comma10k-baseline](https://github.com/YassineYousfi/comma10k-baseline)** — comma10k 分割基準。
- **[openpilot-pipeline](https://github.com/mbalesni/openpilot-pipeline)** — 端到端訓練流程。
- **[openpilot-supercombo-model](https://github.com/MTammvee/openpilot-supercombo-model)** — 使用 supercombo ONNX 模型。
- **[traffic-lights](https://github.com/sshane/traffic-lights)** — 紅綠燈辨識模型與資料。
- **[Comma.ai-Simulation-instruction](https://github.com/Aravindseenu/Comma.ai-Simulation-instruction)** — openpilot 搭配 CARLA 模擬說明。

## 文件與學習

- **[docs](https://github.com/optskug/docs)** — Toyota／Lexus／Subaru 等車款指南與歷史。
- **[docs](https://github.com/ophwug/docs)** — comma 裝置非官方修正與調整文件。
- **[comma-wiki-cn](https://github.com/12kv/comma-wiki-cn)** — 中文 comma／openpilot wiki。
- **[dragonpilot_wiki](https://github.com/dragonpilot/dragonpilot_wiki)** — dragonpilot wiki。

## 閉源／商業（對照用）

- **[comma.ai shop](https://comma.ai/shop)** — 官方裝置與線組。
- **[comma Discord](https://discord.comma.ai)** — 主要社群。

## 相關列表

- [alteredorange/awesome-openpilot](https://github.com/alteredorange/awesome-openpilot) — 較早的清單，2023 後未更新。
- [Awesome](https://github.com/sindresorhus/awesome)

## 貢獻

歡迎開 PR 或 issue。每條一行、需開源且切題、直接連到倉庫、不放星數。閉源／商業只放對照區。

## 授權

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允許範圍內，貢獻者放棄本作品的所有著作權。
