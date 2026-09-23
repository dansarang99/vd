import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

s = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Referer': 'https://datalab.naver.com/shoppingInsight/sCategory.naver',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}
s.headers.update(headers)

# 1. First visit page to get session cookies
r_init = s.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')
print('Init status:', r_init.status_code, 'Cookies:', len(s.cookies))

# 2. Post to getCategoryKeywordRank.naver
data = {
    'cid': '50000003', # 디지털/가전
    'timeUnit': 'date',
    'startDate': '2026-08-22',
    'endDate': '2026-09-22',
    'age': '30',
    'gender': 'm', # 30대 남성
    'device': '',
    'page': '1',
    'count': '20'
}

r_post = s.post('https://datalab.naver.com/shoppingInsight/getCategoryKeywordRank.naver', data=data)
print('Post status:', r_post.status_code)
if r_post.status_code == 200:
    res = r_post.json()
    ranks = res.get('ranks', [])
    print(f'Successfully fetched {len(ranks)} keywords for 30대 남성 디지털/가전!')
    for item in ranks[:10]:
        print(f" #{item['rank']} {item['keyword']}")
else:
    print('Response text:', r_post.text[:300])
