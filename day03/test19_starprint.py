# file : test19_starprint.py
# date : 20240131
# desc : 별 찍기 (피라미드 만들기)

# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    # 1. i가 1일때는, range(1, 2) : 한 번 반복
    # 2. i가 2일때는, range(1, 3) : 두 번 반복
    for j in range(1, i+1): 
        print('*', end = '') # end = \n 대신 empty로 변환
    print('') # 안 쪽 for문이 끝나면 엔터 처리

print('-------------------------------------------------')

for i in range(1, 6):
    for j in range(1, 6-i+1): # range 값 바꿔서 디버깅 해보기
        print(' ', end = '')
    for j in range (1, i+1):
        print('*', end = '') 
    print('') 

print('-------------------------------------------------')

for i in range(1, 6):
    for j in range(1, 6-i+1):
        print(' ', end = '')
    for j in range (1, 2*(i+1)-2):
        print('*', end = '') 
    print('') 
