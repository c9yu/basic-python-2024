# file : test14_while.py
# date : 20240130
# desc : while문

# if 조건:, elif 조건:, else:, for i range():, while 조건:
# 모두 공통적으로 ':'가 들어간다.

# while 참인 조건:
count = 0

#while count < 10: # count 변수값이 10보다 작거나 같은 동안 반복
while True : # 조건이 참인 동안, 그런데 True는 항상 참이다. 즉, 끝이 나지 않는다. (무한루프)
    count = count + 1
    print('나무찍기', count)
    if count == 10: # 무한루프기 때문에 빠져나갈 곳을 만들어 놓는다.
        break 

# 무한루프 : Window OS, 모바일 OS, 자동차 네비게이션, 라즈베리파이, 아두이노, 게임
#            Winform 개발... 등등에 사용
    
number = 0
while True:
    number = number + 1
    if str(number).count('3') >= 1 or \
       str(number).count('6') >= 1 or \
       str(number).count('9') >= 1 : # 숫자를 문자열로 바꾼 값 안에 '3', '6', '9'가 있으면 짝
       print ('짝!') # 짝! 대신 continue 로 변경

    else: 
        print(number) # print(number) 대신 continue로 변경

    if number > 31:
        break 

# continue 는 반복에서 제외시키는 구문
# break 는 반복문을 완전히 빠져나가는 구문 즉, break가 더 강하다.

