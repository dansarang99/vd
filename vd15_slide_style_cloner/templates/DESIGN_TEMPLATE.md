# {{PROJECT_NAME}} — Executive Presentation Design System
> Reference Source: `{{REFERENCE_SOURCE}}`  
> Resolution Standard: 1920x1080 Widescreen (16:9) | Base Virtual Grid: 960x540 pt

---

## 1. Design Philosophy & Architectural Principles

This design system is engineered for executive-level (C-Suite & Board) strategy presentations. It prioritizes clarity, cognitive speed, and institutional credibility over decorative fluff.

1. **Information-First Minimalism**
   - Eliminate non-functional clip arts, frivolous gradients, and decorative 3D graphics.
   - Information priority is communicated through **Typography Scale Contrast** and **Deliberate Accent Color Coding**.
2. **Strict Card Container Architecture**
   - Package all substantive content within distinct white card containers (`background: #FFFFFF`, subtle border, gentle box-shadow).
   - This prevents cognitive fatigue and allows immediate horizontal/vertical visual scanning.
3. **Dual Atmosphere Strategy**
   - **Light Mode (Content & Analysis Slides)**: Pure white / crisp cool tint background for maximum text contrast and data readability.
   - **Dark Mode (Cover & Section Dividers)**: Deep navy background for authoritative gravity and clear transition pauses between strategic pillars.

---

## 2. Canvas Geometry & Spatial Grid (1920x1080 Full HD)

```
+-------------------------------------------------------------------------------+
|  Y: 72px   [ KICKER TAG: {{KICKER_TEXT}} (Accent Color, 20-22px, Bold) ]     |
|  Y: 110px  [ MAIN TITLE: {{SLIDE_HEADLINE}} (Primary Color, 52-58px, 800) ]   |
|-------------------------------------------------------------------------------|
|  Y: 220px  [ CONTENT CONTAINER AREA ]                                         |
|            - 3-Card Grid: Width 530px each | Gap 32px                         |
|            - 4-Card Grid: Width 390px each | Gap 24px                         |
|            - 2-Column Split: 1060px (Left) + 640px (Right) | Gap 40px         |
|  Y: 860px                                                                     |
|-------------------------------------------------------------------------------|
|  Y: 880px  [ FULL-WIDTH CALLOUT / TAKEAWAY BANNER (Height: 88-100px) ]        |
|-------------------------------------------------------------------------------|
|  Y: 1010px [ FOOTNOTE / SOURCE (18px) ]               [ SLIDE NUMBER (18px) ] |
+-------------------------------------------------------------------------------+
```

- **Canvas Dimensions**: `1920px × 1080px` (Fixed, `overflow: hidden`)
- **Safe Margins**:
  - Left / Right Margin: `90px` (Content width: `1740px`)
  - Top Margin: `72px`
  - Bottom Margin: `45px`
- **Spatial Hierarchy**:
  - Header height: `~150px`
  - Main content height: `~640px`
  - Bottom takeaway height: `~88px`
  - Footer height: `~40px`

---

## 3. Information & Typography Hierarchy

| Level | Component | Desktop Size (px) | Equivalent (pt) | Weight | Color Token | Purpose |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **L1** | **Kicker Tag** | 20~22px | 11.1pt | 700 Bold | `{{ACCENT_PRIMARY}}` | Pillar / chapter context, uppercase, letter-spacing +2px |
| **L2** | **Slide Title** | 52~58px | 30.0pt | 800 ExtraBold | `{{PRIMARY_NAVY}}` | The single core message. Use em-dash (`—`) for contrast. |
| **L3** | **Hero Metric** | 96~104px | 52.0pt | 900 Black | Accent Palette | Giant statistical impact number (with `%` or `x`) |
| **L4** | **Card Title** | 30~34px | 17.0pt | 700 Bold | `{{PRIMARY_NAVY}}` | Sub-headline, question, or key category name |
| **L5** | **Card Body** | 22~24px | 12.0pt | 400 Regular | `{{SECONDARY_SLATE}}` | Analytical explanations, structured bullet items (Line-height: 1.5) |
| **L6** | **Takeaway Banner** | 24~26px | 13.5pt | 700 Bold | White / Navy | Executive synthesis banner across full content width |
| **L7** | **Metadata / Footnote**| 18~19px | 9.5pt | 400 Regular | `{{MUTED_SLATE}}` | Data sources, citations, and slide numbering |

---

## 4. The 6 Core Executive Slide Archetypes

### Archetype 1: Strategic Title Cover (Cover)
- **Mood**: Elegant, high-authority entry slide.
- **Background**: Soft Ice Tint (`{{CANVAS_ICE}}`) with an organic circular graphic (`width: 1100px`, `border-radius: 50%`, `right: -250px`, opacity 0.6).
- **Structure**:
  - Top Kicker Badge: Pill tag (`{{ACCENT_PRIMARY}}`)
  - Main Title: 72px ExtraBold, 2 lines max
  - Subtitle: 28px Slate Navy with horizontal accent line
  - Author / Organization Metadata box at bottom left

### Archetype 2: Key Strategic Questions (Inquiry 3-Card)
- **Mood**: High-focus diagnostic slide framing core problems.
- **Background**: Crisp White Canvas.
- **Structure**:
  - 3 Equal Cards (`width: 550px`, `height: 600px`, `gap: 30px`).
  - Top Circular Badge: Q1 (`{{ACCENT_1}}`), Q2 (`{{ACCENT_2}}`), Q3 (`{{ACCENT_3}}`) (Diameter: 56px).
  - Bold Question text (34px, 3 lines max) followed by 2-3 supporting evidence bullets.
  - Bottom full-width Callout Banner: Cool ice tint with quote or strategic premise.

### Archetype 3: Section Pillar Divider (Dark Divider)
- **Mood**: Heavy gravitas, signaling chapter transitions.
- **Background**: Deep Navy (`{{PRIMARY_NAVY}}`) with subtle dark slate geometric curvature.
- **Structure**:
  - Kicker: Glowing accent color (`{{ACCENT_PRIMARY}}`)
  - Main Chapter Title: 64px White ExtraBold
  - Executive Overview: 28px soft blue text
  - 3 Key Takeaway Bullet points with glowing accent bullet dots (`•`)

### Archetype 4: Key Performance & Reality Metrics (Metric 4-Card)
- **Mood**: Data-driven, empirical proof slide.
- **Structure**:
  - 4 Column Cards (`width: 405px`, `gap: 24px`).
  - Top: Massive Hero Metric (`96px`, bold accent color).
  - Sub-label & 2 descriptive analytical sentences.
  - Bottom Banner: Full-width Dark Navy banner summarizing the strategic conclusion.

### Archetype 5: Transformation Roadmap & Pipeline (Process Flow)
- **Mood**: Step-by-step evolution, pipeline, or architecture progression.
- **Structure**:
  - 4 to 5 Horizontal Step Cards connected by chevron arrows or progress line.
  - Step Number Badge (`01`, `02`, `03`...) at card top.
  - Highlighted Step: Crucial inflection point styled with inverted Dark Navy background.
  - Bottom Banner: Transition bottleneck takeaway.

### Archetype 6: Strategic Priority Matrix (Quadrant 2x2 with Sidebar)
- **Mood**: Trade-off decision, risk vs. return, or technology landscape analysis.
- **Structure**:
  - Left Canvas (1100px): 2x2 Coordinate Grid (X/Y axes with clear polar labels).
  - Top-Right "Critical / Danger / High-Value" Zone highlighted with subtle peach tint (`{{TINT_PEACH}}`).
  - Interactive Pill tags placed precisely within the 4 quadrants.
  - Right Sidebar (580px): 2 stacked synthesis cards (e.g. "Key Discovery" + "Action Principle").

---

## 5. Defensive Design & Quality Assurance Rules

1. **Card Text Limit**: Maximum 4 bullet points per card. Never allow text to exceed card boundaries.
2. **Strict Font Stack**: Use `@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');` as primary font family, falling back to `-apple-system, BlinkMacSystemFont, "Malgun Gothic", sans-serif`.
3. **Never Use Unprocessed Color Codes**: Always reference defined tokens (`var(--primary-navy)`, etc.).
4. **Mandatory Kicker & Bottom Banner**: No substantive content slide is complete without a top Kicker tag and a bottom Takeaway banner.
