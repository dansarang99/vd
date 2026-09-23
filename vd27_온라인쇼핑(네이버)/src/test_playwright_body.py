from playwright.sync_api import sync_playwright
import sys

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    url = 'https://search.shopping.naver.com/search/all?query=%EB%8B%8C%ED%85%90%EB%8F%84%EC%8A%A4%EC%9C%84%EC%89%902'
    page.goto(url, timeout=20000)
    page.wait_for_timeout(3000)
    
    # Save a snippet of body text
    body_text = page.locator('body').inner_text()
    print('Body text snippet (first 1000 chars):')
    print(body_text[:1000])
    
    # Check total count or items
    print('---')
    links = page.locator('a').all_inner_texts()
    print('Sample links:', [l for l in links if l.strip()][:15])
    
    browser.close()
