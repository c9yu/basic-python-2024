# file : test13_range.py
# date : 20240130
# desc : 리스트 범위 지정

list_a = [1,2,3,4,5,6,7,8,9,10]
print(list_a) # 이 상태에서 범위를 100까지 늘리려면?

# 범위 지정
print(range(5))
print(list(range(5))) # 0부터 n개의 범위 수를 생성한다.

print(list(range(0, 5))) # 0 ~ 4
print(list(range(1, 6))) # 1 ~ 5
print(list(range(5,11))) # 5 ~ 10

print(list(range(4,11,2))) # 5 ~ 10까지 2씩 증가

print(list(range(10, -1, -1))) # 10 ~ 1까지 1씩 감소

# 1. range(a) 괄호 안에 숫자가 하나인 경우 0부터 시작해서 a-1 까지
# 2. range(b, a) 괄호 안에 숫자가 둘 인 경우 b부터 시작해서 a-1 까지
# 3. range(b, a, c) 괄호 안에 숫자가 셋 인 경우 b부터 시작해서 a-1 까지 c씩 증가한다.

#1
list_a = list(range(1,100)) # range() 클래스
print(list_a) 
#2
list_a = [i for i in range(1, 100)] # 리스트 컨프리헨션
print(list_a)

# 위 둘은 동일하니 조금더 편한 것(1번)을 사용하자