#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[자막 내보내기 유틸리티]
마크다운 형태의 5대 대본 파일에서 'Track 4 [자막용 대본]'을 추출하여
표준 SRT 자막 파일(.srt)로 자동 생성합니다.
100% 상대 경로를 지원하므로 어떤 환경에서도 바로 실행됩니다.
"""

import os
import sys
import re

def convert_script_to_srt(md_path, output_srt_path, seconds_per_scene=15):
    if not os.path.exists(md_path):
        print(f"[오류] 대본 파일을 찾을 수 없습니다: {md_path}")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 각 씬 분리
    scene_blocks = re.split(r"(?:### 🎬 Scene|\[ \d+장면 \]  🎬 Scene)", content)
    
    srt_items = []
    current_time_sec = 0

    scene_index = 1
    for block in scene_blocks[1:]:
        # 자막용 대본 파싱
        caption_match = re.search(r"📝\s*(?:\*\*)?\[자막용 대본\](?:\*\*)?\s*:\s*\n([^\n]+(?:\n[^\n]+)*?)(?=\n\s*[-*•]?\s*🔊|\Z)", block)
        if not caption_match:
            caption_match = re.search(r"(?:4\.\s*)?📝\s*(?:\*\*)?\[자막(?:\s*용)?\s*대본\](?:\*\*)?\s*:\s*\n([^\n]+(?:\n[^\n]+)*?)(?=\n\s*(?:5\.|\Z))", block)

        if caption_match:
            raw_text = caption_match.group(1).strip()
            # 마크다운 인용부호, 백틱, 세로줄 등 정리
            clean_lines = []
            for line in raw_text.split("\n"):
                l = line.strip()
                l = re.sub(r"^[>│\s\-*•]+", "", l)
                l = l.replace("`", "").strip()
                if l and not l.startswith("🔊"):
                    clean_lines.append(l)
            
            caption_text = "\n".join(clean_lines) if clean_lines else f"Scene {scene_index}"
        else:
            caption_text = f"Scene {scene_index}"

        # 시간 계산
        start_min, start_sec = divmod(current_time_sec, 60)
        start_hr, start_min = divmod(start_min, 60)

        end_time_sec = current_time_sec + seconds_per_scene
        end_min, end_sec = divmod(end_time_sec, 60)
        end_hr, end_min = divmod(end_min, 60)

        start_ts = f"{start_hr:02d}:{start_min:02d}:{start_sec:02d},000"
        end_ts = f"{end_hr:02d}:{end_min:02d}:{end_sec:02d},000"

        srt_items.append(f"{scene_index}\n{start_ts} --> {end_ts}\n{caption_text}\n")
        current_time_sec = end_time_sec
        scene_index += 1

    # 상대 경로 기준 저장 폴더 생성
    out_dir = os.path.dirname(output_srt_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_items))

    print(f"[성공] 총 {len(srt_items)}개 장면의 자막이 생성되었습니다 -> {output_srt_path}")
    return True

if __name__ == "__main__":
    # 스크립트 실행 위치 기준 100% 상대 경로 계산
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
    
    # 기본 입력: 예시 완성본 마크다운
    default_input = os.path.join(BASE_DIR, "examples", "rabbit_and_turtle_master.md")
    # 기본 출력: result 폴더 내 자막 파일
    default_output = os.path.join(BASE_DIR, "result", "subtitles.srt")

    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_file = sys.argv[2] if len(sys.argv) > 2 else default_output

    print(f"[*] 자막 변환 시작...")
    print(f"  - 입력 파일: {os.path.relpath(input_file, BASE_DIR)}")
    print(f"  - 출력 파일: {os.path.relpath(output_file, BASE_DIR)}")
    convert_script_to_srt(input_file, output_file)
