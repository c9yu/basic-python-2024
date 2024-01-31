# file : test22_car.py
# date : 20240131
# desc : 자동차 Car 클래스 만들기

class Car :
    wheel_num = 4
    color = 'white'
    plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다.')        

    def moveLeft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def moveRight(self):
        print(f'{self.__plate_num}이 우회전합니다.')

    def __init__(self, plate_num, company, color, gear_type) -> None:
        self.__plate_num = plate_num # 매개변수 plate_num과 self.plate_num은 다른 값이다.
        self.company = company
        self.color = color
        self.gear_type = gear_type
        
    def __str__(self) -> str: # print(객체)했을 때 출력되는 부분 지정한 것
        return f'제 차는 {self.__plate_num}입니다. 색은 {self.color}입니다.'
        
    def getPlateNumber(self): # 외부에서 접근할 수 없도록 막는 조치
        return self.__plate_num
    
    def setPlateNumber(self, new_platenumber):
        self.__plate_num = new_platenumber


sarah = Car('54라 9538', '현대 자동차', '흰색', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차 번호는{sarah.getPlateNumber()}')
print(f'차 색상은{sarah.color}')
sarah.moveForward() # ()빼먹지 않게 주의


sarah.plate_num = '98하 7789(실수로 변경하려고한 번호)' # 누군가 실수로 차 번호를 변경할 수 있다. : 하면 안되는데 이런 일이 일어날 수 있다. 
print(sarah) # 실수로 발생한 번호변경을 막아냄           # 그래서 이를 막기 위해 외부 접근을 막고 Class 내에서만 변경 할 수 있게끔 조치가 필요하다.

sarah.setPlateNumber('11나 1111(제대로 된 방법으로 변경한 번호)')
print(sarah) # 제대로 된 방법으로 번호 변경

# csuv = Car('경남88 1922', '기아 자동차', '회색', '자동')
# print(f'차번호는 {csuv.__plate_num}')
# csuv.moveBackward()

