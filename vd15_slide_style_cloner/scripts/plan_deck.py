#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deck Storyline Planner (/plan & /grill-me Engine)
Generates a structured deck_spec.json skeleton based on flexible expansion ratios (1:1, 1:1.5, 1:2, 1:3, 1:5)
and seamlessly incorporates EDA chart visualizers from public data.
"""

import sys
import os
import json
import argparse
from typing import Dict, Any, List

def create_deck_plan(
    topic: str,
    ratio: float = 1.0,
    base_slide_count: int = 10,
    theme: Dict[str, str] = None,
    eda_data: Dict[str, Any] = None,
    author: str = "Executive Strategy Team"
) -> Dict[str, Any]:
    target_count = max(5, int(round(base_slide_count * ratio)))
    
    default_theme = {
        "primary_navy": "#0F2742",
        "secondary_slate": "#1E4260",
        "accent_coral": "#D9481F",
        "accent_teal": "#14707E",
        "accent_amber": "#B07D18",
        "canvas_ice": "#DCEAF6"
    }
    active_theme = {**default_theme, **(theme or {})}
    
    slides: List[Dict[str, Any]] = []
    
    # 1. Slide 1: Cover
    slides.append({
        "archetype": "cover",
        "kicker": "EXECUTIVE STRATEGY",
        "title": topic,
        "subtitle": f"AI & Digital Transformation Era: Strategic Blueprint ({target_count} Slides)",
        "author": f"{author} · 2026"
    })
    
    # 2. Slide 2: Opening Inquiry
    slides.append({
        "archetype": "inquiry_3card",
        "kicker": "OPENING",
        "title": "Three Foundational Strategic Inquiries",
        "cards": [
            {"badge": "Q1", "title": "Market Urgency", "headline": "Where is the immediate paradigm inflection?", "bullets": ["Ecosystem shifts & competitive urgency", "Accelerating transformation cycle"]},
            {"badge": "Q2", "title": "Structural Gap", "headline": "What internal bottlenecks inhibit scaling?", "bullets": ["Data silos & analytical latency", "Resource allocation frictions"]},
            {"badge": "Q3", "title": "Executive Mandate", "headline": "What must leadership decide this quarter?", "bullets": ["Institutional governance framework", "Priority infrastructure investments"]}
        ],
        "takeaway": "Sustainable competitive advantage requires transitioning from reactive posture to deliberate institutional design."
    })
    
    # 3. If EDA data exists, inject dedicated EDA Chart Slide
    if eda_data and eda_data.get("chart_image"):
        slides.append({
            "archetype": "eda_chart",
            "kicker": "EMPIRICAL EDA",
            "title": f"공공데이터 실측 탐색적 데이터 분석(EDA) — {eda_data.get('chart_title', '수급 및 추세 지표')}",
            "chart_image": eda_data.get("chart_image"),
            "insights": eda_data.get("key_insights", [
                "최근 분기 지표 상승 반등으로 시장의 관망세가 개선 국면으로 진입함.",
                "핵심 세부 지표 간 변동성 완화로 중장기 전략 실행의 신뢰 구간 확보.",
                "공공데이터포털 실측 데이터 기반의 객관적 의사결정 프레임워크 수립."
            ]),
            "takeaway": "객관적 실측 데이터 분석 결과, 과거 관행에서 벗어나 데이터 기반 거버넌스로의 전환이 시급함.",
            "source": f"공공데이터포털(data.go.kr) / {eda_data.get('data_source', '공공통계')}"
        })
        
    part_names = [
        ("PART 1", "Market Paradigm & Empirical Reality", "Current Landscape & Bottlenecks"),
        ("PART 2", "Target Architecture & Core Strategy", "Modern Technical & Operational Pillars"),
        ("PART 3", "Governance, Risk & Organization", "Securing Assets & Mitigating Vulnerabilities"),
        ("PART 4", "Execution Roadmap & Leadership Mandates", "18-Month Action Plan & Immediate Decisions")
    ]
    
    remaining_slots = target_count - len(slides)
    slots_per_part = max(2, remaining_slots // len(part_names)) if remaining_slots > 0 else 2
    
    for p_idx, (p_kicker, p_title, p_sub) in enumerate(part_names):
        if len(slides) >= target_count:
            break
            
        slides.append({
            "archetype": "dark_divider",
            "kicker": p_kicker,
            "title": p_title,
            "subtitle": p_sub,
            "bullets": [
                f"Pillar {p_idx+1}.1: Critical strategic context and foundational assumptions",
                f"Pillar {p_idx+1}.2: Analytical decomposition and empirical performance metrics",
                f"Pillar {p_idx+1}.3: Actionable frameworks for decisive C-Suite execution"
            ]
        })
        
        part_slide_types = ["metric_4card", "inquiry_3card", "process_flow", "quadrant_matrix"]
        current_part_count = min(slots_per_part - 1, target_count - len(slides))
        
        for s_idx in range(current_part_count):
            stype = part_slide_types[s_idx % len(part_slide_types)]
            if stype == "metric_4card":
                slides.append({
                    "archetype": "metric_4card",
                    "kicker": f"{p_kicker} · DATA REALITY",
                    "title": f"Empirical Metrics & Reality Check — {p_title}",
                    "cards": [
                        {"metric": "84%", "title": "Primary Metric", "desc": "Key performance benchmark", "bullets": ["Verified institutional data"]},
                        {"metric": "3.8x", "title": "Velocity Gain", "desc": "Operational acceleration", "bullets": ["Optimized cycle times"]},
                        {"metric": "45%", "title": "Cost Efficiency", "desc": "Waste elimination target", "bullets": ["FinOps resource recovery"]},
                        {"metric": "92%", "title": "Strategic Focus", "desc": "Core stakeholder priority", "bullets": ["Executive alignment rate"]}
                    ],
                    "takeaway": "Measurable empirical indicators substantiate the imperative for strategic modernization."
                })
            elif stype == "inquiry_3card":
                slides.append({
                    "archetype": "inquiry_3card",
                    "kicker": f"{p_kicker} · STRATEGIC PILLARS",
                    "title": f"Core Structural Pillars of {p_title}",
                    "cards": [
                        {"badge": "01", "title": "Foundation", "headline": "Modernizing core capabilities", "bullets": ["Architectural modularity", "Single source of truth"]},
                        {"badge": "02", "title": "Optimization", "headline": "Streamlining workflow friction", "bullets": ["Automated policy guardrails", "Frictionless deployment"]},
                        {"badge": "03", "title": "Governance", "headline": "Sustaining quality and trust", "bullets": ["Continuous telemetry", "Compliance enforcement"]}
                    ],
                    "takeaway": "Success requires balanced co-evolution across technology, people, and operating guardrails."
                })
            elif stype == "process_flow":
                slides.append({
                    "archetype": "process_flow",
                    "kicker": f"{p_kicker} · PIPELINE & FLOW",
                    "title": f"End-to-End Operational Pipeline — {p_title}",
                    "steps": [
                        {"title": "01. Intake", "desc": "Automated ingestion", "bullets": ["Data cataloging", "Validation"]},
                        {"title": "02. Processing", "desc": "Standardization", "bullets": ["Cleaning", "Transformation"]},
                        {"title": "03. Synthesis", "desc": "Context integration", "bullets": ["Semantic modeling"], "highlight": True},
                        {"title": "04. Delivery", "desc": "Secure serving", "bullets": ["Access control", "API endpoints"]},
                        {"title": "05. Audit", "desc": "Feedback loop", "bullets": ["Continuous monitoring"]}
                    ],
                    "takeaway": "Standardized pipeline stages eliminate single points of failure and enhance institutional agility."
                })
            elif stype == "quadrant_matrix":
                slides.append({
                    "archetype": "quadrant_matrix",
                    "kicker": f"{p_kicker} · DECISION MATRIX",
                    "title": f"Strategic Trade-Off & Prioritization — {p_title}",
                    "y_axis_high": "HIGH IMPACT", "y_axis_low": "LOW IMPACT",
                    "x_axis_low": "LOW RISK", "x_axis_high": "HIGH RISK",
                    "matrix_items": [
                        {"text": "Foundation Guardrails", "x": 120, "y": 90},
                        {"text": "Strategic Transformation Core", "x": 580, "y": 80, "alert": True},
                        {"text": "Iterative Improvements", "x": 140, "y": 380},
                        {"text": "Experimental Bets", "x": 600, "y": 390}
                    ],
                    "sidebar_cards": [
                        {"tag": "PRIORITY RULE", "text": "Aggressively fund High-Impact initiatives while systematically de-risking dependencies.", "dark": True},
                        {"tag": "ORGANIZATIONAL HEALTH", "text": "Institutional readiness is the primary differentiator between successful adoption and stalled pilot programs."}
                    ]
                })

    while len(slides) < target_count:
        idx = len(slides) + 1
        slides.append({
            "archetype": "inquiry_3card",
            "kicker": "EXECUTIVE MANDATE",
            "title": f"Leadership Execution Checklist (Item #{idx})",
            "cards": [
                {"badge": "A", "title": "Resource Allocation", "headline": "Immediate capital & talent assignment", "bullets": ["Dedicated agile strike team", "Quarterly milestone funding"]},
                {"badge": "B", "title": "Policy Institutionalization", "headline": "Clear authority and decision boundaries", "bullets": ["Steering committee mandate", "Operational KPI definitions"]},
                {"badge": "C", "title": "Review Cadence", "headline": "Continuous board-level review", "bullets": ["Monthly governance check", "Risk telemetry tracking"]}
            ],
            "takeaway": "Decisive executive sponsorship is the single most critical factor in transformation velocity."
        })

    return {
        "title": topic,
        "ratio": f"1:{ratio}",
        "total_slides": len(slides[:target_count]),
        "theme": active_theme,
        "slides": slides[:target_count]
    }

def main():
    parser = argparse.ArgumentParser(description="Generate structured slide plan (deck_spec.json) supporting decimal ratios and EDA data.")
    parser.add_argument("-t", "--topic", required=True, help="Presentation topic.")
    parser.add_argument("-r", "--ratio", type=float, default=1.0, help="Expansion ratio: e.g. 1.0 (1:1), 1.5 (1:1.5), 2.0 (1:2), 3.0 (1:3), etc.")
    parser.add_argument("-b", "--base-count", type=int, default=10, help="Base reference slide count (default: 10).")
    parser.add_argument("-o", "--output", default="deck_spec.json", help="Path to save generated deck_spec.json.")
    parser.add_argument("-e", "--eda-summary", default=None, help="Optional path to eda_summary.json generated by eda_analyzer.py.")
    parser.add_argument("--author", default="Executive Strategy Team", help="Author/Organization metadata.")

    args = parser.parse_args()

    eda_data = None
    if args.eda_summary and os.path.exists(args.eda_summary):
        with open(args.eda_summary, "r", encoding="utf-8") as f:
            eda_data = json.load(f)

    plan = create_deck_plan(
        topic=args.topic,
        ratio=args.ratio,
        base_slide_count=args.base_count,
        eda_data=eda_data,
        author=args.author
    )

    out_dir = os.path.dirname(args.output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

    print(f"[+] Successfully generated Deck Plan ({plan['total_slides']} slides, Ratio 1:{args.ratio}): {args.output}")

if __name__ == "__main__":
    main()
