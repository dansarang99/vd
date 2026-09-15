# {{PROJECT_NAME}} — Design Tokens & CSS Specification
> Reference Source: `{{REFERENCE_SOURCE}}`  
> Base CSS Standard: W3C Compliant, Modern CSS Variables

---

## 1. Master CSS Token Variables

```css
:root {
  /* ---------------- Brand & Foundation Tokens ---------------- */
  --primary-navy:    {{PRIMARY_NAVY}};     /* Default: #0F2742 - High authority dark background & primary text */
  --secondary-slate: {{SECONDARY_SLATE}};  /* Default: #1E4260 - Secondary headlines & card body text */
  --muted-slate:     {{MUTED_SLATE}};      /* Default: #5D7186 - Captions, footnotes, citations */
  --pure-white:      #FFFFFF;              /* Card surfaces, inverted text */
  
  /* ---------------- Accent Color Palette ---------------- */
  --accent-1:        {{ACCENT_1}};         /* Default: #D9481F - Coral / Warm Alert / Primary Kicker */
  --accent-2:        {{ACCENT_2}};         /* Default: #14707E - Deep Teal / Growth / Balanced Metric */
  --accent-3:        {{ACCENT_3}};         /* Default: #B07D18 - Amber Gold / Caution / Strategic Target */
  --accent-4:        {{ACCENT_4}};         /* Default: #2C5282 - Royal Slate / Secondary Accent */

  /* ---------------- Surface & Container Tints ---------------- */
  --canvas-ice:      {{CANVAS_ICE}};       /* Default: #DCEAF6 - Cover background tint */
  --canvas-tint:     {{CANVAS_TINT}};      /* Default: #F8FAFC - Main content background */
  --tint-cool:       {{TINT_COOL}};        /* Default: #F1F6F9 - Soft cool card fill / light banner */
  --tint-peach:      {{TINT_PEACH}};       /* Default: #FAECE8 - Danger / highlight quadrant fill */
  --card-border:     {{CARD_BORDER}};      /* Default: #D4DFE9 - 1.5px or 2px clean border */

  /* ---------------- Elevation & Geometry ---------------- */
  --radius-sm:       8px;
  --radius-md:       16px;
  --radius-lg:       20px;
  --radius-full:     9999px;
  --shadow-card:     0 8px 24px rgba(15, 39, 66, 0.04);
  --shadow-hover:    0 12px 32px rgba(15, 39, 66, 0.08);

  /* ---------------- Typography Families ---------------- */
  --font-family:     'Pretendard', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Malgun Gothic", sans-serif;
}
```

---

## 2. Typography Token Scale (1920x1080 Viewport)

| Role | CSS Variable | Font Size | Line Height | Weight | Letter Spacing |
|:---|:---|:---:|:---:|:---:|:---:|
| **Hero Metric** | `--fs-hero` | 96px ~ 104px | 1.0 | 900 | -1px |
| **Cover Headline** | `--fs-cover` | 68px ~ 76px | 1.15 | 800 | -0.5px |
| **Slide Main Title** | `--fs-title` | 52px ~ 58px | 1.25 | 800 | -0.5px |
| **Card / Box Title** | `--fs-card-title`| 30px ~ 34px | 1.35 | 700 | 0px |
| **Banner Takeaway** | `--fs-banner` | 24px ~ 26px | 1.4 | 700 | 0px |
| **Card Body Text** | `--fs-body` | 22px ~ 24px | 1.55 | 400 ~ 500 | 0px |
| **Kicker Tag** | `--fs-kicker` | 20px ~ 22px | 1.2 | 700 | +2px (Uppercase) |
| **Footnote / Pagination** | `--fs-footnote` | 18px ~ 19px | 1.4 | 400 | 0px |

---

## 3. Standard Component CSS Boilerplate

```css
/* Card Container */
.executive-card {
  background: var(--pure-white);
  border: 2px solid var(--card-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-card);
  padding: 36px 32px;
  display: flex;
  flex-direction: column;
}

/* Full-width Takeaway Banner (Dark) */
.takeaway-banner-dark {
  background: var(--primary-navy);
  color: var(--pure-white);
  border-radius: var(--radius-md);
  padding: 24px 36px;
  font-size: var(--fs-banner);
  font-weight: 700;
  line-height: 1.4;
  display: flex;
  align-items: center;
}

/* Full-width Takeaway Banner (Cool Tint) */
.takeaway-banner-cool {
  background: var(--tint-cool);
  color: var(--primary-navy);
  border: 1.5px solid var(--card-border);
  border-radius: var(--radius-md);
  padding: 22px 36px;
  font-size: var(--fs-banner);
  font-weight: 600;
  line-height: 1.45;
  font-style: italic;
}

/* Kicker Tag */
.kicker-tag {
  font-size: var(--fs-kicker);
  font-weight: 700;
  color: var(--accent-1);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 12px;
}

/* Hero Badge */
.circle-badge {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--pure-white);
  font-size: 22px;
  font-weight: 800;
}
```
