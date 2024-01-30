# date : 20240130
# desc : 여러 조건 if문

date = input('날짜 입력(ex.12-01) > ') # 문자열로 들어온다.

month = date.split('-')[0]  # 12(월)
day = date.split('-')[1]    # 01(일)

if month == '12' and day == '25': # 12월 25일
    print('메리 크리스마스!')
elif month == '01' and day == '01': # 1월 1일
    print('해피 뉴이어!')
elif month == '04' and day == '14': # 4월 14일
    print('짜장면 먹는 날!')
else:
    print('평범한 날입니다.')