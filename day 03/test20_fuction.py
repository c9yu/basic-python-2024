# file : test20_function.py
# date : 20240131
# desc : 함수 만들기 (계산기 기능)

# 형태 : def 함수명 (매개변수)
#        수행할 문장 1
#        수행할 문장 2

def add(x, y) -> int:
    result = x + y
    return result

def min(x, y) -> int:
    result = x - y
    return result

def mul(x, y) -> int:
    result = x * y
    return result

def div(x, y) -> float:
    result = x/y
    return result

def say_hello() -> None:
    print('Hello')
#    return None     # None을 리턴하는 것은 의미가 없기 때문에 생략하는 것이다.

say_hello()
print('더하기 -> ')
a, b = map(int, input('두 정수 입력(공백으로 구분) >').split(' '))
결과 = add(a, b) # add(a, b) : 함수 결과값을 리턴을 통해 받는다.
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {min(a, b)}')
print(f'{a} X {b} = {mul(a, b)}')
print(f'{a} / {b} = {div(a, b)}')


