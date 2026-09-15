"""
check_api_status.py
공공데이터포털(data.go.kr) 완주로컬푸드 오픈API 승인/동기화 상태 실시간 점검 도구
"""

import os
import sys
import io
import urllib.parse
import xml.etree.ElementTree as ET
import requests

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

KEY = os.environ.get("DATA_GO_KR_API_KEY", "fiskecT9sTDtX%2FSiEp4PEucmrVfqb4bhdrcnJ1ZeJ4fTqu9ChfrDDSa6mchONPj4CaUb3UV8Du8AW1RPGEgHPg%3D%3D")
DECODED_KEY = urllib.parse.unquote(KEY)

ENDPOINTS = [
    ("월별 판매현황", "https://apis.data.go.kr/4720000/wanjulocalfoodsalemonth/getSaleMonthList"),
    ("일별 판매현황", "https://apis.data.go.kr/4720000/wanjulocalfoodsaleday/getSaleDayList")
]

def check_status():
    print("==============================================================================")
    print("   [(AX)창업기술 이한규 대표] 공공데이터포털 오픈API 승인 및 실시간 응답 점검")
    print("==============================================================================")
    print(f"• 테스트 키: {KEY[:20]}...{KEY[-15:]}")
    print("• 포털 게이트웨이 질의 중...\n")

    headers = {'User-Agent': 'Mozilla/5.0'}
    approved_any = False

    for name, ep in ENDPOINTS:
        print(f"[{name}] URL: {ep}")
        try:
            params = {'serviceKey': DECODED_KEY, 'pageNo': 1, 'numOfRows': 5}
            r = requests.get(ep, params=params, headers=headers, timeout=5)
            
            if r.status_code == 200 and "<response>" in r.text and "<errMsg>" not in r.text and "<cmmMsgHeader>" not in r.text:
                print(f"  🎉 [승인 완료 / REAL DATA 연동 성공!]")
                print(f"  -> 실서버 응답 샘플: {r.text[:200]}...")
                approved_any = True
            elif "SERVICE_KEY_IS_NOT_REGISTERED_ERROR" in r.text or "30" in r.text:
                print("  ⏳ [동기화 대기 중: 코드 30] 포털 게이트웨이 인증키 전파가 아직 진행 중입니다.")
            elif "99" in r.text or "AUTH_FAIL" in r.text:
                print(f"  ⚠️ [인증 오류]: {r.text[:150]}")
            else:
                print(f"  ℹ️ 상태코드: {r.status_code} | 응답: {r.text[:150]}")
        except requests.exceptions.Timeout:
            print("  ⏳ [응답 지연] 공공데이터 완주군 서버 응답 시간 초과 (대기 필요)")
        except Exception as e:
            print(f"  ❌ 에러: {e}")
        print()

    print("==============================================================================")
    if approved_any:
        print("  ✅ [축하합니다] 공공데이터포털 승인이 완료되었습니다!")
        print("  -> 이제 'command\\02_실시간_파이프라인_1회실행.bat'을 실행하시면")
        print("     100% REAL DATA가 즉시 대시보드에 반영됩니다.")
    else:
        print("  ⏳ 아직 게이트웨이 동기화 진행 중입니다. 잠시 후 다시 확인해 주세요.")
    print("==============================================================================\n")
    return approved_any

if __name__ == "__main__":
    check_status()
