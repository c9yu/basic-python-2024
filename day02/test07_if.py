# date : 20240130
# desc : if문 응용

import datetime

now = datetime.datetime.now() # 현재 년월일 시분초를 가져온다.

if now.hour < 12:
    print('오전입니다.')
else: 
    print('오후입니다.')


## 조건을 잘 못 잡은 경우
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print('오전입니다.')
if now.hour >= 10: # 만약 조건을 잘 못 나눠줄 경우 문제가 발생한다.
    print('오후입니다.')