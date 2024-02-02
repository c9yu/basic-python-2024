# basic-python-2024
부경대 2024 IOT 개발자과정 기초 프로그래밍 언어 - Python

## 1일차
- 개발환경 구축
    - 코딩 폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 콘솔출력
    - 주석    
    - 변수
    - 자료형
        - 정수형
        - 실수형
        - 문자형
        - 불형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01)) # <Class of 'int'>

    print(5 + 4 / 2) # 7.0
    print(5 == 4)    # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참/거짓으로 조건 분기
            - 하나의 조건의 if문
            - 여러 조건의 if문
        - for : 반복문 기본
        - while : 반복문 변형
    - 복합자료형 + 연산자
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷
    - 구구단 + 디버깅

    ```python
    # debugging
    # F9  : 중단점 토글        
    # F5  : 디버깅 시작
    # 조사식 추가
    # F10 : 한줄씩 실행
    # F11 : 함수 안으로 진입
    # Shift + F5 : 디버깅 종료
    
    print('구구단 시작!')
    for x in range(2, 9+1):
        print(f'{x}단 : ')
        for y in range(1, 9+1):
            print(f'{x} X {y} = {x*y:2d}', end = '  ')  # 2중 for문을 사용하면 이렇게 세 문장만으로 끝낼수 있다.
                                                        # 기존에 end = \n으로 설정되어 있는데 이를 end = ' '로 바꿔준다.
        print() # 안쪽 for문이 끝나면 마지막에 엔터를 한번 추가
    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기 (피라미드 만들기)
    
        ```python
        for i in range(1, 6):
            for j in range(1, 6-i+1):
                print(' ', end = '')
            for j in range (1, 2*(i+1)-2):
                print('*', end = '') 
            print('') 
        ```
    - 함수 (람다함수는 이후에)
    - 객체 지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화 ((ex) __plateNumber)
    - 객체지향 (이후 다시)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중 상속
        - 추상클래스
    
## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        - pip 사용
        
        ```shell
        > pip --version # 버전 확인 -> 버전 확인했는데 최신 버전이 아니면 복사해서 다운 받기
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치 ex) pip install requests -> 마지막 줄에서 Successfully installed를 확인해야 함
        > pip uninstall 패키지명 # 패키지를 삭제 
        ```
    - 예외 처리 : 비정상적 프로그램 종료 막기

        ```python
        def divide(x, y):
            try : 
                return x / y # ZeroDivisionError 발생
            except ZeroDivisionError as e:
                print('[오류]제수는 0이 될 수 없습니다.') 
                return 0
        ```
    - 텍스트 파일 입출력

        ```python
        f = open('파일명', mode= 'r|w|a', encoding='cp949|utf-8')
        f.read()
        f.readline() # 읽기
        f.write('text') # 쓰기
        f.close() # 파일은 반드시 닫는다.
        ```

- 파이썬 응용
    - 주피터 노트북
        - Ctrl + Shift + P -> (명령 팔레트) 로 시작
        - 사용방법 (test31_jupyternb.ipynb 참조)
    - folium
    ![folium 사용법](https://raw.githubusercontent.com/c9yu/basic-python-2024/main/images/python_001.png)
    - 이미지 업로드는 이미지 주소 복사 한 뒤 새로운 탭에서 연 뒤 URL 복사하여 사용

## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(Colab)
    - 