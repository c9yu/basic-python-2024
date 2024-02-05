# file : test36_PyQt.py
# date : 20240205
# desc : PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
# GUI : Graphic User Interface/ CLI : Command Line Interface
from PyQt5.QtWidgets import QApplication, QWidget
#print(sys.argv) # 현재 파이썬 파일의 경로표시

class qtwin_exam(QWidget): # QWidget을 상속받아 사용한다. qtwin_exam(QWidget) : 자식(부모), 부모가 가능한 일은 자식도 기본적으로 가능하다.
    # 생성자
    def __init__(self) -> None:
        super().__init__() # 상속받은 경우 __init__이 엄청 복잡해진다. -> 그래서 수정이 필요하다.
        # 내(self)가 생성되면 __init__ 을 통해 한번 초기화 해주는데
        # 부모(super)또한 생성되면 __init__ 을 통해 한번 초기화 해 준다.
        self.initUI() # 화면 초기화 함수를 호출

    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-300)//2, 400, 300) # 컴퓨터의 경우 좌측 상단이 (0,0)이 된다. x, y, width, height
        self.setWindowTitle('Qt5 Hello World')
        self.text = ''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10))# 10, 10, 10 -> dark gray. #r(0), g(0), b(0) -> black / r(255), g(255), b(255) -> white
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText(130, 150, 'HELLO WORLD')
        paint.drawText(event.rect(), Qt.AlignCenter, self.text) # 여기까지만 해서는 글이 출력되지 않는데 paintEvent 가 필요
                                                                # AlignCenter, AlignLeft, AlignRight

    def paintEvent(self,event) -> None: # 재정의(Override) : 부모의 함수를 다시 정의하는 것
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() # 닫아준다.

loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성할거야
# 무한루프(loop)를 통해 종료버튼을 누르기 전까지 화면이 꺼지지 않도록 해 준다.
isinstance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
loop.exec_()