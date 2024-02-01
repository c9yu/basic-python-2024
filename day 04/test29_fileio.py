# file : test29_fileio.py
# date : 20240201
# desc : 텍스트 파일 읽기

f = open('sample.txt',mode='r', encoding='utf-8')

### <기초적이나 단점이 있는 방법>
# text = f.read() # read()는 mode 'r'일때 사용 
# print(text)     # 텍스트 파일의 모든 텍스트를 전부 한번에 읽어오는데 파일 사이즈가 너무 크면 불가능하다. 
                  # 이런 단점때문에 잘 사용하지 않는다.

### <가장 일반적인 방법>
while True:
    line = f.readline()
    if not line:       # 조건문, 반복문 내의 코드가 한 줄(ex. if not line break만 있으면 if 옆에 바로 적을수 있음  
        break          # 줄이 늘어나면 거의 불가능 

    print(line.replace('\n', ''))

f.close()
