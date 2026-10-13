# Awesome openpilot [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated map of the openpilot ecosystem: forks, car ports, CAN/DBC tools, hardware, data tools, models and docs.
>
> 精選 openpilot 生態地圖：分支、車款移植、CAN／DBC 工具、硬體、資料工具、模型與文件。

**Status / 狀態:** Curated 2026-10. Contributions welcome. / 2026-10 整理，歡迎貢獻。

**Disclaimer / 免責聲明:** openpilot and its forks are **driver assistance (Level 2)**, not self-driving. You must stay attentive with hands ready at all times. Installing or modifying it is your own responsibility; follow your local laws and regulations. Forks listed here are not endorsed by comma.ai or by this list. / openpilot 及其分支是**駕駛輔助（L2）**，不是自動駕駛，必須全程專注、隨時接手。安裝或修改風險自負，請遵守當地法規。本清單不代表 comma.ai 或本清單背書。

---

## Start here / 從這裡開始

The projects people actually share. Everything below is the map around them, not a product catalog.
別人會轉發的是這幾個。下面是圍繞它們的地圖，不是產品目錄。

- **[sunnypilot](https://github.com/sunnypilot/sunnypilot)** — Open-source driver assistance fork of openpilot with extra features and car support. / openpilot 的開源分支，功能與車款支援更多。
- **[FrogPilot](https://github.com/FrogAi/FrogPilot)** — Highly customizable, community-driven openpilot fork. / 高度可自訂、社群主導的 openpilot 分支。
- **[dragonpilot](https://github.com/dragonpilot/dragonpilot)** — Long-running openpilot-based driver assistance fork. / 老牌的 openpilot 衍生駕駛輔助系統。
- **[openpilot-cabana](https://github.com/deanlee/openpilot-cabana)** — Standalone CAN / CAN FD analyzer for reverse engineering, from the Cabana lineage. / 獨立的 CAN／CAN FD 分析工具，延續 Cabana。
- **[Openpilot-Deepdive](https://github.com/OpenDriveLab/Openpilot-Deepdive)** — Research deep dive into how openpilot's driving model works. / 深入研究 openpilot 駕駛模型的專案。

---

## Contents / 目錄

- [Core (comma.ai) / 官方核心](#core-commaai--官方核心)
- [Forks & distributions / 分支與發行版](#forks--distributions--分支與發行版)
- [Hardware & ports / 硬體與移植](#hardware--ports--硬體與移植)
- [CAN, DBC & data tools / CAN、DBC 與資料工具](#can-dbc--data-tools--candbc-與資料工具)
- [Dashcam, UI & companions / 行車紀錄、UI 與周邊](#dashcam-ui--companions--行車紀錄ui-與周邊)
- [Self-hosted backends & installers / 自架後端與安裝工具](#self-hosted-backends--installers--自架後端與安裝工具)
- [Models, training & research / 模型、訓練與研究](#models-training--research--模型訓練與研究)
- [Docs & learning / 文件與學習](#docs--learning--文件與學習)
- [Closed-source / commercial (for reference) / 閉源／商業（對照用）](#closed-source--commercial-for-reference--閉源商業對照用)
- [Related lists / 相關列表](#related-lists--相關列表)
- [Contributing / 貢獻](#contributing--貢獻)
- [License / 授權](#license--授權)

---

## Core (comma.ai) / 官方核心

- **[openpilot](https://github.com/commaai/openpilot)** — The upstream project. / 上游本體。
- **[opendbc](https://github.com/commaai/opendbc)** — Python API and DBC files for car CAN buses. / 車用 CAN 的 Python API 與 DBC。
- **[panda](https://github.com/commaai/panda)** — Firmware for the panda CAN interface. / panda CAN 介面的韌體。
- **[connect](https://github.com/commaai/connect)** — Web app to manage devices and routes. / 管理裝置與行程的網頁 App。
- **[comma-steering-control](https://github.com/commaai/comma-steering-control)** — Steering measurement dataset (~12,500 h). / 約 12,500 小時的轉向資料集。

## Forks & distributions / 分支與發行版

- **[sunnypilot](https://github.com/sunnypilot/sunnypilot)** — Feature-rich fork with broad car support. / 功能豐富、車款廣的分支。
- **[FrogPilot](https://github.com/FrogAi/FrogPilot)** — Customizable community fork. / 可自訂的社群分支。
- **[FrogPilot-Resources](https://github.com/FrogAi/FrogPilot-Resources)** — Models, themes and assets FrogPilot downloads. / FrogPilot 下載的模型、主題等資源。
- **[dragonpilot](https://github.com/dragonpilot/dragonpilot)** — openpilot-based driver assistance fork. / openpilot 衍生分支。
- **[StarPilot](https://github.com/firestar5683/StarPilot)** — Monthly-updated open-source fork. / 每月更新的開源分支。
- **[openpilot](https://github.com/j-vanetten/openpilot)** — jvePilot: FCA/Stellantis hybrid openpilot + ACC. / jvePilot：FCA 車款混合 ACC。
- **[openpilot](https://github.com/BogGyver/openpilot)** — Fork for pre-AP / AP1 / AP2 Tesla cars. / 給 pre-AP／AP1／AP2 Tesla 的分支。
- **[zoompilot](https://github.com/zoompilot/zoompilot)** — Driver assistance fork focused on Mazda. / 以 Mazda 為主的分支。
- **[openpilot](https://github.com/crwusiz/openpilot)** — Community fork popular with Korean users. / 韓國社群常用分支。
- **[openpilot](https://github.com/kisapilot/openpilot)** — Community fork (Korea). / 韓國社群分支。
- **[openpilot](https://github.com/jixiexiaoge/openpilot)** — Merges features from several forks. / 整合多個分支功能。
- **[flowpilot](https://github.com/flowdriveai/flowpilot)** — openpilot-based system that runs on Android phones. / 可在 Android 手機執行的衍生系統。

## Hardware & ports / 硬體與移植

- **[RKPilot](https://github.com/MM-X/RKPilot)** — openpilot hardware/software on RK3588 / Orange Pi. / 在 RK3588／香橙派上跑 openpilot。
- **[jetlink](https://github.com/zoompilot/jetlink)** — Runs the openpilot driving model on Jetson Orin Nano, macOS, iOS. / 在 Jetson Orin Nano、macOS、iOS 跑駕駛模型。
- **[openpilot-ext-radar-addon](https://github.com/eFiniLan/openpilot-ext-radar-addon)** — External radar add-on for longitudinal control. / 外接雷達強化縱向控制。
- **[BrakeModule](https://github.com/killinen/BrakeModule)** — Brake control module for BMW E39 with Bosch DSC. / BMW E39 煞車控制模組。
- **[c3-faux-touch-keyboard](https://github.com/nelsonjchen/c3-faux-touch-keyboard)** — Cheap macro keyboard firmware to tap the comma 3 screen. / 便宜巨集鍵盤韌體，代按 comma 3 螢幕。
- **[mount-install-templates](https://github.com/ophwug/mount-install-templates)** — Mount install templates for comma three / 3X / four. / comma three／3X／four 安裝模板。

## CAN, DBC & data tools / CAN、DBC 與資料工具

- **[openpilot-cabana](https://github.com/deanlee/openpilot-cabana)** — CAN / CAN FD bus analyzer. / CAN／CAN FD 分析器。
- **[PlotJuggler](https://github.com/PlotJuggler/PlotJuggler)** — Time-series visualizer commonly used with openpilot logs. / 常用於 openpilot log 的時序視覺化工具。
- **[CanLab](https://github.com/Sherin-SEF-AI/CanLab)** — PyQt6 desktop app for reverse-engineering CAN captures. / 逆向 CAN 擷取資料的桌面 App。
- **[strym](https://github.com/jmscslgroup/strym)** — Real-time CAN logging, analysis and visualization. / 即時 CAN 記錄、分析與視覺化。
- **[make_cabana_route](https://github.com/projectgus/make_cabana_route)** — Convert local CAN logs into Cabana routes. / 把本地 CAN log 轉成 Cabana route。
- **[OpenpilotToolkit](https://github.com/spektor56/OpenpilotToolkit)** — Toolkit and library for interacting with openpilot devices. / 與 openpilot 裝置互動的工具組。

## Dashcam, UI & companions / 行車紀錄、UI 與周邊

- **[comma-sync](https://github.com/sourylime/comma-sync)** — Sync and stitch comma dashcam footage into videos. / 同步並拼接 comma 行車影像。
- **[opview](https://github.com/eFiniLan/opview)** — openpilot onroad UI over WebRTC on your phone. / 用手機透過 WebRTC 看行車 UI。
- **[Comma4-UI-Streamer](https://github.com/peterclampton/Comma4-UI-Streamer)** — MJPEG stream of the comma 4 UI for any browser. / 把 comma 4 UI 串流到瀏覽器。
- **[OpenPilotSiriShortcuts](https://github.com/twilsonco/OpenPilotSiriShortcuts)** — iOS Shortcuts to set navigation destinations. / 設定導航目的地的 iOS 捷徑。
- **[eon-custom-themes](https://github.com/Coltonton/eon-custom-themes)** — Custom boot logos and themes for EON / LEON / Two. / EON／LEON／Two 開機畫面與主題。

## Self-hosted backends & installers / 自架後端與安裝工具

- **[connect-killer](https://github.com/MoreTore/connect-killer)** — Self-hosted backend for openpilot connectivity. / openpilot 連線功能的自架後端。
- **[retropilot-server](https://github.com/florianbrede-ayet/retropilot-server)** — Replacement for the comma backend and dashboard. / 替代 comma 後端與儀表板。
- **[openpilot-installer-generator](https://github.com/sshane/openpilot-installer-generator)** — Generates custom fork installer binaries. / 產生自訂分支安裝程式。

## Models, training & research / 模型、訓練與研究

- **[Openpilot-Deepdive](https://github.com/OpenDriveLab/Openpilot-Deepdive)** — Deep dive into the driving model. / 駕駛模型深入研究。
- **[openpilot.distill](https://github.com/YassineYousfi/openpilot.distill)** — Distill openpilot using your own drives. / 用自己的行程蒸餾模型。
- **[comma10k-baseline](https://github.com/YassineYousfi/comma10k-baseline)** — Segmentation baseline on comma10k. / comma10k 分割基準。
- **[openpilot-pipeline](https://github.com/mbalesni/openpilot-pipeline)** — End-to-end training pipeline for openpilot-style models. / 端到端訓練流程。
- **[openpilot-supercombo-model](https://github.com/MTammvee/openpilot-supercombo-model)** — Using the supercombo ONNX model. / 使用 supercombo ONNX 模型。
- **[traffic-lights](https://github.com/sshane/traffic-lights)** — Traffic-light recognition model and data. / 紅綠燈辨識模型與資料。
- **[Comma.ai-Simulation-instruction](https://github.com/Aravindseenu/Comma.ai-Simulation-instruction)** — Running openpilot with CARLA, with troubleshooting. / openpilot 搭配 CARLA 模擬說明。

## Docs & learning / 文件與學習

- **[docs](https://github.com/optskug/docs)** — Guides and history for openpilot on Toyota/Lexus/Subaru and more. / Toyota／Lexus／Subaru 等車款指南與歷史。
- **[docs](https://github.com/ophwug/docs)** — Unofficial docs of fixes and tweaks for comma devices. / comma 裝置非官方修正與調整文件。
- **[comma-wiki-cn](https://github.com/12kv/comma-wiki-cn)** — Chinese-language comma / openpilot wiki. / 中文 comma／openpilot wiki。
- **[dragonpilot_wiki](https://github.com/dragonpilot/dragonpilot_wiki)** — dragonpilot wiki. / dragonpilot wiki。

## Closed-source / commercial (for reference) / 閉源／商業（對照用）

- **[comma.ai shop](https://comma.ai/shop)** — Official comma devices and harnesses. / 官方裝置與線組。
- **[comma Discord](https://discord.comma.ai)** — Main community chat. / 主要社群。

## Related lists / 相關列表

- [alteredorange/awesome-openpilot](https://github.com/alteredorange/awesome-openpilot) — Earlier list, inactive since 2023. / 較早的清單，2023 後未更新。
- [Awesome](https://github.com/sindresorhus/awesome)

## Contributing / 貢獻

Open a PR or issue. One line per entry, open-source and on-topic, link to the repo, no star counts. Closed-source/commercial only in the reference section.
歡迎開 PR 或 issue。每條一行、需開源且切題、直接連到倉庫、不放星數。閉源／商業只放對照區。

## License / 授權

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright to this work. / 在法律允許範圍內，貢獻者放棄本作品的所有著作權。
