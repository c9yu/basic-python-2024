# date : 20240130
# desc : 복합자료형 list

### 학생들의 국어 점수의 평균을 구하려 한다.
s1 = 80 # 학생1 의 점수 80점
s2 = 90
s3 = 100
s4 = 50
s5 = 60

koreansum = s1 + s2 + s3 + s4 + s5
print(koreansum)   # 점수의 총 합
print(koreansum/5) # 점수의 평균
# 이 경우 학생의 수가 늘어날 경우 점점 코드가 길어진다.

print('--------------------------------------------------------------')

# 그러나 리스트를 활용할 경우
std = [80, 90, 100, 50, 60] # 변수를 추가하기 쉽다.

# 리스트의 각 자리의 번호를 index라고 하며, 첫번째 자리는 1이 아닌 '0'부터 시작한다.
# 즉, 리스트 std는 index는 0, 1, 2, 3, 4까지이다.

### 리스트 요소 접근 
print(std[3]) # 리스트 std의 index 3의 값을 출력하라 : 50
#print(std[5]) # index 5는 없다.

### 파이썬 리스트의 특징
list_1 = [256, 3.5, '문자열', True, [1, 2, 3, 4], (3, 4), std] # 파이썬의 리스트는 아무거나 다 들어간다.
print(list_1)
print([list_1[5]])

list_1[6] = '바꾼 값' # 리스트의 값을 변경
print(list_1)

print('--------------------------------------------------------------')

### 리스트 연산
print(list_1[2:4]) 
# 내가 만약 n번째 인덱스의 값까지 출력을 하고 싶다면
# print(list_1[2:n+1])이 되어야 한다.

print(list_1[-5:-3])
# 인덱스의 끝자리는 -1이기도 하다. 
# 즉, list_1의 인덱스는 0  1  2  3  4  5  6 
#                     -7 -6 -5 -4 -3 -2 -1  가 된다.                

### 이중 리스트
print(list_1[4][2]) # 리스트 안의 리스트의 index 2의 값   

### 응용
list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2]) # 출력될 값을 예상해 보자 : 6

list_4 = [1,2,3]
list_5 = [7,8,9]
# 리스트 연산은 +, *만 사용 가능
print(list_4 + list_5) # + : 리스트를 연결
print(list_5 * 2) # * : 리스트를 반복

# 리스트 길이
print(len(list_4))

# append() 리스트 마지막에 하나 추가
# insert(index, val) 리스트의 해당 index에 val을 추가 -> 기존의 값은 뒤로 밀린다.
print(list_1) 

list_1.append('Hello')
print(list_1)

list_1.insert(2, 100)
print(list_1)

# extend() 기존 리스트 확장
list_4.extend(list_5) # list_4에 list_5를 추가한다.
print(list_4)

print(list_5)
print(list_4) # 이후에도 계속해서 추가하여 변경된 상태로 출력되는 list_4 모습
# '+'와 extend는 거의 비슷하지만 '+'의 경우 다른 변수에 값을 할당해줘야 한다.

# 리스트 삭제
del list_4[3]    # 리스트의 인덱스 하나를 삭제
print(list_4)
#del list_4      # 리스트 전체를 삭제해 오류가 발생
#print(list_4)

# pop
val = list_5.pop() # 마지막 값을 꺼내오기
print(val) # [7, 8, 9]에서 9를 꺼내온다.
print(list_5) # 9가 빠지고 [7, 8]만 남는다.

print(std)
val = std.pop(2) # index 2의 값을 꺼내오기
print(val)
print(std) 

# clear() - del과는 다르다
list_5.clear()
print(list_5)
# del의 경우 완전히 삭제해 버리지만, clear()의 경우 텅 빈 리스트로 만들어 버린다.(내용만 삭제)

# sort()
print(list_1)
#list_1.sort() - 문자열, 숫자, 불 섞여있는 리스트는 sort 불가능

print(std)
std.sort()
print(std) # 오름차순 정렬

std.sort(reverse=True)
print(std) # 내림차순 정렬

# in, not in - 내가 찾는 요소가 리스트 안에 있는지 확인하는 용도
print(90 in std) # True
print(98 in std) # False

# reverse(), copy(), count()... 등 추가로 몇가지가 더 있다. std. 을 통해 확인하고, 공부하자
# '*' : 전개연산자 - 사용하는 일은 잘 없다.
list_a = [1, 3, 5]
list_b = [2, 4, 8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)