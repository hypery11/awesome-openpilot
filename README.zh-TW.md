# Awesome openpilot [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Awesome openpilot](assets/banner.png)

[![Entries](https://img.shields.io/badge/entries-88-blue)](#目錄) [![Last updated](https://img.shields.io/badge/last_updated-2026--11--09-brightgreen)](https://github.com/hypery11/awesome-openpilot/commits/main/) [![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey)](LICENSE) [![Link check](https://github.com/hypery11/awesome-openpilot/actions/workflows/links.yml/badge.svg)](https://github.com/hypery11/awesome-openpilot/actions/workflows/links.yml)

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

## 本週新增

2026-11-03 至 2026-11-09 新增的條目（依 git 紀錄整理）。

- **[carrotpilot](https://github.com/ajouatom/openpilot)** — 以 openpilot 為基礎、聚焦 Hyundai／Kia／Genesis 相容性與縱向操控體感的獨立駕駛輔助分支，從 i.carrotpilot.app/carrot-wip 安裝；支援 comma three、3X 與 four，README 為韓文、英文與簡體中文。 _(分支與發行版)_
- **[BluePilot](https://github.com/BluePilotDev/bluepilot)** — 以 sunnypilot 為基礎、先在本地驗證再上游回報的 Ford 專用橫向與縱向強化分支，支援 comma 3X 與 comma 4，從 installer.comma.ai/BluePilotDev/bp-7.0 安裝。 _(分支與發行版)_
- **[SunnyPilot-TeslaHW1](https://github.com/P6g9YHK6/SunnyPilot-TeslaHW1)** — 以 sunnypilot 為基礎、移植 Tesla Hardware 1／AP1 支援的分支（已在 2015 Model S 與 2016 Model X 測試），搭配 xnor 線束，支援 comma 3X 與 comma 4。 _(分支與發行版)_
- **[sealion7ka2](https://github.com/diamondlim/sealion7ka2)** — KA2（openpilot 系 ADAS 盒，用於 BYD Sealion 7）分支的獨立備份：裝置追蹤的 longitudinal_off 分支，含 rate／alive gating 修正、無雷達規劃器與 ka2_hermes 盒端工具。 _(分支與發行版)_
- **[ChadolPilot](https://github.com/taylor224/openpilot)** — 以 sunnypilot 為基礎、針對 Hyundai／Kia／Genesis 的分支，加入 2025 年款角度轉向、Kia EV3 與 CCNC 支援，從 installer.comma.ai/taylor224/main 安裝；首次開機在裝置上建置，README 為韓文與英文。 _(分支與發行版)_
- **[jetson-cuda-overlay](https://github.com/feiyang2025/jetson-cuda-overlay)** — 可套用到 sunnypilot、openpilot 等分支的 NVIDIA Jetson AGX Orin CUDA／TensorRT 與 V4L2 鏡頭覆蓋層，讓各分支共用同一套 CUDA 推論與 GMSL 鏡頭路徑。 _(硬體與移植)_
- **[subaru-preglobal-icbm](https://github.com/khaled-khurram/subaru-preglobal-icbm)** — 給搭載 EyeSight 的 preglobal Subaru 用的 Intelligent Cruise Button Management：在 sunnypilot 上透過已在改寫的 ES_Distance 訊息模擬 ACC 按鍵，已在 2015 Outback 實車驗證；完整縱向控制仍是未完成的研究。 _(硬體與移植)_
- **[tesla-hw1-port](https://github.com/rampage1999/tesla-hw1-port)** — sunnypilot 分支，加入 2012–2016 年 Tesla Model S/X 舊平台（HW1／AP1，另含 HW2 與 HW3 設定），搭配對應的 [opendbc 分支](https://github.com/rampage1999/tesla-hw1-opendbc)提供 teslaLegacy panda 安全模型、Bosch 雷達與 DBC 更新；移植自 xnor-tech 的 tesla-unity。 _(硬體與移植)_
- **[fw_autopatch](https://github.com/SiliconTrailer/openpilot-tesla-fw-autopatch)** — 給 Tesla 更新後變成「Car Unrecognized: Dashcam Mode」的車主使用的腳本：讀取車輛回報的韌體版本，只把已知韌體系列的版本升級加入本機 opendbc 指紋；在 2021 Model 3、comma four、openpilot 0.11.2 上測試過。 _(CAN、DBC 與資料工具)_

<details>
<summary>本週另外新增 7 條</summary>

- **[Leapmotor B05 / Lafa5 CAN](https://github.com/a724271419/Leapmotor-B05-Lafa5-can)** — 零跑 B05／Lafa5（LPA120）的 openpilot 可行性研究：唯讀的 CAN 逆向文件與離線 Node.js 工具，包含已解碼的 CCAN ID、CarState 欄位與還原的 E2E 校驗，不含注入實作；README 為中文。 _(CAN、DBC 與資料工具)_
- **[ka2-settings](https://github.com/diamondlim/ka2-settings)** — 給 KA2（openpilot 系 ADAS 盒，用於 BYD Sealion 7）的 Android 前面板：透過藍牙 SPP 顯示即時狀態、ACC 按鍵、盒端依 schema 提供的設定清單、調校列與溫度。 _(行車紀錄、UI 與周邊)_
- **[SimSteer](https://github.com/140er/simsteer)** — 以畫面擷取搭配虛擬手把或方向盤，用 comma.ai openpilot 的視覺與規劃模型來開 Euro Truck Simulator 2、Assetto Corsa 與 Forza。 _(行車紀錄、UI 與周邊)_
- **[op助手](https://github.com/mouxangithub/ai)** — 給各 openpilot 分支（sunnypilot、FrogPilot、dragonpilot 等）的裝置端 AI 助手：聊天調參、路線診斷、車輛適配、SecOC、Cabana CAN 分析與社群 Wiki RAG，並提供裝置上的網頁介面；README 為中文。 _(行車紀錄、UI 與周邊)_
- **[CommaPlay](https://github.com/navipilot/commaplay)** — 在 comma 3 上執行的實驗性無線 CarPlay 接收模組：由裝置把 iPhone 的 CarPlay 畫面、聲音與觸控轉送到區網內的瀏覽器，不占用 openpilot 的螢幕；README 為中文。 _(行車紀錄、UI 與周邊)_
- **[openpilot-tailscale](https://github.com/TurboCE/openpilot-tailscale)** — 安裝腳本，把官方 Tailscale ARM64 執行檔裝到跑 openpilot、CarrotPilot 或 FrogPilot 的 AGNOS 裝置上，執行檔與登入狀態保存在 /data，開機 90 秒後由 systemd timer 啟動；README 為韓文。 _(自架後端與安裝工具)_
- **[openpilot-models](https://github.com/happymaj11r/openpilot-models)** — 給 openpilot（carrot 分支）的自訂駕駛模型合集，可在裝置上的模型介面選擇下載。 _(模型、訓練與研究)_

</details>

---

## 目錄

- [一覽比較](#一覽比較)
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

## 一覽比較

### 主要分支

資料取自各專案的 README 與 GitHub（2026-10-21）。分支變動很快，安裝前請以專案本身為準。

| 專案 | 與 openpilot 的關係 | 授權（GitHub） | README 提到的裝置 | 安裝／文件 |
|---|---|---|---|---|
| [openpilot](https://github.com/commaai/openpilot) | 上游（comma.ai） | MIT | comma four；另列 comma 3X 分支 | 安裝網址 `openpilot.comma.ai` · [docs.comma.ai](https://docs.comma.ai) |
| [sunnypilot](https://github.com/sunnypilot/sunnypilot) | openpilot 的分支 | MIT | 未載明 | [docs.sunnypilot.ai](https://docs.sunnypilot.ai/) · [社群論壇](https://community.sunnypilot.ai/) |
| [FrogPilot](https://github.com/FrogAi/FrogPilot) | 社群主導的分支 | MIT | comma 3／3X | 安裝網址 `frogpilot.download` · [FrogPilot wiki](https://frogpilot.com/wiki/) |
| [dragonpilot](https://github.com/dragonpilot/dragonpilot) | 以 openpilot 為基礎 | MIT | comma 3／3X 與 O3／O3L／O3XL；EON／C2 在 `d2` 分支 | [英文版 README](https://github.com/dragonpilot/dragonpilot/blob/pre-build/README_EN.md) |
| [StarPilot](https://github.com/StarPilotHQ/StarPilot) | 自訂分支 | MIT；README 註明部分改編自 sunnypilot 的程式碼另有自訂授權聲明 | comma 3、3X、4 | [wiki.firestar.link](https://wiki.firestar.link) |

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
- **[StarPilot](https://github.com/StarPilotHQ/StarPilot)** — 每月更新的開源分支。
- **[openpilot](https://github.com/j-vanetten/openpilot)** — jvePilot：FCA 車款混合 ACC。
- **[openpilot](https://github.com/BogGyver/openpilot)** — 給 pre-AP／AP1／AP2 Tesla 的分支。
- **[zoompilot](https://github.com/zoompilot/zoompilot)** — 以 Mazda 為主的分支。
- **[openpilot](https://github.com/crwusiz/openpilot)** — 韓國社群常用分支。
- **[openpilot](https://github.com/kisapilot/openpilot)** — 韓國社群分支。
- **[openpilot](https://github.com/jixiexiaoge/openpilot)** — 整合多個分支功能。
- **[flowpilot](https://github.com/flowdriveai/flowpilot)** — 可在 Android 手機執行的衍生系統。
- **[xpilot](https://github.com/onemiless/xpilot)** — 只支援 Tesla 的 sunnypilot 衍生版，透過插件宿主與裝置上的插件商店擴充功能；支援 comma 3、3X、3XL 與 four。
- **[carrotpilot](https://github.com/ajouatom/openpilot)** — 以 openpilot 為基礎、聚焦 Hyundai／Kia／Genesis 相容性與縱向操控體感的獨立駕駛輔助分支，從 i.carrotpilot.app/carrot-wip 安裝；支援 comma three、3X 與 four，README 為韓文、英文與簡體中文。
- **[BluePilot](https://github.com/BluePilotDev/bluepilot)** — 以 sunnypilot 為基礎、先在本地驗證再上游回報的 Ford 專用橫向與縱向強化分支，支援 comma 3X 與 comma 4，從 installer.comma.ai/BluePilotDev/bp-7.0 安裝。
- **[SunnyPilot-TeslaHW1](https://github.com/P6g9YHK6/SunnyPilot-TeslaHW1)** — 以 sunnypilot 為基礎、移植 Tesla Hardware 1／AP1 支援的分支（已在 2015 Model S 與 2016 Model X 測試），搭配 xnor 線束，支援 comma 3X 與 comma 4。
- **[sealion7ka2](https://github.com/diamondlim/sealion7ka2)** — KA2（openpilot 系 ADAS 盒，用於 BYD Sealion 7）分支的獨立備份：裝置追蹤的 longitudinal_off 分支，含 rate／alive gating 修正、無雷達規劃器與 ka2_hermes 盒端工具。
- **[ChadolPilot](https://github.com/taylor224/openpilot)** — 以 sunnypilot 為基礎、針對 Hyundai／Kia／Genesis 的分支，加入 2025 年款角度轉向、Kia EV3 與 CCNC 支援，從 installer.comma.ai/taylor224/main 安裝；首次開機在裝置上建置，README 為韓文與英文。

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
- **[jetson-cuda-overlay](https://github.com/feiyang2025/jetson-cuda-overlay)** — 可套用到 sunnypilot、openpilot 等分支的 NVIDIA Jetson AGX Orin CUDA／TensorRT 與 V4L2 鏡頭覆蓋層，讓各分支共用同一套 CUDA 推論與 GMSL 鏡頭路徑。
- **[subaru-preglobal-icbm](https://github.com/khaled-khurram/subaru-preglobal-icbm)** — 給搭載 EyeSight 的 preglobal Subaru 用的 Intelligent Cruise Button Management：在 sunnypilot 上透過已在改寫的 ES_Distance 訊息模擬 ACC 按鍵，已在 2015 Outback 實車驗證；完整縱向控制仍是未完成的研究。
- **[openpilot-honda-city-brasil](https://github.com/kriptomad/openpilot-honda-city-brasil)** — 以 STM32H725 重新設計、支援 CAN FD 的「Hybrid Panda」KiCad 電路板，加上讓黑色 panda（STM32F4）在目前 panda 程式碼上繼續運作的移植，以及 Honda City G7（巴西）在 openpilot v0.9.9 與 flowpilot 上的車型移植；尚未在硬體或實車上驗證。
- **[tesla-hw1-port](https://github.com/rampage1999/tesla-hw1-port)** — sunnypilot 分支，加入 2012–2016 年 Tesla Model S/X 舊平台（HW1／AP1，另含 HW2 與 HW3 設定），搭配對應的 [opendbc 分支](https://github.com/rampage1999/tesla-hw1-opendbc)提供 teslaLegacy panda 安全模型、Bosch 雷達與 DBC 更新；移植自 xnor-tech 的 tesla-unity。

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
- **[openpilot_ros2_bridge](https://github.com/jkk-research/openpilot_ros2_bridge)** — 給跑 openpilot 的 comma 3/3X 與 comma four 裝置用的 ROS 2（Jazzy）橋接，在車上電腦以預建 Docker 映像或本機安裝執行。
- **[fw_autopatch](https://github.com/SiliconTrailer/openpilot-tesla-fw-autopatch)** — 給 Tesla 更新後變成「Car Unrecognized: Dashcam Mode」的車主使用的腳本：讀取車輛回報的韌體版本，只把已知韌體系列的版本升級加入本機 opendbc 指紋；在 2021 Model 3、comma four、openpilot 0.11.2 上測試過。
- **[Leapmotor B05 / Lafa5 CAN](https://github.com/a724271419/Leapmotor-B05-Lafa5-can)** — 零跑 B05／Lafa5（LPA120）的 openpilot 可行性研究：唯讀的 CAN 逆向文件與離線 Node.js 工具，包含已解碼的 CCAN ID、CarState 欄位與還原的 E2E 校驗，不含注入實作；README 為中文。

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
- **[navdy-hud](https://github.com/geniuth/navdy-hud)** — 直接在已 root 的 Navdy HUD 上執行的 Android App，接收 comma 裝置經藍牙送出的行車資料，在 HUD 上畫出車道、前車、測速照相與盲點，不經過手機；README 為韓文。
- **[comma4-true-black](https://github.com/alanbixby/comma4-true-black)** — 實驗性工具，調整兩項顯示設定，嘗試修正 comma four 螢幕黑色區域微微泛紅或泛灰的問題，不需換分支或重刷；結束後還原原廠電壓並輸出報告。
- **[ka2-settings](https://github.com/diamondlim/ka2-settings)** — 給 KA2（openpilot 系 ADAS 盒，用於 BYD Sealion 7）的 Android 前面板：透過藍牙 SPP 顯示即時狀態、ACC 按鍵、盒端依 schema 提供的設定清單、調校列與溫度。
- **[SimSteer](https://github.com/140er/simsteer)** — 以畫面擷取搭配虛擬手把或方向盤，用 comma.ai openpilot 的視覺與規劃模型來開 Euro Truck Simulator 2、Assetto Corsa 與 Forza。
- **[op助手](https://github.com/mouxangithub/ai)** — 給各 openpilot 分支（sunnypilot、FrogPilot、dragonpilot 等）的裝置端 AI 助手：聊天調參、路線診斷、車輛適配、SecOC、Cabana CAN 分析與社群 Wiki RAG，並提供裝置上的網頁介面；README 為中文。
- **[CommaPlay](https://github.com/navipilot/commaplay)** — 在 comma 3 上執行的實驗性無線 CarPlay 接收模組：由裝置把 iPhone 的 CarPlay 畫面、聲音與觸控轉送到區網內的瀏覽器，不占用 openpilot 的螢幕；README 為中文。

## 自架後端與安裝工具

- **[connect-killer](https://github.com/MoreTore/connect-killer)** — openpilot 連線功能的自架後端。
- **[retropilot-server](https://github.com/florianbrede-ayet/retropilot-server)** — 替代 comma 後端與儀表板。
- **[openpilot-installer-generator](https://github.com/sshane/openpilot-installer-generator)** — 產生自訂分支安裝程式。
- **[comma-analytics](https://github.com/clickityclickclickclick/comma-analytics)** — 自架 Grafana 儀表板，分析 comma／openpilot 行程。
- **[openpilot-tailscale](https://github.com/TurboCE/openpilot-tailscale)** — 安裝腳本，把官方 Tailscale ARM64 執行檔裝到跑 openpilot、CarrotPilot 或 FrogPilot 的 AGNOS 裝置上，執行檔與登入狀態保存在 /data，開機 90 秒後由 systemd timer 啟動；README 為韓文。

## 模型、訓練與研究

- **[Openpilot-Deepdive](https://github.com/OpenDriveLab/Openpilot-Deepdive)** — 駕駛模型深入研究。
- **[openpilot.distill](https://github.com/YassineYousfi/openpilot.distill)** — 用自己的行程蒸餾模型。
- **[openpilot.perception](https://github.com/cristianku/openpilot.perception)** — 從 comma 裝置的道路影像做 3D 物件感知與定位，獨立於 openpilot 駕駛模型訓練。
- **[openpilot-local-finetune](https://github.com/klebeer/openpilot-local-finetune)** — 在筆電上用自己的行程微調 openpilot 駕駛模型。
- **[openpilot_carla_model_finetuner](https://github.com/jagoff2/openpilot_carla_model_finetuner)** — 在 CARLA 收集置中行駛樣本、微調 openpilot 駕駛模型並匯出到 comma 3X。
- **[openpilot-desktop](https://github.com/luzijun360/openpilot-desktop)** — 在 Mac 或 Windows 上對行車影片跑 openpilot 駕駛模型，疊出 comma 同款車道線與路徑。
- **[mqb-eps-research](https://github.com/brendanballon/mqb-eps-research)** — 研究 VW MQB 電動輔助轉向韌體，想提升 openpilot 的轉向力道與反應；目前仍是離線研究，尚無實車驗證的修改。
- **[comma10k-baseline](https://github.com/YassineYousfi/comma10k-baseline)** — comma10k 分割基準。
- **[openpilot-pipeline](https://github.com/mbalesni/openpilot-pipeline)** — 端到端訓練流程。
- **[openpilot-supercombo-model](https://github.com/MTammvee/openpilot-supercombo-model)** — 使用 supercombo ONNX 模型。
- **[traffic-lights](https://github.com/sshane/traffic-lights)** — 紅綠燈辨識模型與資料。
- **[openpilot-models](https://github.com/happymaj11r/openpilot-models)** — 給 openpilot（carrot 分支）的自訂駕駛模型合集，可在裝置上的模型介面選擇下載。
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

完整規則見 [CONTRIBUTING.md](CONTRIBUTING.md)，也可以用 issue 表單[推薦專案](https://github.com/hypery11/awesome-openpilot/issues/new?template=suggest-project.yml)。

## 授權

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允許範圍內，貢獻者放棄本作品的所有著作權。
