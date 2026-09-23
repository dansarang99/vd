from playwright.sync_api import sync_playwright
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    captured_data = []
    
    def handle_response(res):
        if 'getCategoryKeywordRank.naver' in res.url:
            try:
                captured_data.append({
                    'url': res.url,
                    'post_data': res.request.post_data,
                    'json': res.json()
                })
            except Exception as e:
                pass

    page.on("response", handle_response)
    
    page.goto('https://datalab.naver.com/shoppingInsight/sCategory.naver', timeout=20000)
    page.wait_for_timeout(2000)
    
    btn = page.locator('a.btn_submit, a:has-text("조회하기")')
    if btn.count() > 0:
        btn.first.click()
        page.wait_for_timeout(3000)
        
    print(f'Captured {len(captured_data)} rank responses!')
    for item in captured_data:
        print('POST DATA:', item['post_data'])
        ranks = item['json'].get('ranks', [])
        print(f'Ranks returned: {len(ranks)}')
        for r in ranks[:5]:
            print('  >', r)
            
    browser.close()
