# 📐 DESIGN.md (디자인 8요소 마스터 명세서)

## 디자인 8요소 마스터 테이블

| 번호 | 디자인 요소 | 핵심 파라미터 | 슬라이드 실측 규격 |
| :---: | :--- | :--- | :--- |
| **1** | **Canvas & Grid** | Aspect Ratio: 16:9<br>Dimensions: 1920×1080px (13.333" × 7.5")<br>Safe Padding: Top 80px, Left 100px | 3-Column Card Layout<br>Card Width: 520px, Gap: 40px |
| **2** | **Color System** | Base Background: `#0B0F19` (Obsidian Dark)<br>Card Surface: `rgba(255, 255, 255, 0.04)`<br>Primary Accent: `#3B82F6` (Electric Blue)<br>Secondary Accent: `#10B981` (Emerald Green) | Text High: `#FFFFFF`<br>Text Mid: `#94A3B8`<br>Text Low: `#64748B` |
| **3** | **Typography** | Font Family: `Pretendard`, `Inter`<br>Weight: Bold (700), Black (900), Regular (400) | Title: 28pt Bold<br>Hero Metric: 44pt Black<br>Unit: 11pt Bold<br>Body: 11pt Regular |
| **4** | **Shape & Radius** | Card Border Radius: 16px (`rounded-2xl`)<br>Badge/Chip Radius: 9999px (Pill) | Button/Card: 16px 곡률 통일 |
| **5** | **Borders & Dividers**| Card Border: `1px solid rgba(255, 255, 255, 0.12)`<br>Hero Accent Border: `2px solid #3B82F6` | Hairline 글래스 림 효과 |
| **6** | **Elevation & Depth**| Box Shadow: `0 12px 32px -4px rgba(0, 0, 0, 0.5)`<br>Hero Glow: `radial-gradient(rgba(59,130,246,0.2))` | 카드가 배경에서 붕 떠오르는 입체감 |
| **7** | **Surface Material** | Glassmorphism (`backdrop-filter: blur(20px)`), 반투명 아크릴 표면 | 불투명 플라스틱 배제, 간유리 질감 |
| **8** | **Icon & Decor** | 3D 네온 엠블럼, 1px 도트 인디케이터, 테크 뱃지 | 각 카드 상단 32px 심볼 배치 |
