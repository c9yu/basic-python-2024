# file : test42_pypaint.py
# date : 20240206
# desc : 그림판 만들기

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./day07/pyPaint.ui',self)
        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('Py 그림판')
        self.setCenter()
        self.show()
    
    def setCenter(self):
        gm = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())