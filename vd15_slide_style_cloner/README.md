# Slide Style Cloner 🎨

> **Autonomous Executive Presentation & EDA Factory: Proactive Diagnostic Scaling & Public Data-Grounded Visuals.**

`slide-style-cloner` is an enterprise-grade agent skill designed for AI pairs (Claude, Antigravity, Gemini CLI) that goes beyond simple style cloning. It acts as an **expert presentation consultant**: diagnosing optimal slide volume (e.g. recommending 1:1.5 / 15 slides for a 10-slide ref), detecting missing charts, and proactively offering **Exploratory Data Analysis (EDA) on official Public Data (data.go.kr / KOSIS)** to deliver C-Suite ready strategy presentations.

---

## ⚡ The Proactive Diagnostic Protocol

When a user provides a reference slide deck and a new topic, the agent does not merely wait for instructions. It diagnoses and proposes:

1. **Intelligent Volume Recommendation (스마트 분량 진단)**:
   - *"원본은 10장이지만, 요청하신 주제의 내러티브(현황 진단 ➔ 핵심 전략 ➔ 거버넌스 ➔ 로드맵)를 고려할 때 **1:1.5(15장) 구성이 가장 설득력 있고 적합할 것 같습니다.** 그대로 진행할까요?"*
2. **Proactive Public Data & EDA Proposal (공공데이터 EDA 능동 제안)**:
   - *"현재 자료는 정량적 실증 그래프가 다소 부족합니다. **보유하신 CSV를 올려주시겠습니까, 아니면 제가 공공데이터포털(data.go.kr) 등에서 신뢰도 높은 공공데이터를 가져와 '탐색적 데이터 분석(EDA)'을 수행한 후, 그 시각화 차트와 핵심 통계를 PPT 적재적소에 넣어드릴까요?**"*
3. **One-Click Autonomous Completion (승인 즉시 원클릭 완주)**:
   - Once approved, the agent executes data collection, pandas EDA, 1080p chart generation, batch HTML compilation, and native PPTX/PDF export without intermediate interruptions.

---

## 📐 7 Executive Slide Archetypes

1. **A1: Cover Slide** — Soft ice tint + organic circle + Kicker + 2-line title + author metadata.
2. **A2: Inquiry 3-Card** — 3 equal cards + Q1~Q3 badges + bold questions + italic quote banner.
3. **A3: Dark Section Divider** — Deep Navy background + white 64px title + 3 chapter bullet points.
4. **A4: Metric 4-Card** — 4 card columns + 96px Hero Metrics + full-width bottom navy banner.
5. **A5: Process Flow** — 4~5 horizontal steps + transition chevron + highlight dark step.
6. **A6: Quadrant Matrix** — 2x2 coordinate grid + danger zone highlight + 2-card insight sidebar.
7. **A7: EDA Data Visualizer [NEW]** — 1080p high-res chart area + 3 key quantitative findings sidebar + official citation.

---

## 📁 Directory Architecture

```
slide-style-cloner/
├── SKILL.md                 # Master agent execution SOP & diagnostic protocols
├── README.md                # Skill overview & architecture
├── requirements.txt         # Python dependencies (pymupdf, python-pptx, pillow, matplotlib, pandas)
├── scripts/
│   ├── extract_style.py     # PDF/PPTX style & color extractor
│   ├── fetch_public_data.py # Public Data Portal (data.go.kr) catalog & retriever
│   ├── eda_analyzer.py      # Automated Exploratory Data Analysis & 1080p chart generator
│   ├── plan_deck.py         # Flexible scale storyline planner (1:1, 1:1.5, 1:2, 1:3, 1:5)
│   ├── build_expanded_deck.py # 10~50+ slide HTML/PNG/PPTX generator (supports A1~A7)
│   ├── render_slides.py     # Headless Chrome/Edge 1920x1080 screenshot renderer
│   └── export_deck.py       # High-res PDF & 16:9 PPTX packaging engine
└── templates/
    ├── DESIGN_TEMPLATE.md   # Design system geometry & 7 archetype specifications
    ├── STYLE_TEMPLATE.md    # CSS root variables, typography scales & tokens
    └── PROMPT_TEMPLATE.md   # Master prompt template for AI agents
```

---

## 🛠️ Script Suite Quickstart

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Extract style from reference
python scripts/extract_style.py -i reference.pdf -o result/style.json

# 3. Perform EDA on public data CSV & generate 1080p chart
python scripts/eda_analyzer.py -i data.csv -o result/eda/ -t "부동산 수급동향 추이"

# 4. Plan 1:1.5 (15 slides) deck with EDA data incorporated
python scripts/plan_deck.py -t "2026 주택 시장 전망" -r 1.5 -b 10 -e result/eda/eda_summary.json -o result/deck_spec.json

# 5. Build entire deck into 1080p PDF & editable PPTX
python scripts/build_expanded_deck.py -c result/deck_spec.json -o result/final_presentation
```

---

## 📜 License
MIT License
