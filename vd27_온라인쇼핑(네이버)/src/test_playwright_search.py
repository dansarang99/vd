from playwright.sync_api import sync_playwright
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    url = 'https://search.shopping.naver.com/search/all?query=%EB%8B%8C%ED%85%90%EB%8F%84%EC%8A%A4%EC%9C%84%EC%89%902'
    page.goto(url, timeout=20000)
    page.wait_for_timeout(2000)
    
    print('Search Page Title:', page.title())
    
    # Try extracting __NEXT_DATA__
    content = page.content()
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', content)
    if match:
        data = json.loads(match.group(1))
        initial_state = data.get('props', {}).get('pageProps', {}).get('initialState', {})
        total = initial_state.get('products', {}).get('total', 0)
        prods = initial_state.get('products', {}).get('list', [])
        print(f'Total search result count: {total:,}')
        print(f'Products loaded in state: {len(prods)}')
        for p_wrap in prods[:5]:
            item = p_wrap.get('item', {})
            print(f" - [{item.get('mallName')}] {item.get('productTitle')} | {item.get('lowPrice')}원 | 리뷰 {item.get('reviewCount')}건 | 평점 {item.get('scoreInfo')}")
    else:
        # Check DOM cards
        cards = page.locator('div[class*="product_item"], div[class*="basicList_item"]').all()
        print(f'Cards in DOM: {len(cards)}')
        
    browser.close()
