#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expanded Deck Engine (Bulk 20~50+ Slide Generator)
Takes a structured JSON deck specification, generates pixel-perfect 1920x1080 HTML slides
for the 6 core archetypes, and automatically triggers headless rendering and PDF/PPTX export.
"""

import sys
import os
import json
import argparse
import subprocess
from typing import Dict, Any, List

COMMON_CSS = """
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
}

body {
  width: 1920px;
  height: 1080px;
  overflow: hidden;
  font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Malgun Gothic", sans-serif;
  background-color: #FFFFFF;
  color: #0F2742;
  position: relative;
}

.slide-header {
  position: absolute;
  top: 72px;
  left: 90px;
  right: 90px;
}

.kicker {
  font-size: 22px;
  font-weight: 700;
  color: #D9481F;
  letter-spacing: 2px;
  margin-bottom: 12px;
  text-transform: uppercase;
}

.slide-title {
  font-size: 54px;
  font-weight: 800;
  color: #0F2742;
  line-height: 1.25;
  letter-spacing: -0.5px;
}

.slide-content {
  position: absolute;
  top: 220px;
  left: 90px;
  right: 90px;
  bottom: 160px;
}

.card {
  background: #FFFFFF;
  border: 2px solid #D4DFE9;
  border-radius: 20px;
  box-shadow: 0 8px 24px rgba(15, 39, 66, 0.04);
}

.bottom-banner-dark {
  position: absolute;
  bottom: 75px;
  left: 90px;
  right: 90px;
  background: #0F2742;
  border-radius: 16px;
  color: #FFFFFF;
  padding: 22px 36px;
  font-size: 24px;
  font-weight: 700;
  line-height: 1.4;
  display: flex;
  align-items: center;
}

.bottom-banner-cool {
  position: absolute;
  bottom: 75px;
  left: 90px;
  right: 90px;
  background: #F1F6F9;
  border: 1.5px solid #D4DFE9;
  border-radius: 16px;
  color: #0F2742;
  padding: 22px 36px;
  font-size: 23px;
  font-weight: 600;
  font-style: italic;
  line-height: 1.45;
  display: flex;
  align-items: center;
}

.slide-footer {
  position: absolute;
  bottom: 32px;
  left: 90px;
  right: 90px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  color: #5D7186;
}
"""

def generate_cover_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    navy = theme.get("primary_navy", "#0F2742")
    coral = theme.get("accent_coral", "#D9481F")
    ice = theme.get("canvas_ice", "#DCEAF6")
    slate = theme.get("secondary_slate", "#1E4260")
    
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>
{COMMON_CSS}
body {{ background-color: {ice}; }}
.circle-bg {{
  position: absolute;
  width: 1100px;
  height: 1100px;
  right: -250px;
  top: -100px;
  border-radius: 50%;
  background: radial-gradient(circle, #C2DBEF 0%, #B0D0EB 60%, rgba(176, 208, 235, 0) 70%);
  z-index: 1;
}}
.cover-content {{
  position: absolute;
  top: 300px;
  left: 90px;
  max-width: 1100px;
  z-index: 2;
}}
.cover-kicker {{
  display: inline-block;
  background: {coral};
  color: #FFFFFF;
  padding: 10px 24px;
  border-radius: 30px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: 2px;
  margin-bottom: 24px;
}}
.cover-title {{
  font-size: 68px;
  font-weight: 800;
  color: {navy};
  line-height: 1.25;
  margin-bottom: 24px;
}}
.cover-sub {{
  font-size: 28px;
  color: {slate};
  line-height: 1.5;
  margin-bottom: 40px;
}}
.cover-meta {{
  font-size: 20px;
  color: #5D7186;
  font-weight: 500;
}}
</style></head>
<body>
  <div class="circle-bg"></div>
  <div class="cover-content">
    <div class="cover-kicker">{s.get('kicker', 'STRATEGY DECK')}</div>
    <h1 class="cover-title">{s.get('title', 'Executive Presentation')}</h1>
    <div class="cover-sub">{s.get('subtitle', '')}</div>
    <div class="cover-meta">{s.get('author', 'Executive Strategy Team')}</div>
  </div>
  <div class="slide-footer">
    <div>CONFIDENTIAL & PROPRIETARY</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def generate_dark_divider_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    navy = theme.get("primary_navy", "#0F2742")
    coral = theme.get("accent_coral", "#D9481F")
    
    bullets = "".join([f"<li style='margin-bottom: 14px;'><span style='color:{coral}; font-weight:bold; margin-right:12px;'>•</span>{b}</li>" for b in s.get('bullets', [])])
    
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>
{COMMON_CSS}
body {{ background-color: {navy}; color: #FFFFFF; }}
.divider-box {{
  position: absolute;
  top: 260px;
  left: 90px;
  right: 90px;
}}
.divider-kicker {{
  font-size: 24px;
  font-weight: 700;
  color: {coral};
  letter-spacing: 3px;
  margin-bottom: 20px;
}}
.divider-title {{
  font-size: 64px;
  font-weight: 800;
  color: #FFFFFF;
  line-height: 1.25;
  margin-bottom: 30px;
}}
.divider-sub {{
  font-size: 28px;
  color: #D5E4EF;
  line-height: 1.5;
  margin-bottom: 40px;
}}
.divider-bullets {{
  list-style: none;
  font-size: 24px;
  color: #E2ECF3;
  line-height: 1.6;
}}
</style></head>
<body>
  <div class="divider-box">
    <div class="divider-kicker">{s.get('kicker', 'PART')}</div>
    <h1 class="divider-title">{s.get('title', 'Chapter Title')}</h1>
    <div class="divider-sub">{s.get('subtitle', '')}</div>
    <ul class="divider-bullets">{bullets}</ul>
  </div>
  <div class="slide-footer" style="color: #8CA4BA;">
    <div>STRATEGIC TRANSITION</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def generate_inquiry_3card_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    cards_html = []
    default_colors = [theme.get("accent_coral", "#D9481F"), theme.get("accent_teal", "#14707E"), theme.get("accent_amber", "#B07D18")]
    
    for i, card in enumerate(s.get('cards', [])[:3]):
        color = default_colors[i % len(default_colors)]
        bullets = "".join([f"<li style='margin-bottom: 12px;'><span style='color:{color}; font-weight:bold; margin-right:8px;'>•</span>{b}</li>" for b in card.get('bullets', [])])
        cards_html.append(f"""
        <div class="card" style="flex: 1; padding: 40px 32px; display: flex; flex-direction: column;">
          <div style="display: flex; align-items: center; margin-bottom: 24px;">
            <div style="width: 52px; height: 52px; border-radius: 50%; background: {color}; color: #FFFFFF; font-size: 22px; font-weight: 800; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
              {card.get('badge', f'Q{i+1}')}
            </div>
            <div style="font-size: 28px; font-weight: 700; color: #0F2742;">{card.get('title', '')}</div>
          </div>
          <div style="font-size: 24px; font-weight: 700; color: #1E4260; line-height: 1.4; margin-bottom: 20px;">
            {card.get('headline', '')}
          </div>
          <ul style="list-style: none; font-size: 21px; color: #5D7186; line-height: 1.55; flex-grow: 1;">
            {bullets}
          </ul>
        </div>
        """)
        
    banner_cls = "bottom-banner-cool" if s.get("banner_type") == "cool" else "bottom-banner-dark"
    
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{COMMON_CSS}</style></head>
<body>
  <div class="slide-header">
    <div class="kicker">{s.get('kicker', 'INQUIRY')}</div>
    <h1 class="slide-title">{s.get('title', '')}</h1>
  </div>
  <div class="slide-content" style="display: flex; gap: 30px; height: 600px;">
    {''.join(cards_html)}
  </div>
  <div class="{banner_cls}">
    {s.get('takeaway', '')}
  </div>
  <div class="slide-footer">
    <div>출처: {s.get('source', '내부 전략 분석')}</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def generate_metric_4card_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    cards_html = []
    colors = [theme.get("accent_coral", "#D9481F"), theme.get("accent_teal", "#14707E"), theme.get("accent_amber", "#B07D18"), theme.get("primary_navy", "#0F2742")]
    
    for i, card in enumerate(s.get('cards', [])[:4]):
        color = colors[i % len(colors)]
        bullets = "".join([f"<li style='margin-bottom: 8px;'>{b}</li>" for b in card.get('bullets', [])])
        cards_html.append(f"""
        <div class="card" style="flex: 1; padding: 36px 28px; display: flex; flex-direction: column;">
          <div style="font-size: 88px; font-weight: 900; color: {color}; line-height: 1.0; margin-bottom: 16px;">
            {card.get('metric', '0%')}
          </div>
          <div style="font-size: 26px; font-weight: 700; color: #0F2742; margin-bottom: 14px;">
            {card.get('title', '')}
          </div>
          <div style="font-size: 21px; color: #1E4260; line-height: 1.45; margin-bottom: 14px;">
            {card.get('desc', '')}
          </div>
          <ul style="list-style: none; font-size: 19px; color: #5D7186; line-height: 1.5; flex-grow: 1;">
            {bullets}
          </ul>
        </div>
        """)
        
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{COMMON_CSS}</style></head>
<body>
  <div class="slide-header">
    <div class="kicker">{s.get('kicker', 'KEY METRICS')}</div>
    <h1 class="slide-title">{s.get('title', '')}</h1>
  </div>
  <div class="slide-content" style="display: flex; gap: 24px; height: 600px;">
    {''.join(cards_html)}
  </div>
  <div class="bottom-banner-dark">
    {s.get('takeaway', '')}
  </div>
  <div class="slide-footer">
    <div>출처: {s.get('source', '데이터 분석 및 실증 지표')}</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def generate_process_flow_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    steps_html = []
    steps = s.get('steps', [])
    navy = theme.get("primary_navy", "#0F2742")
    coral = theme.get("accent_coral", "#D9481F")
    
    for i, step in enumerate(steps[:5]):
        is_highlight = step.get('highlight', False)
        bg = navy if is_highlight else "#FFFFFF"
        text_color = "#FFFFFF" if is_highlight else "#0F2742"
        sub_color = "#D5E4EF" if is_highlight else "#5D7186"
        badge_bg = coral if is_highlight else "#DCEAF6"
        badge_text = "#FFFFFF" if is_highlight else navy
        
        bullets = "".join([f"<li style='margin-bottom: 8px;'>{b}</li>" for b in step.get('bullets', [])])
        
        steps_html.append(f"""
        <div class="card" style="flex: 1; background: {bg}; color: {text_color}; padding: 32px 24px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div style="padding: 6px 14px; border-radius: 8px; background: {badge_bg}; color: {badge_text}; font-size: 18px; font-weight: 800;">
              STEP {i+1:02d}
            </div>
            {f'<div style="font-size:16px; font-weight:700; color:{coral};">★ KEY FOCUS</div>' if is_highlight else ''}
          </div>
          <div style="font-size: 26px; font-weight: 800; line-height: 1.3; margin-bottom: 14px;">
            {step.get('title', '')}
          </div>
          <div style="font-size: 20px; color: {sub_color}; line-height: 1.45; margin-bottom: 14px;">
            {step.get('desc', '')}
          </div>
          <ul style="list-style: none; font-size: 18px; color: {sub_color}; line-height: 1.5; flex-grow: 1;">
            {bullets}
          </ul>
        </div>
        """)
        
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{COMMON_CSS}</style></head>
<body>
  <div class="slide-header">
    <div class="kicker">{s.get('kicker', 'PROCESS & ROADMAP')}</div>
    <h1 class="slide-title">{s.get('title', '')}</h1>
  </div>
  <div class="slide-content" style="display: flex; gap: 20px; height: 600px;">
    {''.join(steps_html)}
  </div>
  <div class="bottom-banner-dark">
    {s.get('takeaway', '')}
  </div>
  <div class="slide-footer">
    <div>출처: {s.get('source', '실행 프레임워크 및 로드맵')}</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def generate_quadrant_matrix_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    navy = theme.get("primary_navy", "#0F2742")
    coral = theme.get("accent_coral", "#D9481F")
    teal = theme.get("accent_teal", "#14707E")
    
    pills_html = []
    for pill in s.get('matrix_items', []):
        top = pill.get('y', 50)
        left = pill.get('x', 50)
        is_alert = pill.get('alert', False)
        bg = coral if is_alert else "#FFFFFF"
        fg = "#FFFFFF" if is_alert else navy
        border = f"border: 2px solid {coral};" if is_alert else "border: 2px solid #D4DFE9;"
        pills_html.append(f"""
        <div style="position: absolute; top: {top}px; left: {left}px; background: {bg}; color: {fg}; {border} padding: 10px 20px; border-radius: 30px; font-size: 20px; font-weight: 700; box-shadow: 0 4px 12px rgba(0,0,0,0.06); white-space: nowrap;">
          {pill.get('text', '')}
        </div>
        """)
        
    side_cards = []
    for sc in s.get('sidebar_cards', [])[:2]:
        is_dark = sc.get('dark', False)
        bg = navy if is_dark else "#F1F6F9"
        fg = "#FFFFFF" if is_dark else navy
        tag_color = coral if is_dark else teal
        side_cards.append(f"""
        <div class="card" style="flex: 1; background: {bg}; color: {fg}; padding: 32px 28px; display: flex; flex-direction: column; justify-content: center;">
          <div style="font-size: 20px; font-weight: 800; color: {tag_color}; margin-bottom: 12px;">{sc.get('tag', 'INSIGHT')}</div>
          <div style="font-size: 24px; font-weight: 700; line-height: 1.45;">{sc.get('text', '')}</div>
        </div>
        """)
        
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{COMMON_CSS}</style></head>
<body>
  <div class="slide-header">
    <div class="kicker">{s.get('kicker', 'STRATEGIC MATRIX')}</div>
    <h1 class="slide-title">{s.get('title', '')}</h1>
  </div>
  <div class="slide-content" style="display: flex; gap: 30px; height: 620px;">
    <!-- 2x2 Matrix Area -->
    <div class="card" style="flex: 1.8; position: relative; background: #F8FAFC; overflow: hidden; border: 2px solid #D4DFE9;">
      <!-- Axis Lines -->
      <div style="position: absolute; top: 50%; left: 40px; right: 40px; height: 2px; background: #CBD5E1;"></div>
      <div style="position: absolute; left: 50%; top: 40px; bottom: 40px; width: 2px; background: #CBD5E1;"></div>
      <!-- Top Right Highlight Zone -->
      <div style="position: absolute; top: 0; right: 0; width: 50%; height: 50%; background: #FAECE8; opacity: 0.6;"></div>
      <!-- Axis Labels -->
      <div style="position: absolute; top: 16px; left: 50%; transform: translateX(-50%); font-size: 18px; font-weight: 800; color: #5D7186;">{s.get('y_axis_high', 'HIGH IMPACT')} ▲</div>
      <div style="position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%); font-size: 18px; font-weight: 800; color: #5D7186;">▼ {s.get('y_axis_low', 'LOW IMPACT')}</div>
      <div style="position: absolute; top: 50%; left: 16px; transform: translateY(-50%); font-size: 18px; font-weight: 800; color: #5D7186;">◀ {s.get('x_axis_low', 'LOW')}</div>
      <div style="position: absolute; top: 50%; right: 16px; transform: translateY(-50%); font-size: 18px; font-weight: 800; color: #5D7186;">{s.get('x_axis_high', 'HIGH')} ▶</div>
      <!-- Pills -->
      {''.join(pills_html)}
    </div>
    <!-- Sidebar Area -->
    <div style="flex: 1; display: flex; flex-direction: column; gap: 20px;">
      {''.join(side_cards)}
    </div>
  </div>
  <div class="slide-footer">
    <div>출처: {s.get('source', '전략 우선순위 분석')}</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def generate_eda_chart_html(s: Dict[str, Any], idx: int, total: int, theme: Dict[str, str]) -> str:
    navy = theme.get("primary_navy", "#0F2742")
    coral = theme.get("accent_coral", "#D9481F")
    teal = theme.get("accent_teal", "#14707E")
    
    chart_img = s.get("chart_image", "")
    if chart_img and os.path.exists(chart_img):
        chart_img_url = f"file:///{os.path.abspath(chart_img).replace(os.sep, '/')}"
    else:
        chart_img_url = chart_img
        
    insights_html = "".join([
        f"""<div style="background: #F1F6F9; border-left: 5px solid {coral if i==0 else teal}; border-radius: 10px; padding: 18px 22px; margin-bottom: 16px;">
             <div style="font-size: 16px; font-weight: 800; color: {coral if i==0 else teal}; margin-bottom: 6px;">INSIGHT {i+1:02d}</div>
             <div style="font-size: 21px; font-weight: 600; color: #1E4260; line-height: 1.45;">{ins}</div>
           </div>"""
        for i, ins in enumerate(s.get("insights", [])[:3])
    ])
    
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><style>{COMMON_CSS}</style></head>
<body>
  <div class="slide-header">
    <div class="kicker">{s.get('kicker', 'DATA EXPLORATION')}</div>
    <h1 class="slide-title">{s.get('title', '')}</h1>
  </div>
  <div class="slide-content" style="display: flex; gap: 30px; height: 600px;">
    <!-- Chart Area (Left) -->
    <div class="card" style="flex: 1.6; padding: 24px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: #FFFFFF;">
      <img src="{chart_img_url}" style="max-width: 100%; max-height: 540px; border-radius: 12px; object-fit: contain;">
    </div>
    <!-- Sidebar Findings (Right) -->
    <div style="flex: 1.1; display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <div style="font-size: 24px; font-weight: 800; color: {navy}; margin-bottom: 20px; display: flex; align-items: center;">
          <span style="display: inline-block; width: 10px; height: 24px; background: {coral}; border-radius: 3px; margin-right: 12px;"></span>
          핵심 탐색적 분석(EDA) 시사점
        </div>
        {insights_html}
      </div>
      <div style="background: {navy}; color: #FFFFFF; border-radius: 12px; padding: 18px 24px; font-size: 19px; font-weight: 700;">
        {s.get('takeaway', '')}
      </div>
    </div>
  </div>
  <div class="slide-footer">
    <div>출처: {s.get('source', '공공데이터포털(data.go.kr) 실측 데이터 기반 분석')}</div>
    <div>{idx+1}</div>
  </div>
</body>
</html>"""

def build_deck(config_path: str, output_dir: str, render_png: bool = True, export_files: bool = True):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        
    theme = config.get("theme", {})
    slides = config.get("slides", [])
    deck_title = config.get("title", "Executive Presentation")
    
    html_dir = os.path.join(output_dir, "html")
    png_dir = os.path.join(output_dir, "png")
    os.makedirs(html_dir, exist_ok=True)
    
    print(f"[*] Building {len(slides)} slides into '{output_dir}'...")
    
    for idx, s in enumerate(slides):
        arch = s.get("archetype", "inquiry_3card")
        if arch == "cover":
            html = generate_cover_html(s, idx, len(slides), theme)
        elif arch == "dark_divider":
            html = generate_dark_divider_html(s, idx, len(slides), theme)
        elif arch == "inquiry_3card":
            html = generate_inquiry_3card_html(s, idx, len(slides), theme)
        elif arch == "metric_4card":
            html = generate_metric_4card_html(s, idx, len(slides), theme)
        elif arch == "process_flow":
            html = generate_process_flow_html(s, idx, len(slides), theme)
        elif arch == "quadrant_matrix":
            html = generate_quadrant_matrix_html(s, idx, len(slides), theme)
        elif arch == "eda_chart":
            html = generate_eda_chart_html(s, idx, len(slides), theme)
        else:
            html = generate_inquiry_3card_html(s, idx, len(slides), theme)
            
        file_name = f"slide_{idx+1:02d}_{arch}.html"
        with open(os.path.join(html_dir, file_name), "w", encoding="utf-8") as f:
            f.write(html)
            
    print(f"[+] Successfully generated {len(slides)} HTML slides in '{html_dir}'.")
    
    if render_png:
        print("[*] Rendering 1920x1080 PNG slides using Headless Browser...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        render_script = os.path.join(script_dir, "render_slides.py")
        subprocess.run([sys.executable, render_script, "-i", html_dir, "-o", png_dir], check=True)
        
    if export_files:
        print("[*] Exporting to PDF & 16:9 PPTX...")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        export_script = os.path.join(script_dir, "export_deck.py")
        out_base = os.path.join(output_dir, deck_title.replace(" ", "_"))
        subprocess.run([sys.executable, export_script, "-i", png_dir, "-o", out_base, "--title", deck_title], check=True)
        
    print(f"\n[SUCCESS] Completed entire presentation pipeline for {len(slides)} slides!")

def main():
    parser = argparse.ArgumentParser(description="Build 10~50+ slides from a structured JSON deck spec.")
    parser.add_argument("-c", "--config", required=True, help="Path to deck configuration JSON.")
    parser.add_argument("-o", "--output-dir", default="result/generated_deck", help="Output directory.")
    parser.add_argument("--no-render", action="store_true", help="Skip PNG rendering.")
    parser.add_argument("--no-export", action="store_true", help="Skip PDF/PPTX export.")
    
    args = parser.parse_args()
    build_deck(args.config, args.output_dir, render_png=not args.no_render, export_files=not args.no_export)

if __name__ == "__main__":
    main()
