import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8',
    'Referer': 'https://search.shopping.naver.com/'
})

# Let's test search.shopping.naver.com/search/all?query=...
query = '닌텐도스위치2'
url = f'https://search.shopping.naver.com/search/all?query={requests.utils.quote(query)}'
r = s.get(url)
print('Search HTML status:', r.status_code)
if r.status_code == 200:
    print('HTML length:', len(r.text))
    # Check if __NEXT_DATA__ or window.__PRELOADED_STATE__ exists
    import re
    match_next = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', r.text)
    if match_next:
        data = json.loads(match_next.group(1))
        print('Found __NEXT_DATA__ in search HTML!')
        prods = data.get('props', {}).get('pageProps', {}).get('initialState', {}).get('products', {}).get('list', [])
        print('Products count:', len(prods))
        if prods:
            p0 = prods[0].get('item', {})
            print('Top item:', p0.get('productTitle'), 'Price:', p0.get('lowPrice'), 'Mall:', p0.get('mallName'))
    else:
        # Check window.__PRELOADED_STATE__
        match_pre = re.search(r'window\.__PRELOADED_STATE__\s*=\s*(\{.*?\});\s*</script>', r.text)
        if match_pre:
            print('Found __PRELOADED_STATE__!')
        else:
            print('Checking other script tags...')
