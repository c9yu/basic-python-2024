# file : test21_OOP.py
# date : 20240131
# desc : 객체 지향 클래스 만들기

# 객체는 변수(명사)와 함수(동사)로 이루어져 있으며
# class 는 변수와 함수로 이루어져 있다.

### class(person이라는 객체를 만들기 위한 청사진) 만들기
class person : # 사람 클래스 선언
    name = ''
    age = 0
    gender = '' # 클래스 안에 들어가는 변수 : 멤버변수(명사)

    # 생성자 함수(스페셜 함수) : 클래스의 객체를 생성할 때 동작, 직접 호출해서 사용하는 것이 아닌 자동으로 호출되어 동작
    def __init__(self) -> None:
        self.name = '홍길동'
        self.age = 29
        self.gender = '남자'

    # 클래스를 호출할 때 원하는 형태로 변환해서 보여주는 경우
    def __str__(self) -> str: # str이니 return문이 필요함
        strs = f'커스텀 출력, 이름: {self.name} 객체 생성!'
        return strs

    # 멤버함수 : 멤버함수와 일반 함수의 차이점: walk(self) self가 들어간다. (이는 클래스의 멤버함수이기 때문에 이를 알려주기 위해)
    # init == 초기화
    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')
    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

# 사람 객체 생성, Instance(사례, 예제)
cg = person() # 함수호출처럼 작성하면 된다.
jh = person() # 

# print(type(cg))
# print(id(cg))     # id()를 통해다른 객체임을 확인 할 수 있다.
# print(id(jh))      

cg.name = '이찬규' # 객체명.멤버변수 = ~~  의 형태
cg.age = '26'
cg.gender = '남자'

jh.name = '황지환'
jh.age = '26'
jh.gender = '남자'

print(f'{cg} => 이름: {cg.name} / 나이: {cg.age} / 성별: {cg.gender}')
print(f'{jh} => 이름: {jh.name} / 나이: {jh.age} / 성별: {jh.gender}')

cg.walk
print('1분동안 걷는다.')
cg.stop()

jh.walk
print('걷는 것을 싫어한다.')
jh.stop()

print('생성자 함수 추가 ------------------------------------------------------')
gd = person()
print(f'gd = {gd} => 이름: {gd.name} / 나이: {gd.age} / 성별: {gd.gender}')
print(gd)