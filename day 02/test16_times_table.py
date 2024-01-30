# file : test16_times_table.py
# date : 20240130
# desc : 구구단 프로그램
# spec : for문의 활용과 2중 for문의 이해가 필요하다.

# 2 X 1 = 2, 2 X 2 = 4, 2 X 3 = 6, ... , 2 X 9 = 18
# 9 X 1 = 9, ...                   ... , 9 X 9 = 81

#x = 2
#for y in range(1, 10):
#    print(f'{x} X {y} = {x*y:2d}')

#x = 3
#for y in range(1, 10):
#    print(f'{x} X {y} = {x*y:2d}')

#x = 4
#for y in range(1, 10):
#    print(f'{x} X {y} = {x*y:2d}') # 이렇게 하나씩 가면 너무 오래 걸리니까

print('구구단 시작!')
for x in range(2, 9+1):
    print(f'{x}단 : ')
    for y in range(1, 9+1):
        print(f'{x} X {y} = {x*y:2d}', end = '  ') # 2중 for문을 사용하면 이렇게 세 문장만으로 끝낼수 있다.
                                                  # 기존에 end = \n으로 설정되어 있는데 이를 end = ' '로 바꿔준다.
        
    print() # 안쪽 for문이 끝나면 마지막에 엔터를 한번 추가


### debugging 단축키

# F9  : 중단점 토글        
# F5  : 디버깅 시작
# 조사식 추가
# F10 : 한줄씩 실행
# F11 : 함수 안으로 진입
# Shift + F5 : 디버깅 종료