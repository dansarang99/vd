#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Google Opal Prompt Builder Engine (vd23)
========================================
이 모듈은 사용자의 비즈니스 자동화 요구사항을 입력받아
Google Opal(opal.google) 좌측 프롬프트 입력창에 최적화된
C-I-P-O-E 5대 아키텍처 규격의 메타 프롬프트를 생성합니다.

Author: BJ Jang (dansarang99)
License: MIT
"""

from typing import List, Dict, Optional
import json

class OpalPromptBuilder:
    """
    Google Opal 노드 컴파일러 최적화 프롬프트 생성기
    """

    PRESETS = {
        "lean_canvas": {
            "name": "Lean Canvas Auto-Generator",
            "name_kr": "원클릭 스타트업 린 캔버스 자동 완성기",
            "persona": "Senior Startup Accelerator & Venture Builder",
            "goal": "예비 창업자가 사업 아이템과 타깃 고객을 입력하면 9대 린 캔버스 항목(문제, 고객군, 가치제안, 솔루션, 채널, 수익모델, 비용구조, 핵심지표, 경쟁우위)을 심층 분석하여 구조화된 마크다운 표와 30일 실행 로드맵으로 출력합니다.",
            "inputs": [
                {"name": "Business Item / Service Name", "type": "Short Text", "desc": "창업 아이템 명칭 및 한 줄 소개"},
                {"name": "Detailed Description", "type": "Long Text Area", "desc": "해결하려는 문제 및 핵심 기능 상세 설명"},
                {"name": "Primary Target Customer", "type": "Short Text", "desc": "1차 목표 고객 페르소나 (예: 2030 직장인, 소상공인 등)"},
                {"name": "Revenue Model", "type": "Single Select Dropdown", "options": ["B2B SaaS / 정기구독", "B2C 커머스 / 플랫폼 수수료", "중개 매칭 플랫폼", "광고 및 데이터 수익", "기타 비즈니스 모델"]}
            ],
            "pipeline": [
                "Node 1 (Input Validation): Inspect input completeness. Ensure business item and target customer are defined clearly.",
                "Node 2 (Market Category Classification): Automatically classify market industry and identify typical industry benchmark margins.",
                "Node 3 (Core AI Engine - Gemini 1.5 Pro): Act as an elite accelerator director. Systematically evaluate: 1. Problem & Existing Alternatives, 2. Early Adopter Profile, 3. High-Concept Pitch & Unique Value Proposition, 4. Solution Set, 5. Top Acquisition Channels, 6. Revenue Streams & Pricing Tiers, 7. Fixed/Variable Cost Drivers, 8. North Star Metric & Key KPIs, 9. Defensible Unfair Advantage (Moat).",
                "Node 4 (Synthesis & Formatting): Construct a clean 3x3 Markdown Lean Canvas Table with bulleted strategic takeaways.",
                "Node 5 (Roadmap & Action Items): Produce a pragmatic 4-week MVP validation schedule (Problem Interview -> Prototype -> Smoke Test -> Customer Commitment)."
            ],
            "output_ui": [
                "Header Summary: Executive Pitch Deck Summary Card with Market Readiness Score (1-100)",
                "Main Body: Full 9-Block Markdown Lean Canvas Grid with deep actionable bullets",
                "Validation Roadmap: 30-day step-by-step experiment action checklist with success criteria"
            ],
            "guardrails": "Do not provide generic business advice; tailor each of the 9 blocks specifically to the user's defined target customer and industry dynamics."
        },
        "psst_grant": {
            "name": "PSST Government Grant Proposal Builder",
            "name_kr": "정부지원사업 PSST 표준 사업계획서 1차 초안 빌더",
            "persona": "Government Startup Grant Lead Evaluator & AX Consultant",
            "goal": "중소벤처기업부 및 창업진흥원 예비/초기창업패키지 표준 양식인 PSST(문제인식, 실현가능성, 성장전략, 팀구성) 프레임워크에 맞춰 고득점을 유도하는 표준 사업계획서 1차 초안을 작성합니다.",
            "inputs": [
                {"name": "Startup Item Title", "type": "Short Text", "desc": "지원사업 과제명 (정부과제 표준 명명법 권장)"},
                {"name": "Current Problem & Pain Points", "type": "Long Text Area", "desc": "기존 시장의 불편함과 개발 필요성"},
                {"name": "Our Solution & Core Tech", "type": "Long Text Area", "desc": "독창적 해결방안 및 차별화된 핵심 기술/서비스"},
                {"name": "Target Grant Program", "type": "Single Select Dropdown", "options": ["예비창업패키지", "초기창업패키지", "청년창업사관학교", "디딤돌 R&D 지원사업", "창업도약패키지"]}
            ],
            "pipeline": [
                "Node 1 (Compliance Check): Verify mandatory PSST elements and match evaluation criteria of the chosen grant program.",
                "Node 2 (Search & Policy Context): Reference latest governmental technology roadmap keywords (AI, Digital Twin, ESG, DX).",
                "Node 3 (Core AI Logic - Gemini 1.5 Pro): Write in formal official government proposal Korean tone (개조식 및 논리적 서술형 혼합):\n  - 1. 문제인식 (Problem): 배경, 필요성, 타깃 시장 규모 (TAM-SAM-SOM)\n  - 2. 실현가능성 (Solution): 개발 추진 내용, 차별성, 시제품 제작 계획\n  - 3. 성장전략 (Scale-up): 비즈니스 모델, 판로 개척, 정부지원금 소요 예산표 (비목별 편성)\n  - 4. 팀 구성 (Team): 대표자 역량, 팀원 시너지, 기술 파트너십",
                "Node 4 (Evaluator Scoring Checklist): Generate a 5-item self-audit evaluation checklist simulating an actual screening judge."
            ],
            "output_ui": [
                "Summary Header: 과제명, 주관기관, 예상 평가 점수 및 핵심 강점 요약 카드",
                "PSST Full Proposal: 4대 챕터별 완벽한 본문 텍스트 (개조식 기호: ■, ○, - 활용)",
                "Budget Allocation Table: 지원금 예산 비목별(재료비, 외주용역비, 마케팅비, 인건비) 권장 비율표"
            ],
            "guardrails": "Always maintain formal Korean government proposal terminology (e.g., '기대효과', '사업화 로드맵', '일자리 창출 계획')."
        },
        "competitor_battlecard": {
            "name": "Competitive Intelligence & Battlecard Analyzer",
            "name_kr": "실시간 경쟁사 비교 분석 및 영업용 배틀카드 빌더",
            "persona": "Strategic Corporate Intelligence & Product Marketing Lead",
            "goal": "자사 제품과 2~3개의 경쟁사를 입력받아 실시간 구글 검색을 통해 가격, 주요 기능, 리뷰, 포지셔닝 맵을 비교하고 영업용 킬러 차별화 포인트를 도출합니다.",
            "inputs": [
                {"name": "Our Product / Service", "type": "Short Text", "desc": "자사 제품명 및 핵심 특징"},
                {"name": "Competitor 1 Name or URL", "type": "Short Text", "desc": "경쟁사 A 이름 또는 웹사이트 링크"},
                {"name": "Competitor 2 Name or URL", "type": "Short Text", "desc": "경쟁사 B 이름 또는 웹사이트 링크"},
                {"name": "Industry Sector", "type": "Short Text", "desc": "산업군 / 도메인"}
            ],
            "pipeline": [
                "Node 1 (Search Tool Trigger): Perform Google Search on Competitor 1 and Competitor 2 to fetch official pricing, key features, and user testimonials.",
                "Node 2 (Feature Extraction): Extract structured feature comparison metrics (Pricing tiers, User experience, Integration, Support).",
                "Node 3 (Gemini 1.5 Pro Matrix Analysis): Build a 2x2 Positioning Matrix (e.g., Ease of Use vs Customizability) and Conduct SWOT Comparison.",
                "Node 4 (Sales Battlecard Synthesis): Output actionable 'How to Win Against Competitor X' talk tracks and objection handling scripts."
            ],
            "output_ui": [
                "Header: Competitor Threat Level Meter and Quick Overview",
                "Comparison Table: Side-by-side Feature Matrix (Our Product vs Competitors)",
                "Sales Talk Tracks: 3 Killer Value Propositions and 5 Objection-Handling Scripts for Sales Meetings"
            ],
            "guardrails": "Ensure fact-based comparisons; cite searched data or clearly denote inferred strategic assessments."
        },
        "omnichannel_content": {
            "name": "Omni-Channel Content Factory for Startups",
            "name_kr": "1초 완성 옴니채널 SNS 마케팅 콘텐츠 팩토리",
            "persona": "Viral Growth Hacker & Senior Content Strategist",
            "goal": "신제품 런칭, 프로모션, 또는 핵심 아티클 한 편을 입력받아 인스타그램 카드뉴스, 네이버 블로그 SEO 글, 링크드인 인사이트 포스트, 숏폼 비디오 대본을 동시 다발적으로 생성합니다.",
            "inputs": [
                {"name": "Product Announcement / Topic", "type": "Long Text Area", "desc": "공지할 신제품 내용, 이벤트, 또는 브랜드 스토리"},
                {"name": "Brand Tone & Voice", "type": "Single Select Dropdown", "options": ["전문적이고 신뢰감 있는 (Professional)", "트렌디하고 친근한 MZ 스타일 (Witty & Friendly)", "영감을 주는 감성적인 (Inspirational & Emotional)", "정보 전달 중심의 교육적 (Informative & Educational)"]},
                {"name": "Call to Action (CTA)", "type": "Short Text", "desc": "유도할 행동 (예: 사전예약 신청, 무료 상담 링크, 회원가입)"}
            ],
            "pipeline": [
                "Node 1 (Core Message Distillation): Identify the top 1 'Hook' and 3 core value propositions.",
                "Node 2 (Multi-Channel Routing): Split generation into 4 dedicated specialized channels in parallel.",
                "Node 3 (Channel-Specific Crafting):\n  - Channel A (Instagram Card News): 8-slide structure (Hook Cover -> 5 Content Slides -> Summary -> CTA slide) with visual prompt tags.\n  - Channel B (Naver Blog): SEO Title, 1500-word conversational article with bold headings, FAQ section, and 20 hashtag keywords.\n  - Channel C (LinkedIn): Thought leadership narrative, lesson learned, and community discussion question.\n  - Channel D (Short-form Video 60s): Scene-by-scene script with visual cues, TTS voiceover, and on-screen caption texts.",
                "Node 4 (Dashboard Rendering): Present all channels in organized, copy-ready blocks."
            ],
            "output_ui": [
                "Multi-Tab View: Tab 1: Instagram Slides / Tab 2: Blog Article / Tab 3: LinkedIn Post / Tab 4: 60s Reel Script",
                "One-Click Copy Blocks: Pre-formatted text ready for direct publishing"
            ],
            "guardrails": "Adopt the chosen Tone & Voice consistently across all channels while respecting each platform's distinct native format."
        },
        "vc_stress_tester": {
            "name": "VC Pitching Stress-Tester & Question Simulator",
            "name_kr": "VC 투자심사역 압박면접 Q&A 시뮬레이터",
            "persona": "Tough Tier-1 Venture Capitalist Principal",
            "goal": "창업자의 사업 아이템 및 IR 요약문을 분석하여 실제 투자 심사위원회에서 심사역들이 던질 가장 날카롭고 공격적인 10대 질문과 모범 방어 답변 전략을 생성합니다.",
            "inputs": [
                {"name": "IR Executive Summary", "type": "Long Text Area", "desc": "사업 개요, 시장 기회, 기술력, 트랙션(매출/유저) 요약"},
                {"name": "Target Investment Round", "type": "Single Select Dropdown", "options": ["Seed / 엔젤투자", "Pre-Series A", "Series A", "Series B 이상"]},
                {"name": "Current Biggest Concern", "type": "Short Text", "desc": "창업자가 생각하는 현재 사업의 가장 취약한 점 (선택 사항)"}
            ],
            "pipeline": [
                "Node 1 (Vulnerability Scan): Detect red flags in Unit Economics (CAC/LTV), Market Size ceiling, Moat credibility, and Team completeness.",
                "Node 2 (VC Persona Engine): Formulate 10 ruthless investor questions categorized into:\n  - Category 1: Market & Competition (왜 지금인가? 빅테크가 따라하면?)\n  - Category 2: Unit Economics & Traction (고객 획득 비용의 지속 가능성은?)\n  - Category 3: Tech Moat & IP (진짜 기술적 진입장벽이 있는가?)\n  - Category 4: Exit & Milestone (이번 라운드 투자금으로 달성할 구체적 숫자는?)",
                "Node 3 (Defensive Strategy Formulation): Provide the golden response structure (Acknowledge -> Concrete Data/Metric Proof -> Strategic Hedge) for each question."
            ],
            "output_ui": [
                "Investor Risk Scorecard: High/Medium/Low risk matrix across 4 domains",
                "10 Sharp VC Questions & Recommended Answers: Detailed battle guide with data backup suggestions",
                "Key Metrics To Prepare: Numerical proof points required before the meeting"
            ],
            "guardrails": "Act as a constructive yet rigorously skeptical investor. Challenge unsupported assumptions."
        }
    }

    @classmethod
    def generate_preset_prompt(cls, preset_key: str) -> str:
        """미리 정의된 프리셋 키로 Opal 프롬프트 텍스트를 반환합니다."""
        preset = cls.PRESETS.get(preset_key)
        if not preset:
            raise ValueError(f"Unknown preset key: {preset_key}. Available: {list(cls.PRESETS.keys())}")
        
        return cls._assemble_prompt(
            app_name=preset["name"],
            persona=preset["persona"],
            goal=preset["goal"],
            inputs=preset["inputs"],
            pipeline=preset["pipeline"],
            output_ui=preset["output_ui"],
            guardrails=preset["guardrails"]
        )

    @classmethod
    def generate_custom_prompt(
        cls,
        app_name: str,
        goal: str,
        target_user: str = "Startups & AX Consultants",
        persona: Optional[str] = None,
        inputs: Optional[List[Dict[str, str]]] = None,
        pipeline: Optional[List[str]] = None,
        output_ui: Optional[List[str]] = None,
        guardrails: Optional[str] = None
    ) -> str:
        """사용자 정의 파라미터로 Opal 최적화 프롬프트를 조립합니다."""
        
        assigned_persona = persona or f"Expert AI Consultant for {target_user}"
        
        assigned_inputs = inputs or [
            {"name": "Core Inquiry / Topic", "type": "Text Area", "desc": "분석 또는 처리할 기본 입력 정보"},
            {"name": "Specific Constraints or Style", "type": "Short Text", "desc": "요청 사항 및 제약 조건"}
        ]
        
        assigned_pipeline = pipeline or [
            "Node 1 (Input Validation): Parse and validate all required user input fields.",
            "Node 2 (Context & Search): Gather necessary background benchmarks and context.",
            f"Node 3 (Core AI Logic - Gemini 1.5 Pro): Act as {assigned_persona}. Execute in-depth step-by-step reasoning.",
            "Node 4 (Data Structuring): Format the raw response into a structured Markdown table, summary badges, and prioritized lists.",
            "Node 5 (Presentation): Render the output cleanly in an interactive dashboard card view."
        ]
        
        assigned_output_ui = output_ui or [
            "Executive Summary Header with Key Highlights",
            "Structured Analysis Section with Comparative Tables",
            "Actionable Next Steps and Implementation Roadmap"
        ]
        
        assigned_guardrails = guardrails or "Ensure outputs are highly actionable, precise, and professional."

        return cls._assemble_prompt(
            app_name=app_name,
            persona=assigned_persona,
            goal=goal,
            inputs=assigned_inputs,
            pipeline=assigned_pipeline,
            output_ui=assigned_output_ui,
            guardrails=assigned_guardrails
        )

    @staticmethod
    def _assemble_prompt(
        app_name: str,
        persona: str,
        goal: str,
        inputs: List[Dict[str, str]],
        pipeline: List[str],
        output_ui: List[str],
        guardrails: str
    ) -> str:
        """C-I-P-O-E 규격에 맞게 최종 문자열을 조립합니다."""
        
        input_lines = []
        for idx, item in enumerate(inputs, start=1):
            options_text = ""
            if "options" in item:
                options_text = f" [Options: {', '.join(item['options'])}]"
            input_lines.append(f"{idx}. {item['name']}: (Type: {item.get('type', 'Text')}) - {item.get('desc', '')}{options_text}")
        inputs_str = "\n".join(input_lines)

        pipeline_lines = []
        for step in pipeline:
            pipeline_lines.append(f"- {step}")
        pipeline_str = "\n".join(pipeline_lines)

        ui_lines = []
        for elem in output_ui:
            ui_lines.append(f"- {elem}")
        ui_str = "\n".join(ui_lines)

        prompt_body = f"""Create an automated multi-step workflow app named "{app_name}".

[App Goal & Persona]
Role: Act as an expert {persona}.
Goal: {goal}

[User Input Elements]
{inputs_str}

[Workflow Pipeline Nodes]
{pipeline_str}

[Output UI & Format]
{ui_str}

[Guardrails & Logic Rules]
- {guardrails}
- If any required input field is blank, politely request the user to provide it with 2 sample examples before executing downstream nodes.
- Deliver results with rich Markdown typography, bold emphasis, and structured clarity.
"""
        return prompt_body.strip()


if __name__ == "__main__":
    builder = OpalPromptBuilder()
    print("=== [Google Opal Sample Prompt: Lean Canvas] ===")
    sample = builder.generate_preset_prompt("lean_canvas")
    print(sample)
