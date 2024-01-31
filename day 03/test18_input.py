# file : test17_input.py
# date : 20240131
# desc : 다중 입력

### 1. 두 수를 받을 때 가장 원시적인 방법
# 원래는 (input_a, input_b) 튜플형으로 데이터를 받는게 정석 -> 생략해서 input_a,input_b로 
#input_a,input_b = input('값을 두 개 입력(공백으로 구분) > ').split(' ') 
#input_a = int(input_a)
#input_b = int(input_b)

### 2. map() 함수 사용 -- 더 많이 사용함, 1번 방법에서 3문장으로 해결됐던 것을 한 문장으로 처리
input_a, input_b = map(int, input('값을 두 개 입력(공백으로 구분) > ').split(' '))


print(f'입력값 {input_a}, {input_b}')
print(f'더하기 결과{input_a + input_b}')
