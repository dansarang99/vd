#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interactive CLI for Google Opal Prompt Builder (vd23)
=====================================================
터미널에서 대화형으로 Opal 자동화 앱 생성 프롬프트를 만들고
즉시 파일로 저장하거나 클립보드에 복사할 수 있는 CLI 도구입니다.

Author: BJ Jang (dansarang99)
"""

import sys
import os
from pathlib import Path
from opal_prompt_builder import OpalPromptBuilder

try:
    import pyperclip
    HAS_CLIP = True
except ImportError:
    HAS_CLIP = False

def print_banner():
    print("=" * 72)
    print(" 🚀 [vd23] Google Opal 자동화 앱 생성 프롬프트 빌더 CLI")
    print("    구글 오팔(opal.google) 좌측 창 전용 메타 프롬프트 생성기")
    print("    장대표(BJ Jang)의 AI 실무 자동화 시리즈")
    print("=" * 72)

def main():
    print_banner()
    
    presets = OpalPromptBuilder.PRESETS
    keys = list(presets.keys())

    print("\n[메뉴 선택]")
    print(" 1. 창업지도사 5대 프리셋에서 선택하기")
    print(" 2. 나만의 새로운 자동화 앱 아이디어 직접 입력하기")
    print(" 0. 종료")

    choice = input("\n번호를 입력하세요 (기본값: 1): ").strip() or "1"

    if choice == "0":
        print("프로그램을 종료합니다.")
        return

    prompt_text = ""
    app_title = ""

    if choice == "1":
        print("\n--- [5대 프리셋 목록] ---")
        for i, k in enumerate(keys, 1):
            p = presets[k]
            print(f" {i}. [{p['name_kr']}] - {p['name']}")
        
        idx_input = input(f"\n원하는 프리셋 번호를 선택하세요 (1~{len(keys)}, 기본값: 1): ").strip() or "1"
        try:
            selected_idx = int(idx_input) - 1
            if 0 <= selected_idx < len(keys):
                selected_key = keys[selected_idx]
                prompt_text = OpalPromptBuilder.generate_preset_prompt(selected_key)
                app_title = presets[selected_key]["name"]
            else:
                print("잘못된 번호입니다. 기본 1번으로 진행합니다.")
                prompt_text = OpalPromptBuilder.generate_preset_prompt(keys[0])
                app_title = presets[keys[0]]["name"]
        except ValueError:
            prompt_text = OpalPromptBuilder.generate_preset_prompt(keys[0])
            app_title = presets[keys[0]]["name"]

    elif choice == "2":
        print("\n--- [사용자 맞춤형 앱 아이디어 입력] ---")
        app_name = input("1. 만들고 싶은 앱 이름 (예: AI 특허 검색 요약기): ").strip() or "AI Smart Assistant"
        goal = input("2. 앱의 핵심 목적/해결 과제: ").strip() or "사용자 입력을 바탕으로 최적의 인사이트를 제공합니다."
        target = input("3. 타깃 사용자 (기본: 창업자 및 실무자): ").strip() or "창업자 및 실무자"
        
        prompt_text = OpalPromptBuilder.generate_custom_prompt(
            app_name=app_name,
            goal=goal,
            target_user=target
        )
        app_title = app_name

    print("\n" + "=" * 72)
    print(f" ✨ [Google Opal 좌측 창 복사용 프롬프트 완성: {app_title}]")
    print("=" * 72)
    print(prompt_text)
    print("=" * 72)

    # 결과 디렉토리 저장
    result_dir = Path(__file__).resolve().parent.parent / "result"
    result_dir.mkdir(parents=True, exist_ok=True)
    
    safe_filename = "".join(c for c in app_title if c.isalnum() or c in (' ', '_', '-')).rstrip()
    safe_filename = safe_filename.replace(" ", "_").lower()
    out_path = result_dir / f"opal_prompt_{safe_filename}.txt"
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(prompt_text)
    print(f"\n💾 파일 저장 완료: {out_path}")

    # 클립보드 복사 시도
    if HAS_CLIP:
        try:
            pyperclip.copy(prompt_text)
            print("📋 클립보드에 자동 복사되었습니다! Opal(opal.google) 좌측 창에 바로 붙여넣기(Ctrl+V) 하세요.")
        except Exception:
            print("💡 (안내) 클립보드 복사를 지원하지 않는 환경입니다. 위 프롬프트를 직접 드래그하여 복사하세요.")
    else:
        print("💡 위 텍스트를 복사하여 Google Opal(https://opal.google) 좌측 입력창에 붙여넣으세요.")

    print("\n🎉 완료되었습니다!")

if __name__ == "__main__":
    main()
