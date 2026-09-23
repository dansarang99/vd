from playwright.sync_api import sync_playwright
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    responses = []
    page.on("response", lambda res: responses.append(res.url))
    
    page.goto('https://datalab.naver.com/shoppingInsight/sCategory.naver', timeout=20000)
    page.wait_for_timeout(3000)
    
    print('Page Title:', page.title())
    
    # Click search button if present: class "btn_submit" or similar
    btn = page.locator('a.btn_submit, button.btn_submit, a:has-text("조회하기")')
    if btn.count() > 0:
        print('Found submit button, clicking...')
        btn.first.click()
        page.wait_for_timeout(3000)
    
    # Check keyword list
    keywords = page.locator('.rank_top1000_scroll li, .rank_top1000 li, ul.rank_top1000_scroll li').all_inner_texts()
    print(f'Keywords found: {len(keywords)}')
    for k in keywords[:10]:
        print('  >', k.replace('\n', ' '))
        
    print('\nAPI calls detected:')
    for u in responses:
        if 'datalab' in u and ('.naver' in u or 'api' in u):
            print('  API:', u)
            
    browser.close()
