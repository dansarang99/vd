"""
eda_engine.py
완주로컬푸드 실시간 데이터 탐색적 데이터 분석(EDA) 및 통계량 산출 엔진
- 기능:
  1. 결측치 및 데이터 타입 무결성 검증
  2. 6대 핵심 KPI 지표(총매출, 총판매량, 객단가, 1위 매장 점유율 등) 산출
  3. 매장별, 품목별, 카테고리별 다차원 집계 분석
  4. 품절 임박 및 매출 급증 이상치(Anomaly/Alert) 감지
  5. C-Level 경영진 브리핑 텍스트(Markdown) 자동 생성
"""

import os
import sys
import io
import pandas as pd
import numpy as np

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass



def run_eda(df_or_csv):
    """
    수집된 판매현황 데이터를 대상으로 심층 EDA를 수행하고 결과 딕셔너리 반환
    """
    if isinstance(df_or_csv, str):
        df = pd.read_csv(df_or_csv, encoding='utf-8-sig')
    else:
        df = df_or_csv.copy()

    # 1. 기본 무결성 검증 및 전처리
    df['판매금액'] = pd.to_numeric(df['판매금액'], errors='coerce').fillna(0).astype(int)
    df['판매수량'] = pd.to_numeric(df['판매수량'], errors='coerce').fillna(0).astype(int)
    df['단위가격'] = pd.to_numeric(df['단위가격'], errors='coerce').fillna(0).astype(int)

    # 2. 핵심 KPI 집계
    total_revenue = int(df['판매금액'].sum())
    total_quantity = int(df['판매수량'].sum())
    avg_price = int(total_revenue / max(1, total_quantity))
    record_count = len(df)
    current_time = df['집계시간'].iloc[0] if '집계시간' in df.columns and len(df) > 0 else "12:00"
    current_date = df['판매일자'].iloc[0] if '판매일자' in df.columns and len(df) > 0 else "오늘"

    # 3. 매장별 매출 분석
    store_agg = df.groupby('판매매장명').agg(
        매출액=('판매금액', 'sum'),
        판매수량=('판매수량', 'sum'),
        취급품목수=('품목명', 'nunique')
    ).reset_index()
    store_agg['점유율'] = (store_agg['매출액'] / total_revenue * 100).round(1)
    store_agg = store_agg.sort_values(by='매출액', ascending=False)
    
    top_store = store_agg.iloc[0] if len(store_agg) > 0 else None
    top_store_name = top_store['판매매장명'] if top_store is not None else "-"
    top_store_rev = int(top_store['매출액']) if top_store is not None else 0
    top_store_share = top_store['점유율'] if top_store is not None else 0.0

    # 4. 품목별 매출 분석
    item_agg = df.groupby(['품목카테고리', '품목명', '판매단위']).agg(
        총판매금액=('판매금액', 'sum'),
        총판매수량=('판매수량', 'sum'),
        평균단가=('단위가격', 'mean')
    ).reset_index()
    item_agg['매출비중'] = (item_agg['총판매금액'] / total_revenue * 100).round(1)
    item_agg = item_agg.sort_values(by='총판매금액', ascending=False)
    
    top_item = item_agg.iloc[0] if len(item_agg) > 0 else None
    top_item_name = top_item['품목명'] if top_item is not None else "-"
    top_item_rev = int(top_item['총판매금액']) if top_item is not None else 0
    top_item_qty = int(top_item['총판매수량']) if top_item is not None else 0

    # 5. 카테고리별 매출 분석
    cat_agg = df.groupby('품목카테고리').agg(
        매출액=('판매금액', 'sum'),
        판매수량=('판매수량', 'sum')
    ).reset_index()
    cat_agg['점유율'] = (cat_agg['매출액'] / total_revenue * 100).round(1)
    cat_agg = cat_agg.sort_values(by='매출액', ascending=False)

    # 6. 이상치 및 모니터링 알림(Alert Engine)
    alerts = []
    # 회전율 급증 품목 감지 (평균 판매수량의 1.5배 초과)
    mean_qty = item_agg['총판매수량'].mean()
    high_turnover_items = item_agg[item_agg['총판매수량'] > mean_qty * 1.4]['품목명'].tolist()
    if high_turnover_items:
        alerts.append({
            "type": "🔥 인기 품목 고속 소진",
            "message": f"[{', '.join(high_turnover_items[:3])}] 품목의 주문 속도가 급증하여 당일 물량 조기 품절이 예상됩니다."
        })
    alerts.append({
        "type": "🏪 매장 밸런스 점검",
        "message": f"최고 매출 매장인 [{top_store_name}]이 전체 매출의 {top_store_share}%를 견인하고 있습니다."
    })

    # 7. 구조화된 결과 객체
    eda_results = {
        "summary": {
            "current_date": current_date,
            "current_time": current_time,
            "total_revenue": total_revenue,
            "total_quantity": total_quantity,
            "avg_price": avg_price,
            "record_count": record_count,
            "top_store_name": top_store_name,
            "top_store_rev": top_store_rev,
            "top_store_share": top_store_share,
            "top_item_name": top_item_name,
            "top_item_rev": top_item_rev,
            "top_item_qty": top_item_qty
        },
        "store_agg": store_agg,
        "item_agg": item_agg,
        "cat_agg": cat_agg,
        "alerts": alerts,
        "raw_df": df
    }

    return eda_results

def generate_executive_markdown(eda_results, output_path=None):
    """경영진 보고용 C-Level 요약 마크다운 문서 생성"""
    s = eda_results['summary']
    alerts = eda_results['alerts']
    store_agg = eda_results['store_agg']
    item_agg = eda_results['item_agg']

    md = f"""# 📊 완주로컬푸드 오늘의 판매현황 실시간 분석 보고서 (C-Level Brief)

> **보고일시**: {s['current_date']} {s['current_time']} 기준  
> **모니터링 시스템**: Google Opal & Antigravity Cowork 실시간 자동화 파이프라인 (vd17)

---

## 1. 🌟 핵심 경영 성과 지표 (Executive Summary)
* **총 당일 누적 매출액**: **{s['total_revenue']:,}원** (약 {s['total_revenue'] / 100000000:.2f}억원)
* **총 누적 판매 수량**: **{s['total_quantity']:,}개(건)**
* **평균 구매 단가**: **{s['avg_price']:,}원**
* **최대 실적 직매장**: **{s['top_store_name']}** ({s['top_store_rev']:,}원 / 전체의 {s['top_store_share']}%)
* **당일 베스트셀러 품목**: **{s['top_item_name']}** ({s['top_item_rev']:,}원 / {s['top_item_qty']:,}개 판매)

---

## 2. 🚨 실시간 현장 경보 및 운영 인사이트
"""
    for a in alerts:
        md += f"* **{a['type']}**: {a['message']}\n"

    md += """
---

## 3. 🏪 직매장별 실시간 매출 순위
| 순위 | 직매장명 | 당일 매출액 | 누적 판매수량 | 매출 점유율 |
| :---: | :--- | :---: | :---: | :---: |
"""
    for idx, row in store_agg.iterrows():
        md += f"| {idx+1} | {row['판매매장명']} | {int(row['매출액']):,}원 | {int(row['판매수량']):,}개 | {row['점유율']}% |\n"

    md += """
---

## 4. 🥇 품목별 매출 TOP 5
| 순위 | 카테고리 | 품목명 (단위) | 매출액 | 수량 | 평균단가 |
| :---: | :---: | :--- | :---: | :---: | :---: |
"""
    for idx, row in item_agg.head(5).iterrows():
        md += f"| {idx+1} | {row['품목카테고리']} | {row['품목명']} ({row['판매단위']}) | {int(row['총판매금액']):,}원 | {int(row['총판매수량']):,} | {int(row['평균단가']):,}원 |\n"

    md += """
---
*본 문서는 Google Opal과 Antigravity Cowork에 의해 1시간 간격으로 자동 집계 및 갱신됩니다.*
"""

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"[저장 완료] C-Level 마크다운 보고서: {output_path}")

    return md

if __name__ == "__main__":
    from opal_connector import fetch_or_generate_sales
    df, _, _ = fetch_or_generate_sales()
    results = run_eda(df)
    md = generate_executive_markdown(results, "result/executive_summary.md")
    print(md[:300])
