# -*- coding: utf-8 -*-
"""
==============================================================================
[2026 Antigravity] 인터랙티브 반응형 HTML5 대시보드 컴파일러
==============================================================================
단일 독립 실행형 HTML 파일로 Chart.js, 검색 필터, 탭 전환, 실시간 렌더링을
지원하는 최신 다크 테마 대시보드를 생성합니다.
"""

import os
import json

class DashboardGenerator:
    def __init__(self):
        pass

    def generate(self, keyword_data, output_path="result/dashboard.html"):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 통계 집계
        total_kws = len(keyword_data)
        golden_kws = sum(1 for x in keyword_data if x.get("golden_score", 0) >= 80)
        avg_products = int(sum(x.get("total_products", 0) for x in keyword_data) / max(total_kws, 1))
        avg_price = int(sum(x.get("avg_price", 0) for x in keyword_data) / max(total_kws, 1))
        
        # 카테고리별 집계
        cat_counts = {}
        for x in keyword_data:
            c = x.get("category", "기타")
            cat_counts[c] = cat_counts.get(c, 0) + 1
            
        # 등급별 집계
        grade_counts = {"S": 0, "A": 0, "B": 0, "C": 0}
        for x in keyword_data:
            g_str = str(x.get("comp_grade", "B"))[0]
            if g_str in grade_counts:
                grade_counts[g_str] += 1
                
        # Top 10 키워드 비교 데이터
        top10 = sorted(keyword_data, key=lambda x: x.get("golden_score", 0), reverse=True)[:10]
        top10_labels = [x.get("keyword") for x in top10]
        top10_avg_prices = [x.get("avg_price", 0) for x in top10]
        top10_rec_prices = [x.get("recommended_price", 0) for x in top10]
        
        raw_json = json.dumps(keyword_data, ensure_ascii=False)
        
        html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2026 Antigravity | 네이버 쇼핑 황금키워드 인텔리전스</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css" rel="stylesheet">
<style>
  :root {{
    --bg-main: #090d16;
    --card-bg: rgba(22, 30, 49, 0.75);
    --border: rgba(255, 255, 255, 0.08);
    --primary: #38bdf8;
    --secondary: #818cf8;
    --emerald: #34d399;
    --amber: #fbbf24;
    --rose: #f43f5e;
    --text-primary: #f8fafc;
    --text-muted: #94a3b8;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Pretendard', sans-serif; }}
  body {{ background: var(--bg-main); color: var(--text-primary); min-height: 100vh; padding: 2.5rem; }}
  
  .top-header {{ display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 2rem; }}
  .title-h1 {{ font-size: 2.1rem; font-weight: 800; background: linear-gradient(135deg, #38bdf8, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
  .title-sub {{ color: var(--text-muted); font-size: 0.95rem; margin-top: 0.4rem; }}
  .live-badge {{ background: rgba(56, 189, 248, 0.12); color: var(--primary); border: 1px solid rgba(56, 189, 248, 0.4); padding: 0.5rem 1.1rem; border-radius: 9999px; font-size: 0.85rem; font-weight: 700; }}
  
  .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }}
  .kpi-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 1.2rem; padding: 1.5rem; backdrop-filter: blur(16px); position: relative; overflow: hidden; }}
  .kpi-card::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--primary), var(--secondary)); }}
  .kpi-label {{ color: var(--text-muted); font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }}
  .kpi-val {{ font-size: 2rem; font-weight: 800; margin-top: 0.6rem; color: #ffffff; }}
  .kpi-desc {{ font-size: 0.82rem; color: var(--emerald); margin-top: 0.4rem; }}
  
  .charts-grid {{ display: grid; grid-template-columns: 1fr 1fr 1.3fr; gap: 1.5rem; margin-bottom: 2.5rem; }}
  .chart-panel {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 1.2rem; padding: 1.5rem; backdrop-filter: blur(16px); }}
  .chart-header {{ font-size: 1.1rem; font-weight: 700; margin-bottom: 1.2rem; display: flex; justify-content: space-between; align-items: center; }}
  
  .table-section {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 1.2rem; overflow: hidden; backdrop-filter: blur(16px); }}
  .table-toolbar {{ padding: 1.3rem 1.8rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 1rem; }}
  
  .filter-group {{ display: flex; gap: 0.5rem; flex-wrap: wrap; }}
  .btn-filter {{ background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border); color: var(--text-muted); padding: 0.4rem 0.9rem; border-radius: 0.5rem; font-size: 0.85rem; cursor: pointer; transition: 0.2s; }}
  .btn-filter.active, .btn-filter:hover {{ background: var(--primary); color: #000; font-weight: 700; border-color: var(--primary); }}
  
  .search-input {{ background: rgba(0, 0, 0, 0.4); border: 1px solid var(--border); padding: 0.6rem 1.2rem; border-radius: 0.6rem; color: #fff; width: 280px; outline: none; }}
  .search-input:focus {{ border-color: var(--primary); box-shadow: 0 0 12px rgba(56, 189, 248, 0.3); }}
  
  table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem; }}
  th {{ background: rgba(9, 13, 22, 0.95); padding: 1.1rem 1.5rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase; font-size: 0.78rem; letter-spacing: 0.05em; }}
  td {{ padding: 1.1rem 1.5rem; border-bottom: 1px solid var(--border); vertical-align: middle; }}
  tr:hover {{ background: rgba(255, 255, 255, 0.02); }}
  
  .grade-badge {{ padding: 0.25rem 0.6rem; border-radius: 0.4rem; font-size: 0.78rem; font-weight: 800; }}
  .grade-S {{ background: rgba(52, 211, 153, 0.15); color: var(--emerald); border: 1px solid var(--emerald); }}
  .grade-A {{ background: rgba(56, 189, 248, 0.15); color: var(--primary); border: 1px solid var(--primary); }}
  .grade-B {{ background: rgba(251, 191, 36, 0.15); color: var(--amber); border: 1px solid var(--amber); }}
  .grade-C {{ background: rgba(244, 63, 94, 0.15); color: var(--rose); border: 1px solid var(--rose); }}
  
  .score-cell {{ font-weight: 800; color: var(--emerald); font-size: 1.05rem; }}
  .kw-link {{ color: #ffffff; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 0.4rem; }}
  .kw-link:hover {{ color: var(--primary); text-decoration: underline; }}
</style>
</head>
<body>

  <div class="top-header">
    <div>
      <div class="title-h1">AI 네이버 쇼핑 황금키워드 인텔리전스</div>
      <div class="title-sub">2026 Antigravity 리메이크 파이프라인 | 실시간 데이터랩 베스트 키워드 & 시장성 분석</div>
    </div>
    <div class="live-badge">● 실시간 수집 완료 ({total_kws}개 분석)</div>
  </div>

  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-label">전체 분석 키워드</div>
      <div class="kpi-val">{total_kws}개</div>
      <div class="kpi-desc">전 카테고리 / 성별 / 연령 교차 분석</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">황금키워드 (S/A급)</div>
      <div class="kpi-val" style="color: var(--emerald);">{golden_kws}개</div>
      <div class="kpi-desc">즉시 소싱 추천 블루오션 키워드</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">평균 시장 등록 상품수</div>
      <div class="kpi-val">{avg_products:,}개</div>
      <div class="kpi-desc">네이버 쇼핑 평균 리스팅 규모</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">평균 적정 진입가</div>
      <div class="kpi-val">{avg_price:,}원</div>
      <div class="kpi-desc">사분위(IQR) 기반 최적 마진 타깃가</div>
    </div>
  </div>

  <div class="charts-grid">
    <div class="chart-panel">
      <div class="chart-header">
        <span>📊 카테고리별 키워드 분포</span>
      </div>
      <canvas id="catChart" height="220"></canvas>
    </div>
    <div class="chart-panel">
      <div class="chart-header">
        <span>🎯 경쟁 등급 비중 (S ~ C)</span>
      </div>
      <canvas id="gradeChart" height="220"></canvas>
    </div>
    <div class="chart-panel">
      <div class="chart-header">
        <span>💰 Top 10 황금키워드 (평균가 vs 추천진입가)</span>
      </div>
      <canvas id="priceCompChart" height="220"></canvas>
    </div>
  </div>

  <div class="table-section">
    <div class="table-toolbar">
      <div class="filter-group" id="catFilters">
        <button class="btn-filter active" onclick="filterCategory('전체')">전체보기</button>
      </div>
      <input type="text" id="searchInput" class="search-input" placeholder="키워드, 카테고리 실시간 검색..." onkeyup="filterTable()">
    </div>
    <table id="mainTable">
      <thead>
        <tr>
          <th style="width: 70px;">순위</th>
          <th>카테고리</th>
          <th>타깃(성별/연령)</th>
          <th>키워드</th>
          <th style="width: 120px;">경쟁등급</th>
          <th style="width: 130px;">총 상품수</th>
          <th style="width: 130px;">평균 판매가</th>
          <th style="width: 130px;">적정 진입가</th>
          <th style="width: 100px;">황금스코어</th>
        </tr>
      </thead>
      <tbody>
"""
        for item in keyword_data:
            g_raw = str(item.get("comp_grade", "A"))
            g_char = g_raw[0] if g_raw else "A"
            kw = item.get("keyword", "")
            target_str = f"{item.get('gender', '전체')} {item.get('age', '전체')}"
            
            html += f"""
        <tr data-cat="{item.get('category')}">
          <td><strong style="color:var(--primary);">#{item.get('rank')}</strong></td>
          <td><span style="color:var(--text-muted);">{item.get('category')}</span></td>
          <td>{target_str}</td>
          <td>
            <a href="https://search.shopping.naver.com/search/all?query={kw}" target="_blank" class="kw-link">
              {kw} ↗
            </a>
          </td>
          <td><span class="grade-badge grade-{g_char}">{item.get('comp_grade')}</span></td>
          <td>{item.get('total_products', 0):,}개</td>
          <td>{item.get('avg_price', 0):,}원</td>
          <td><strong style="color:var(--primary);">{item.get('recommended_price', 0):,}원</strong></td>
          <td class="score-cell">{item.get('golden_score', 80)}점</td>
        </tr>
        """
        
        html += f"""
      </tbody>
    </table>
  </div>

<script>
  const rawData = {raw_json};
  const catData = {json.dumps(cat_counts, ensure_ascii=False)};
  const gradeData = {json.dumps(grade_counts, ensure_ascii=False)};

  // 1. 카테고리 도넛 차트
  new Chart(document.getElementById('catChart'), {{
    type: 'doughnut',
    data: {{
      labels: Object.keys(catData),
      datasets: [{{
        data: Object.values(catData),
        backgroundColor: ['#38bdf8', '#818cf8', '#c084fc', '#f43f5e', '#fbbf24', '#34d399', '#a78bfa', '#fb7185'],
        borderWidth: 0
      }}]
    }},
    options: {{
      responsive: true,
      plugins: {{ legend: {{ position: 'bottom', labels: {{ color: '#94a3b8', font: {{ size: 11 }} }} }} }}
    }}
  }});

  // 2. 경쟁 등급 바 차트
  new Chart(document.getElementById('gradeChart'), {{
    type: 'bar',
    data: {{
      labels: ['S급(초특급)', 'A급(유리함)', 'B급(보통)', 'C급(치열)'],
      datasets: [{{
        data: [gradeData['S'], gradeData['A'], gradeData['B'], gradeData['C']],
        backgroundColor: ['#34d399', '#38bdf8', '#fbbf24', '#f43f5e'],
        borderRadius: 8
      }}]
    }},
    options: {{
      responsive: true,
      scales: {{
        x: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ display: false }} }},
        y: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
      }},
      plugins: {{ legend: {{ display: false }} }}
    }}
  }});

  // 3. 가격 비교 바 차트
  new Chart(document.getElementById('priceCompChart'), {{
    type: 'bar',
    data: {{
      labels: {json.dumps(top10_labels, ensure_ascii=False)},
      datasets: [
        {{
          label: '평균가',
          data: {json.dumps(top10_avg_prices)},
          backgroundColor: 'rgba(148, 163, 184, 0.4)',
          borderRadius: 6
        }},
        {{
          label: '추천진입가',
          data: {json.dumps(top10_rec_prices)},
          backgroundColor: '#38bdf8',
          borderRadius: 6
        }}
      ]
    }},
    options: {{
      responsive: true,
      scales: {{
        x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }}, grid: {{ display: false }} }},
        y: {{ ticks: {{ color: '#94a3b8' }}, grid: {{ color: 'rgba(255,255,255,0.05)' }} }}
      }},
      plugins: {{ legend: {{ labels: {{ color: '#94a3b8' }} }} }}
    }}
  }});

  // 카테고리 필터 버튼 동적 생성
  const catFilterContainer = document.getElementById('catFilters');
  Object.keys(catData).slice(0, 7).forEach(cat => {{
    const btn = document.createElement('button');
    btn.className = 'btn-filter';
    btn.innerText = cat;
    btn.onclick = () => filterCategory(cat);
    catFilterContainer.appendChild(btn);
  }});

  let currentCategory = '전체';

  function filterCategory(cat) {{
    currentCategory = cat;
    document.querySelectorAll('.btn-filter').forEach(b => {{
      b.classList.toggle('active', b.innerText === (cat === '전체' ? '전체보기' : cat));
    }});
    applyFilters();
  }}

  function filterTable() {{
    applyFilters();
  }}

  function applyFilters() {{
    const searchVal = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.querySelectorAll('#mainTable tbody tr');
    rows.forEach(r => {{
      const text = r.innerText.toLowerCase();
      const cat = r.getAttribute('data-cat');
      const matchesCat = (currentCategory === '전체' || cat === currentCategory);
      const matchesSearch = text.includes(searchVal);
      r.style.display = (matchesCat && matchesSearch) ? '' : 'none';
    }});
  }}
</script>
</body>
</html>
"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[+] 반응형 웹 대시보드가 성공적으로 생성되었습니다: {output_path}")

if __name__ == "__main__":
    gen = DashboardGenerator()
    sample = [
        {"rank": 1, "category": "디지털/가전", "gender": "남성", "age": "30대", "keyword": "닌텐도스위치2", "comp_grade": "S (블루오션)", "total_products": 28500, "avg_price": 76000, "recommended_price": 69000, "golden_score": 95},
        {"rank": 2, "category": "스포츠/레저", "gender": "전체", "age": "전체", "keyword": "캠핑의자", "comp_grade": "A (유리함)", "total_products": 64000, "avg_price": 42000, "recommended_price": 38000, "golden_score": 88}
    ]
    gen.generate(sample)
