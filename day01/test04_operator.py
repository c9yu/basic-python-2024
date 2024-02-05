# date : 20240129
# desc : 연산자

# 사칙 연산 : +, -, *(곱셈), /(나누기), //(정수로 나누기), %(나눈 나머지)
# 비교 연산 : =(값을 할당), ==(비교), >, <, >=, <=, != : 같지 않다
# 논리 연산 : and, or, not

print(2 * 10)
print(2 ** 10)

print(5 / 2)   # 2.5, 실수로 나누기
print(5 // 2)  # 2, 정수로 나누기
print(5 % 2)   # 1,  정수로 나누고 남은 나머지
               ## 어떤 수를 0으로 나누는 것은 불가능

print(5 == 4) # False
# print(5 = 4)
## 불가능 하다.
print(5 > 4)  # True
print(5 >= 4) # True
print(5 <= 4) # False
print(5 < 4)  # Fase
print(5 != 4) # True

# and : 양 쪽 다 참일 경우 참
print(5 > 4 and (5/2 < 3))  # True
print(5 <= 4 and (5/2 < 3)) # False

# or : 한 쪽이라도 참인 경우 참 (or의 경우 and보다 사용 빈도가 적다.)
print(5 <= 4 or (5/2 < 3))  # True

# not : 거짓일 경우 참으로, 참일 경우 거짓으로
print(not (5 <= 4)) # True