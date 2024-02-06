# file : test41_pyqt.py
# date : 20240206
# desc : PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *     # import * : 전부 가져온다.
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget # 용량을 고려하지 않는다면 'import *' 이 가장 간단한 방법이다.

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 추가
        pixmap = QPixmap('./images/dog.jpg').scaledToWidth(400) # .scaledToWidth(800) 더 큰 해상도를 넓이 800으로 고정한다.
        #pixmap = QPixmap('./images/dog.jpg').scaledToHeight(800) # 사진 비율 자체는 동일하므로 지정해준 값에 맞춰서 크기가 조절된다.

        lblimage = QLabel(self)
        lblimage.setPixmap(pixmap)
        lblSize = QLabel(self) # 디자이너에서 사용하는 라벨과 같은 것
        lblSize.setFont(QFont('Gothic, 20')) 
        lblSize.setStyleSheet('Color : #ff33ff;') # color : red, blue 등도 가능하고 ff00ff는 rgb값(16진수)을 순서대로 나열한 것
        lblSize.setText(f'{pixmap.width()} X {pixmap.height()}') # dog.jpg의 width X height
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter) # 가로 중앙정렬 | 세로 중앙정렬 
        
        vbox = QVBoxLayout(self) # QtDesigner VerticalLayout 위젯 생성
        vbox.addWidget(lblimage) # VerticalLayout을 추가한다.
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VerticalLayout 추가와 동일

        self.setWindowIcon(QIcon('./images/iot.png')) # 실행시 나오는 좌측 상단의 아이콘 변경
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300, 300, 300, 300) # x, y, w, h 
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언해 놓고 입맛에 맞게 골라쓰는 것 (오버로딩)
        # self.setGeometry(300,300,300,300)
        self.setCenter()
        self.show() # showFullScreen() : 의 경우 화면을 가득 채우는 형태

    def setCenter(self): # 윈 앱을 화면 정 중앙에 위치시킨다.
        gm = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry() # 모니터 해상도 구하는 법
    width, height = screen_rect.width(), screen_rect.height()
    print(width, 'x', height) # 활용도가 높다
    ins = WinApp()
    sys.exit(app.exec_()) # 종료시 리소스 반환 등 효율을 위한 구문 : app.exec_()로도 실행 자체는 가능



