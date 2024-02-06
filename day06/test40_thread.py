# file : test40_thread.py
# date : 20240205
# desc : Qt에서 스레드로 동작

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread): # PyQt에서 스레드 QThread 상속
    initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

# 스레드 : 프로세스 하나당 여러 스레드로 나눠 실행해주는 것
# BackWorker(백그라운드 워커)에 대한 설명
    # 스레드 특히 UI 스레드는 혼자서 일을 할 수가 없기 때문에
    # 스레드를 추가해 병렬로 일을 처리하게끔 하는데
    # 이때 추가하는 스레드가 백그라운드 워커?

    def __init__(self, parent)  -> None:
        super().__init__(parent) # 부모 스레드에 있는 초기화 그대로 사용
        self.parent = parent # BackWorker에서 사용할 멤버 변수

    def run(self) -> None: # run : 스레드 실행할 때 사용
        # 스레드로 동작할 내용을 작성
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        #self.parent.pgbTask.setValue(0) # 프로그레스 바 0부터 시작 !! Qthread에선 UI관련 처리를 할 수 없음
        #self.parent.pgbTask.setRange(0, maxVal-1) # 0부터 100까지

        for i in range(maxVal):
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            #self.parent.txblog.append(print_str)
            #self.parent.pgbTask.setValue(i)

class qtwin_exam(QWidget): # UI 스레드

    def __init__(self) -> None:
        super().__init__() 
        uic.loadUi('./day06/ThreadApp.ui', self) # QtDesigner 에서 만든 ui를 로드
        # 버튼에 대한 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행
        # 작업 수행과 이미지 출력 두 가지 일을 나눠서 수행한다.
        th.initSignal.connect(self.initpgbTask) #스레드에서 초기화 시그널이 오면 initPgbTask슬롯 함수가 대신 처리
        th.setSignal.connect(self.setpgbTask)
        th.setLog.connect(self.setTxblog) # TextBrowser 위젯에 진행사항을 출력

# QWidget에 있는 closeEvent를 그대로 쓰면 그냥 닫힘
# 닫을지 말지를 한번 더 물어보는 형태로 다시 구현하고 싶음(재정의: override)

    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료 확인', '종료 하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()
        
    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯함수
    @pyqtSlot(int) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
    def initpgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)
        

    @pyqtSlot(str) # BackWorker 스레드에서 self.initSignal.emit() 동작해서 실행
    def setTxblog(self, msg):
        self.txblog.append(msg)

    @pyqtSlot(int)
    def setpgbTask(self, val):
        self.pgbTask.setValue(val)

if __name__=='__main__':
    loop = QApplication(sys.argv) 
    isinstance = qtwin_exam() 
    isinstance.show()
    loop.exec_()