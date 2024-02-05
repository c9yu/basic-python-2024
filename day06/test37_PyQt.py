# file : test37_PyQt.py
# date : 20240205
# desc : PyQt5 이벤트(=Signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('클릭', self)
        btn01.setGeometry(150, 75, 100, 40) # 버튼의 Geometry
        btn01.clicked.connect(self.btn01_clicked) # 버튼을 클릭하면 btn01_clicked 함수를 실행시키겠다.

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('버튼 시그널')
        #self.show() 

    def btn01_clicked(self):
        QMessageBox.about(self, '버튼 클릭', '버튼을 클릭했습니다!') # 나온 창을 닫지 않으면 아래 창은 손 댈 수 없다.

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료 확인', '종료 하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes : # 닫기
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()

if __name__ == '__main__': # Main entry 확인하는 조건
    loop = QApplication(sys.argv)
    isinstance = qtwin_exam()
    isinstance.show() # 22번째 줄과 동일한 역할
    loop.exec_()