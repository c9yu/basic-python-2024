# file : test27_eh.py
# date : 20240201
# desc : 예외 처리 : 정말 중요하다!

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y):
    try : 
        return x / y # ZeroDivisionError 발생
    except ZeroDivisionError as e:
        print('[오류]제수는 0이 될 수 없습니다.') # return 0 로 리턴값을 받을 때 3 X 0 = 0은 출력되지 않고 '[오류]~~' 만 출력할 수 없는가?
        return None

# -> 기존에 return 0를 주던것을 return None로 받고
# divide 값이 None이 아닌 경우에 출력하는 것으로 하면 가능하다.


def getOperands(): # 계산 할 수를 입력받고 리턴해주는 함수
    try: # 예외 처리는 try, except 구문으로 처리. 예외가 발생 할 수 있는 부분 (한 문장 말고 의심가는 부분 전부)
        a, b = map(int,input('두 수 입력(구분자는 공백)').split()) # 한 번 이상 반복되는 것은 무조건 함수로 만들어라.
        return a, b 
# 예외 1. int로 값을 받기로 했는데 만일 1.2같은 float 값이 들어오면 예외가 발생함 ValueError
# 예외 2. 값을 2개를 받기로 했는데 값이 3개로 들어오면 예외가 발생
    except ValueError as e: # ValueError as e : ValueError 가 기니까 e로 줄인다. 
        #print(e) # == print(ValueError), ValueError : 정확한 예외 메시지 출력 (사용자 입장에서는 오히려 혼란을 야기할 수 있으므로 굳이 넣을 필요 없다.)
        print('[입력 오류]: 정수만 입력하세요')
        return 1, 1

while True:
    mnu = input('메뉴 선택(p[덧셈], m[뺄셈], t[곱셈], d[나눗셈]), x[종료] > ')

    if mnu == 'p':
        a, b = getOperands()
        print(f'덧셈 {a} + {b} = {add(a, b)}')
    elif mnu == 'm':
        a, b = getOperands()
        print(f'뺄셈 {a} - {b} = {minus(a, b)}')
    elif mnu == 't':
        a, b = getOperands()
        print(f'곱셈 {a} X {b} = {multi(a, b)}')

    elif mnu == 'd':
        a, b = getOperands()
        res= divide(a, b)
        if res != None: 
            print(f'나눗셈 {a} X {b} = {res}')

# 예외 3. 나눗셈에서 0으로 나누는 경우 : Zero Division Error, 예외가 발생
    elif mnu == 'x':
        break
    else:
        continue # 다시 메뉴 선택으로