# file : test42_pypaint.py
# date : 20240206
# desc : 그림판 만들기

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *     # import * : 전부 가져온다.
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowIcon(QIcon('./images/iot.png')) # 실행시 나오는 좌측 상단의 아이콘 변경
        self.setWindowTitle('Py 그림판')
        rect = QRect(300, 300, 300, 300)
        self.setGeometry(rect)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())