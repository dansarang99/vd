from playwright.sync_api import sync_playwright
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Stealth launch options
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ]
    )
    context = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        viewport={'width': 1920, 'height': 1080},
        locale='ko-KR'
    )
    # inject stealth script
    page = context.new_page()
    page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    url = 'https://m.search.naver.com/search.naver?where=m&sm=top_hty&fbm=0&ie=utf8&query=%EC%BA%A0%ED%95%91%EC%9D%98%EC%9E%90'
    page.goto(url, timeout=20000)
    page.wait_for_timeout(2000)
    
    print('Mobile Title:', page.title())
    body = page.locator('body').inner_text()
    if '쇼핑 서비스 접속이' in body:
        print('Blocked on mobile!')
    else:
        print('SUCCESS on mobile! No block.')
        # check related keywords or shopping cards
        cards = page.locator('.product_info, .shop_item, .tit').all_inner_texts()
        print(f'Items found: {len(cards)}')
        for c in cards[:5]:
            print('  >', c.replace('\n', ' | '))
            
    browser.close()
