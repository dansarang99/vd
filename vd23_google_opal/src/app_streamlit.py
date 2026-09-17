#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Streamlit Web App for Google Opal Prompt Builder (vd23)
======================================================
강의 현장 시연 및 실습용 Streamlit 인터랙티브 웹 대시보드입니다.

Run:
  streamlit run src/app_streamlit.py

Author: BJ Jang (dansarang99)
"""

import streamlit as st
from opal_prompt_builder import OpalPromptBuilder
from pathlib import Path

st.set_page_config(
    page_title="Google Opal Prompt Builder (vd23)",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1A73E8;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #5F6368;
        margin-bottom: 1.5rem;
    }
    .prompt-box {
        background-color: #F8F9FA;
        border: 1px solid #DADCE0;
        border-radius: 8px;
        padding: 1.2rem;
        font-family: 'Consolas', monospace;
        font-size: 0.95rem;
        line-height: 1.5;
        white-space: pre-wrap;
    }
    .badge-card {
        background: linear-gradient(135deg, #4285F4 0%, #34A853 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        font-weight: 600;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🚀 Google Opal 자동화 앱 생성 프롬프트 빌더 (vd23)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">장대표(BJ Jang)의 AI 실무 자동화 시리즈 • 구글 오팔(opal.google) 좌측 창 전용 메타 프롬프트 생성기</div>', unsafe_allow_html=True)

# Sidebar Menu
st.sidebar.header("⚙️ 모드 선택")
mode = st.sidebar.radio("작업 방식을 선택하세요:", ["🎯 창업지도사 5대 대표 프리셋", "✏️ 나만의 맞춤형 앱 생성 (Custom)"])

presets = OpalPromptBuilder.PRESETS

if mode == "🎯 창업지도사 5대 대표 프리셋":
    preset_labels = [f"{p['name_kr']} ({p['name']})" for p in presets.values()]
    preset_keys = list(presets.keys())
    
    selected_idx = st.sidebar.selectbox("프리셋 선택:", range(len(preset_keys)), format_func=lambda x: preset_labels[x])
    selected_key = preset_keys[selected_idx]
    preset_data = presets[selected_key]

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.subheader("📋 프리셋 상세 사양")
        st.markdown(f"**앱 명칭**: {preset_data['name_kr']}")
        st.markdown(f"**영문 식별자**: `{preset_data['name']}`")
        st.markdown(f"**전문 페르소나**: `{preset_data['persona']}`")
        st.info(f"💡 **목표 및 기대효과**:\n{preset_data['goal']}")

        st.markdown("#### 📥 사용자 입력 필드 (UI)")
        for inp in preset_data["inputs"]:
            opt_str = f" *(옵션: {', '.join(inp['options'])})*" if "options" in inp else ""
            st.markdown(f"- **{inp['name']}** (`{inp['type']}`): {inp.get('desc', '')}{opt_str}")

        st.markdown("#### 🔄 노드 파이프라인")
        for step in preset_data["pipeline"]:
            st.markdown(f"- {step}")

    with col2:
        st.subheader("✨ Google Opal 좌측 창 복사용 프롬프트")
        st.caption("아래 텍스트를 복사하여 https://opal.google 의 좌측 입력창에 그대로 붙여넣으세요.")
        
        prompt_content = OpalPromptBuilder.generate_preset_prompt(selected_key)
        
        st.code(prompt_content, language="text", line_numbers=False)
        
        # 다운로드 버튼
        st.download_button(
            label="💾 프롬프트 텍스트 파일(.txt) 다운로드",
            data=prompt_content,
            file_name=f"opal_prompt_{selected_key}.txt",
            mime="text/plain"
        )

else:
    st.subheader("✏️ 나만의 자동화 앱 생성 (Custom Mode)")
    
    with st.form("custom_app_form"):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            app_name = st.text_input("앱 이름 (영문/한글)", value="AI Startup Patent Analyzer")
            target_user = st.text_input("타깃 사용자", value="예비창업자 및 기술기반 스타트업")
            persona = st.text_input("전문가 페르소나", value="Senior Patent Attorney & Tech Commercialization Specialist")
        with col_c2:
            goal = st.text_area("앱의 핵심 목적 및 기대효과", value="창업자의 기술 아이디어를 입력받아 관련 선행 특허 검색 키워드를 도출하고, 특허 등록 가능성 및 회피 설계 방안을 표로 정리합니다.", height=120)
            guardrails = st.text_input("안전 가이드라인 / 제약조건", value="법적 책임 면책 고지를 포함하고, 구체적인 IPC 분류 및 출원 전략을 단계별로 제시할 것.")

        st.markdown("##### 📥 입력 폼 설정 (최대 3개)")
        i_col1, i_col2, i_col3 = st.columns(3)
        with i_col1:
            inp1_name = st.text_input("입력 1 이름", value="Invention Idea / Technical Abstract")
            inp1_type = st.selectbox("입력 1 유형", ["Long Text Area", "Short Text", "File Upload"], index=0)
        with i_col2:
            inp2_name = st.text_input("입력 2 이름", value="Core Technical Keywords")
            inp2_type = st.selectbox("입력 2 유형", ["Short Text", "Single Select Dropdown"], index=0)
        with i_col3:
            inp3_name = st.text_input("입력 3 이름", value="Target Commercial Market")
            inp3_type = st.selectbox("입력 3 유형", ["Short Text", "Single Select Dropdown"], index=0)

        submitted = st.form_submit_button("🚀 Opal 최적화 프롬프트 생성하기")

    if submitted or app_name:
        custom_inputs = [
            {"name": inp1_name, "type": inp1_type, "desc": "발명의 명칭 및 핵심 기술 요약"},
            {"name": inp2_name, "type": inp2_type, "desc": "주요 핵심 키워드"},
            {"name": inp3_name, "type": inp3_type, "desc": "목표 상용화 시장 및 산업 분야"}
        ]
        
        custom_prompt = OpalPromptBuilder.generate_custom_prompt(
            app_name=app_name,
            goal=goal,
            target_user=target_user,
            persona=persona,
            inputs=custom_inputs,
            guardrails=guardrails
        )
        
        st.subheader("✨ 완성된 Google Opal 프롬프트")
        st.code(custom_prompt, language="text")
        
        st.download_button(
            label="💾 프롬프트 파일 저장",
            data=custom_prompt,
            file_name="opal_custom_prompt.txt",
            mime="text/plain"
        )

st.markdown("---")
st.markdown("""
### 💡 Google Opal(opal.google) 강의 실습 가이드
1. **Opal 접속**: 브라우저에서 `https://opal.google` 에 접속하고 구글 계정으로 로그인합니다.
2. **좌측 입력창 붙여넣기**: 위에서 복사한 C-I-P-O-E 프롬프트를 좌측 **[Describe your workflow...]** 창에 그대로 붙여넣고 `Enter`를 누릅니다.
3. **노드 그래프 확인**: Opal이 자동으로 **Inputs 폼 노드 ➡️ 검색 노드 ➡️ Gemini 1.5 Pro 추론 노드 ➡️ 마크다운 변환 노드 ➡️ 결과 대시보드 노드**를 캔버스에 그리는 것을 확인합니다.
4. **미세 조정**: 각 노드를 클릭하여 우측 인스펙터(Inspector)에서 프롬프트를 다듬거나 테스트 실행(Run)을 눌러 실시간 시연을 진행합니다.
""")
