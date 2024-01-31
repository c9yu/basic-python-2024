# file : test17_input.py
# date : 20240131
# desc : 콘솔 입력

# 출력 - 컴퓨터 화면, 프린터, 스피커, 빔 프로젝터, VR, ...
# 입력 - 콘솔 입력(키보드), 마우스, 목소리, 조이스틱, 터치스크린, ...

# input() - 반드시 input('내용') 내용이 추가되어야 사용자가 문제없이 사용 가능하다.
#temp_val = input('곱할 수 입력 > ')
#temp_val = int(temp_val) - 9번째 10번째 문장은 11번 문장 한 줄로 압축 가능하다.
#temp_val = int(input('곱할 수 입력 > ')) # 문자열형 -> 정수형(형변환) - 만약 형변환을 하지 않은채 수행하면 입력값이 문자열로 들어온다.

temp_val = input('곱할 수(정수) 입력 > ')
if temp_val.isnumeric() == True: # 값을 파악 - 숫자입력이 아니면 튕겨낸다.
    temp_val = int(temp_val) 
    print(f'입력값 = {temp_val}')

# 곱하기
    result = temp_val * 5
    print(f'결과 = {result}') 
else :
    print('잘못된 입력, 정수만 입력하세요.')                          