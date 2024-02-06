# file : test42_pypaint.py
# date : 20240206
# desc : 그림판 만들기

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent 
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI() 
        self.initSignal()

    def initUI(self): # 화면 초기화
        uic.loadUi('./day07/pyPaint.ui',self)
        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('Py 그림판')
        # 캔버스 설정 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;') # 색상칸의 배경을 검정색으로 만든다.
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')

        self.setCenter()
        self.show()

    def initSignal(self): # 동작 초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        # 이미지 로드 및 저장버튼 추가
        self.btn_load.clicked.connect(self.btnloadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)

    def btnloadClicked(self):
        image = QFileDialog.getOpenFileName(None, '이미지 로드', '', 'Image file(*.jpg | *.png)')
        imagePath = image[0]
        #print(imagePath)
        pixmap = QPixmap(imagePath).scaledToHeight(380) # 파일 경로에 있는 이미지를 읽어서 pixmap객체에 넣어준다.
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 라벨 크기에 맞추기

    def btnSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지 저장', '', 'Image file(*.jpg;*.png)' ) # 저장 형태 구현, 실제 저장은 안된다.
        print(filePath)
        if filePath == '':return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)
        

    def buttonClicked(self): # 아래의 black, red, blue를 다 통일한 함수
        btn_val = self.sender().objectName()
        print(btn_val)

        if btn_val == 'btn_black': # 검은색 버튼을 클릭
            self.brushColor = Qt.black

        elif btn_val == 'btn_red':
            self.brushColor = Qt.red

        elif btn_val == 'btn_blue':
            self.brushColor = Qt.blue

        elif btn_val == 'btn_clear':
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)

      # def btnBlueClicked(self):
    #     btn_val = self.sender().objectName() # self.sender() btn_blue
    #     print(btn_val)
    #     self.brushColor = Qt.blue

    # def btnRedClicked(self):
    #     btn_val = self.sender().objectName() # self.sender() btn_red
    #     print(btn_val)
    #     self.brushColor = Qt.red

    # def btnBlackClicked(self):
    #     btn_val = self.sender().objectName() # self.sender() btn_black
    #     print(btn_val)
    #     self.brushColor = Qt.black

    # def btnClearClicked(self):
    #     btn_val = self.sender().objectName()
    #     print(btn_val)
    #     self.canvas.fill(QColor('white'))
    #     self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e) -> None: # 마우스를 클릭한 채 움직이면 실시간으로 클릭된 지점의 좌표를 출력해줌
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap()) # self.lb_canvas.pixmap 안에서만 그리겠다.
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap)) # RoundCap 은 그려지는 선의 끝모양을 동그랗게 만들어준다.
        brush.drawPoint(e.x(), e.y())
        brush.end
        self.update() # 화면 업데이트

    def setCenter(self):
        gm = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())