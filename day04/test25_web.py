# file : test25_web.py
# date : 20240201
# desc : urllib 모듈 사용법

#from urllib.request import * # 'import *'은 urllib.request 안의 모든 내용을 다 사용하겠다는 경우
from urllib.request import Request, urlopen # 일부(Request클래스와 urlopen)만 사용하는 경우

req = Request('https://www.naver.com/') # 네이버 웹주소(url)
res = urlopen(req) # url 주소로 웹사이트 열어달라고 요청

print(f'응답코드 : {res.status}') # uls로 요청된 웹사이트가 응답하는지 확인 # 200대가 출력됐다. : 제대로 요청에 응답했다. 
                                                                         # 만약 400대 or 500대가 나오는 경우 : 요청에 응답되지 않았다. 
print(res.read()) # 웹사이트를 긁어온다.

import requests # urlib.request 보다 성능이 조금 더 나은 모듈이다.
# import requests 의 경우 기본 모듈이 아닌 추가로 설치해야 하는 모듈이다.

res2 = requests.get('https://www.naver.com/') 
print(res2.status_code)
print(res2.text)

