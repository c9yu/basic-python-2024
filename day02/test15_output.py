# file : test15_output.py
# date : 20240130
# desc : 콘솔 출력 포맷양식 String Format

print(10) 
print('10') 
# 둘은 각각 숫자 10 문자 10이지만
# 출력된 순간에 있어서는 둘 다 문자로써 출력된다.

string_1 = '{}'.format(10) # {}위치에 format 함수에 들어있는 값을 할당, 원하는 양식으로 표현
print(type(string_1))

name = '이찬규' #input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다.'.format(name)
print(string_2)

string_3 = '{},{},{}'. format(4000, '만', '빌려주세요')
print(string_3)

### 정수를 문자열포맷 하는 방법
string_4 = '_____{:5d}_____'.format(100) # 출력하고자 하는 100 앞에 빈공간이 만들어진다.
print(string_4)

string_5 = '_____{:05d}_____'.format(100) # 출력하고자 하는 100 앞의 빈공간에 0이 채워진다
print(string_5)

string_6 = '_____{:+05d}_____'.format(-100) # 출력하고자 하는 100 앞의 빈공간이 하나 줄어들고 '-0100'이 채워진다
print(string_6)

string_7 = '_____{:=010d}_____'.format(-100) # -000000100
print(string_7)

# d: 정수, 
# 05d: 다섯자리수 만들때 빈자리 0으로 채우기
# 02d: 두 자리수 만들때 빈자리 0으로 채우기 ---------------------------------------------------------- 꼭 기억 (정말 많이 사용함)
# =: 기호와 숫자를 분리,

### 실수 문자열포맷 f
string_8 = '_____{:f}_____'.format(78.123456789) # 소수점은 기본적으로 6번째 자리까지 나타낸다.
print(string_8)

string_9 = '_____{:.2f}_____'.format(78.123456789) # 소수점 두 번째 자리까지 나타내라
print(string_9)

string_10 = '_____{:7.2f}_____'.format(78.123456789) # 전체 자리수는 7자리로, 소수점 뒤는 두 번째 자리까지 나타내라 ---------- 자주 사용

print(string_10)
# 일반적으로 소수점 두번째 자리까지 나타내는 형식을 많이 사용한다.


# python 3.6 이후 도입. format() 함수 아예 사용 하지 않는 방법 ---------------------------------------- 보다 간단
val = 78.123456789
string_11 = f'_____{val:7.2f}_____'
print(string_11)

val = 7
string_11 = f'_____{val:02d}_____'
print(string_11)

string_12 = 'Hello, world!'
print(string_12.upper()) # upeer() : upper case 대문자 변환 함수
print(string_12.lower()) # lower() : lower case 소문자 변환 함수
print(string_12.lower().capitalize()) # 단어의 첫글자들만 대문자로

print(string_12.split(' ')) # 특정한 단어로 자르는 함수 - 리스트이기때문에 반복문 사용가능
print(string_12.split(',')) # 쉼표로 자른경우

string_12 = 'Hello, Life is short, You need python'
words = string_12.split(' ') # 공백으로 자른 경우
print(words)
print(f'문장의 단어 갯수는 {len(words)}개입니다.') # 단어의 개수를 세어준다.

### 다양한 is~~ 함수를 통해 들어온 값을 확인 할 수 있다.
string_13 = 'A10'
print(string_13.isalnum()) # True, isalnum 알파벳과 숫자
print(string_13.isnumeric()) # False, isnumeric 오직 숫자 

string_14 = '10.5'
print(string_14.isdecimal()) # False, 소수의 경우는 함수를 만들어 처리해야 한다.

print('안녕' in '안녕하세요.') # True, 문장안에 단어가 있는지 확인

