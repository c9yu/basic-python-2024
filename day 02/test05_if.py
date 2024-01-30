# date : 20240130
# desc : 흐름제어 if

## 어떤 조건이 참인 경우와 거짓인 경우로 나누어 일을 처리하는 것을 if문 이라고 한다. 형태는
## if 조건: - 참인 조건
## elif 조건: - 다른 참인 조건
## else: - 거짓인 조건
number = 10

if number > 0: 
    print('양수입니다.')
elif number == 0:
    print('0입니다.')
elif number < 0:
    print('음수입니다.')
else:
    print('정의할 수 없습니다.')

## 입력함수를 통해 사용자에게 값을 입력받는다.
## 입력 input()
number = int(input('정수 입력 >')) # 입력함수로 입력받는 내용은 문자로 들어간다. 따라서 자료형을 변환해 줄 필요가 있다.

if number > 0:
    print('양수입니다.')
elif number == 0:
    print('0입니다.')
elif number < 0:
    print('음수입니다.')
else:
    print('정의할 수 없습니다.') # 모든 수는 사실 세번째 elif 까지의 조건으로 이미 충분하다.