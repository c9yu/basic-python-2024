# file : test28_fileio.py
# date : 20240201
# desc : 텍스트 파일 입출력

# <mode> 
# 1. a(append: 내용 추가) : 이미 있는 내용에 추가 
# 2. r(read: 파일 읽기) : 읽기
# 3. w(write: 파일 쓰기) : 쓰기

# encoding : cp949(ecu-kr : 한글), utf-8(국제 통용어, 어느나라 말이든 다 쓸 수 있는 것)
f = open('sample.txt', mode='w', encoding='utf-8')
# 뭔가를 한다.
f.write('안녕하세요. IOT 개발자 과정입니다.\n') # mode가 a 혹은 w 일 때 f,write() 사용 가능
f.write('반갑습니다!\n') # 추가해도 다음줄에 추가되는 것이 아니다. \n을 사용해야 함

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다.') 

# 결과 : sample.txt 파일이 생성됐다.