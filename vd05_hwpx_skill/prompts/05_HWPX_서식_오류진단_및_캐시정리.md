# [프롬프트 05] HWPX 서식 오류 진단 및 레이아웃 캐시 정리

## 목적
외부에서 변환되었거나, 수식/텍스트 편집 후 한컴오피스에서 "알 수 없는 오류입니다", "글씨가 겹쳐 보임", "셀이 잘림" 등의 오류가 발생하는 HWPX 파일을 진단하고 100% 자동 치료합니다.

---

## 사용자 입력 예시
```text
작업 대상: 생성되었거나 다운로드받은 my_document.hwpx
증상:
1. 한글 프로그램으로 열었을 때 특정 문단 글자가 겹쳐서 나옴
2. 표 셀의 내용이 두 줄인데 한 줄만 보이고 잘려 있음
3. 파일을 열 때 '파일을 읽거나 저장하는데 오류가 있습니다' 경고가 뜸
```

---

## AI 에이전트 실행 지침
1. **1단계: 무결성 검사**:
   ```bash
   python scripts/verify_hwpx.py <대상파일.hwpx>
   ```
   - linesegarray 잔존 개수 파악
   - mimetype 압축 방식 및 첫 항목 위치 확인
   - 표 셀 병합 범위(rowSpan, colSpan) 넘침 여부 검사
2. **2단계: 레이아웃 캐시 정리**:
   ```bash
   python scripts/clear_layout_cache.py <대상파일.hwpx>
   ```
   - 문서 내 잔존하는 `<hp:linesegarray>`를 전부 제거하여 한컴오피스가 개방 시 위치를 100% 재계산하도록 조치.
3. **3단계: 표 셀 높이 자동 맞춤**:
   ```bash
   python scripts/autofit_table_rows.py <대상파일.hwpx>
   ```
4. **4단계: 최종 재검증**:
   - `python scripts/verify_hwpx.py <대상파일.hwpx>`를 재실행하여 PASS 출력 확인.
