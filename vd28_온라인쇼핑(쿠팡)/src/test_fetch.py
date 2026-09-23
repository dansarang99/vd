import requests
from bs4 import BeautifulSoup
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8',
})

# Test 1: Naver DataLab Shopping Insight
r_dl = s.get('https://datalab.naver.com/shoppingInsight/sCategory.naver')
print('DataLab Status:', r_dl.status_code)
if r_dl.status_code == 200:
    soup = BeautifulSoup(r_dl.text, 'html.parser')
    ranks = soup.select('.rank_top1000_scroll .link_text')
    print(f'DataLab Top keywords found: {len(ranks)}')
    for rk in ranks[:10]:
        print(' -', rk.text.strip())

# Test 2: Naver Search Portal Shopping section
r_srch = s.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=캠핑의자')
print('Search Portal Status:', r_srch.status_code)
if r_srch.status_code == 200:
    soup2 = BeautifulSoup(r_srch.text, 'html.parser')
    related = soup2.select('.related_srch .tit, .lst_related_srch .item')
    print(f'Related keywords found: {len(related)}')
    for rel in related[:10]:
        print(' Rel:', rel.text.strip())
