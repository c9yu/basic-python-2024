# date : 20240129
# desc : 자료형

## 기본자료형 - 숫자형, 문자형, 불형, None형 ...
## 추가자료형 - 리스트형, 튜플형, 딕셔너리, 집합 ... (복합자료형은 이후에..)

## None형(python) == null(C, C++, Java, SQL)
## 값은 값인데 아무것도 지정할 수 없는 값 => None
## python에서 변수가 무엇이든 담는 상자에 비유된다면, None는 상자도 없는 상태에 비유된다.
apple = None
print(apple)

## 숫자형 - 정수형, 실수형, 진수형
### 정수형
ten = 10
hundred = 100
temp = -8

### 실수형
pi = 3.141592
tax_rate = 10.0
emp_earn_rate = 3.3
test_val = 2e10
print(test_val)

### 진수형
bit142 = 0b10001110 # 0, 1, 10, 11, 100, 101 ...
oct9= 0o11 # 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15 ...
hex255 = 0xFF # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F ...
print(bit142)
print(oct9)
print(hex255)

## 문자형 - 파이썬에서는 문자, 문자열 차이가 없다.
greeting = 'Hello!'
greeting = "Hello!" # '', "" 홑따옴표, 쌍따옴표 모두 문자열을 나타낸다.
print(greeting)

multi_str = '''Hello!
I am a programmer.
Have a good afternoon.''' # """ """, 도 동일하다
print(multi_str)
multi_str2 = ('Line1\n'
              'Line2\n'
              'Line3') # 혹은 괄호를 벗기고 문장 끝마다 \를 붙이는 것도 동일한 결과를 얻을 수 있다.
print(multi_str2)

## 불형 (Bool, Boolean) - True or False
isCheck = False
print(isCheck)

isCheck = True
print(isCheck)

answer = (3 == 6)
print(answer)
answer = (3.0 == 3)
print(answer)

## 자료형이 어떤 타입인지 체크하는 방법
print(type(apple))
print(type(hundred))
print(type(test_val))
print(type(hex255))
print(type(greeting))
print(type(isCheck))