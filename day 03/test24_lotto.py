# file : test24_lotto.py
# date : 20240131
# desc : 로또 번호 생성

import random as rnd # 랜덤은 주로 rnd로 줄여서 많이 사용

# numbers = list(range(1, 46))

# #print(numbers)
# lottery = list()

# for i in range(6): # 0, 1, 2, 3, 4, 5 총 6번
#     lottery.append(rnd.choice(numbers)) # 1 ~ 45까지 숫자 중 하나를 랜덤으로 꺼내기

# lottery.sort()
# print(lottery)

numbers = weight = list(range(1, 46))
lottery = list()
rnd.shuffle(weight)

lottery = rnd.choices(numbers, weights = weight, k = 6)
lottery.sort
print(lottery) 