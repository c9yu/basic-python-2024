# file : test23_module.py
# date : 20240131
# desc : 모듈 사용

import math

PI = 3.141592
radius = 5
print(f'원의 크기는 {radius * radius * PI}')

# print(math.pi)
print(f'정확한 원의 크기는 {radius * radius * math.pi}')

print(f'sin(0) = {math.cos(0)}')

print(2 ** 10)
print(math.pow(2, 10))

print(math.ceil(3.1)) # 올림
print(math.floor(3.6)) # 내림
print(round(3.5)) # 반올림 : 반올림은 사용 빈도가 커 math가 아닌 기본 함수로 들어가있다.

import math as m # 별명 짓기 : 너무 이름이 긴 모듈의 경우 이름을 줄여 사용할 수 있다.
print(m.sin(2))

from math import pi, pow # 만약 내가 math 안에서 pi와 pow 두 개만 사용하겠다. 하는경우 이렇게 사용 가능하다
print(pi)                # 그러나 이름이 겹쳐 오류가 발생할 수 있다. 이는 주의해야 한다.
print(pow(2,10))