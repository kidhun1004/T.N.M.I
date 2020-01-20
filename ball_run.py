#-*-coding: utf-8-*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtTest
import numpy
import math
import random
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("UI/ball.ui")[0]

class BallWindow(QMainWindow, form_class):
    allOdd = 0
    allEven = 0
    pOdd = 0
    pEven = 0
    trial = 0
    thN = round(math.pi/2,7)
    exN = 0
    error = 0

    pixmap = list(range(29))
    pixmap_resized = list(range(29))
    label = list(range(29))

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for i in range(1,29):
            self.pixmap[i] = QtGui.QPixmap("ball/blueball_1.png")
        self.pixmap[0] = QtGui.QPixmap("ball/redball.png")

        self.label = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                      self.label_8, self.label_9, self.label_10,self.label_11,self.label_12,self.label_13,self.label_14,self.label_15,self.label_16,
                      self.label_17,self.label_18,self.label_19,self.label_20,self.label_21,self.label_22,self.label_23,self.label_24,self.label_25,
                      self.label_26,self.label_27,self.label_28,self.label_29]

        self.pushButton_10.clicked.connect(self.btn10_clicked)
        self.pushButton_100.clicked.connect(self.btn100_clicked)
        self.pushButton_1000.clicked.connect(self.btn1000_clicked)
        self.pushButton_des.clicked.connect(self.btndes_clicked)

        self.des = QtGui.QPixmap('des/ball.PNG')
        self.des_resized = self.des.scaled(420,230)

    def btn10_clicked(self):
        for i in range(0, 10):
            self.allOdd += self.calOdd(10)
            self.label_odd.setText("홀수 사건 횟수: "+str(self.allOdd))
            self.allEven += self.calEven(10)
            self.label_even.setText("짝수 사건 횟수: "+str(self.allEven))

            try:
                self.exN = round((self.allOdd / self.trial)/(self.allEven / self.trial),7)
            except:
                self.exN = 0

            self.trial += 1
            self.label_trial.setText("전체 시도 횟수 : "+str(self.trial))

            self.pOdd = round(self.allOdd / self.trial, 7)
            self.label_podd.setText("홀수 확률 : " + str(self.pOdd))
            self.pEven = round(self.allEven / self.trial,7)
            self.label_peven.setText("짝수 확률 : " + str(self.pEven))

            self.error = round((abs(self.exN - self.thN) * 100) / self.thN,7)

            self.label_exN.setText(": " + str(self.exN))
            self.label_thN.setText(": " + str(self.thN))
            self.label_error.setText(": " + str(self.error))


    def btn100_clicked(self):
        for i in range(0, 100):
            self.allOdd += self.calOdd(100)
            self.label_odd.setText("홀수 사건 횟수 : "+str(self.allOdd))
            self.allEven += self.calEven(100)
            self.label_even.setText("짝수 사건 횟수 : "+str(self.allEven))

            try:
                self.exN = round((self.allOdd / self.trial) / (self.allEven / self.trial), 7)
            except:
                self.exN = 0

            self.trial += 1
            self.label_trial.setText("전체 시도 횟수 : "+str(self.trial))

            self.pOdd = round(self.allOdd / self.trial, 7)
            self.label_podd.setText("홀수 확률 : " + str(self.pOdd))
            self.pEven = round(self.allEven / self.trial,7)
            self.label_peven.setText("짝수 확률 : " + str(self.pEven))

            self.error = round((abs(self.exN - self.thN) * 100) / self.thN,7)

            self.label_exN.setText(": " + str(self.exN))
            self.label_thN.setText(": " + str(self.thN))
            self.label_error.setText(": " + str(self.error))

    def btn1000_clicked(self):
        for i in range(0, 1000):
            self.allOdd += self.calOdd(1000)
            self.label_odd.setText("홀수 사건 횟수 : "+str(self.allOdd))
            self.allEven += self.calEven(1000)
            self.label_even.setText("짝수 사건 횟수 : "+str(self.allEven))

            try:
                self.exN = round((self.allOdd / self.trial) / (self.allEven / self.trial), 7)
            except:
                self.exN = 0

            self.trial += 1
            self.label_trial.setText("전체 시도 횟수 : "+str(self.trial))

            self.pOdd = round(self.allOdd / self.trial, 7)
            self.label_podd.setText("홀수 확률 : " + str(self.pOdd))
            self.pEven = round(self.allEven / self.trial,7)
            self.label_peven.setText("짝수 확률 : " + str(self.pEven))

            self.error = round((abs(self.exN - self.thN) * 100) / self.thN,7)

            self.label_exN.setText(": " + str(self.exN))
            self.label_thN.setText(": " + str(self.thN))
            self.label_error.setText(": " + str(self.error))

    def btndes_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setIconPixmap(self.des_resized)
        msg.setWindowTitle("공 뽑기")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def calOdd(self, trial):
        cnt = 0
        random.seed()
        ns = list()
        n = random.randrange(0, 29)

        self.label_eo.setText("홀수")
        self.pixmap_resized[0] = self.pixmap[0].scaled(45, 45, QtCore.Qt.KeepAspectRatio)
        self.label[0].setPixmap(self.pixmap_resized[0])
        self.label[0].resize(self.pixmap_resized[0].width(), self.pixmap_resized[0].height())
        for i in range(1, 29):
            self.pixmap_resized[i] = self.pixmap[i].scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            self.label[i].setPixmap(self.pixmap_resized[i])
            self.label[i].resize(self.pixmap_resized[i].width(), self.pixmap_resized[i].height())

        QtTest.QTest.qWait(5000 / trial / math.log10(trial))

        for i in range(14, 0, -1):
            # print(i)(
            n = random.randrange(0, 2 * i + 1)

            print(n)

            self.pixmap_resized[n].fill(Qt.transparent)
            self.label[n].setPixmap(self.pixmap_resized[n])
            self.label[n].resize(self.pixmap_resized[n].width(), self.pixmap_resized[n].height())

            QtTest.QTest.qWait(2000 / trial / math.log10(trial))

            if n == 0:
                break
            else:
                cnt += 1
                self.label_cnt.setText("뽑은 갯수 : " + str(cnt))

            self.pixmap_resized[n] = self.pixmap[n].scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            self.label[n].setPixmap(self.pixmap_resized[n])
            self.label[n].resize(self.pixmap_resized[n].width(), self.pixmap_resized[n].height())

            QtTest.QTest.qWait(2000 / trial / math.log10(trial))

            self.pixmap_resized[2*i].fill(Qt.transparent)
            self.label[2*i].setPixmap(self.pixmap_resized[2*i])
            self.label[2*i].resize(self.pixmap_resized[2*i].width(), self.pixmap_resized[2*i].height())
            self.pixmap_resized[2 * i-1].fill(Qt.transparent)
            self.label[2 * i-1].setPixmap(self.pixmap_resized[2 * i-1])
            self.label[2 * i-1].resize(self.pixmap_resized[2 * i-1].width(),self.pixmap_resized[2 * i-1].height())


        print()
        print("@@@@@@@@@", cnt)
        print()

        if cnt == 14:
            print("!!!!!!!!!!")
            return 1
        else:
            return 0


    def calEven(self, trial):
        cnt = 0
        random.seed()
        self.label_eo.setText("짝수")
        self.pixmap_resized[28].fill(Qt.transparent)
        self.label[28].setPixmap(self.pixmap_resized[28])
        self.pixmap_resized[0] = self.pixmap[0].scaled(45, 45, QtCore.Qt.KeepAspectRatio)
        self.label[0].setPixmap(self.pixmap_resized[0])
        self.label[0].resize(self.pixmap_resized[0].width(), self.pixmap_resized[0].height())
        for i in range(1, 28):
            self.pixmap_resized[i] = self.pixmap[i].scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            self.label[i].setPixmap(self.pixmap_resized[i])
            self.label[i].resize(self.pixmap_resized[i].width(), self.pixmap_resized[i].height())

        QtTest.QTest.qWait(5000 / trial / math.log10(trial))

        for i in range(14, 0, -1):
            # print(i)
            n = random.randrange(0, 2 * i)
            print(n)

            self.pixmap_resized[n].fill(Qt.transparent)
            self.label[n].setPixmap(self.pixmap_resized[n])
            self.label[n].resize(self.pixmap_resized[n].width(), self.pixmap_resized[n].height())

            QtTest.QTest.qWait(2000 / trial / math.log10(trial))


            if n == 0:
                break
            else:
                cnt += 1
                self.label_cnt.setText("뽑은 갯수 : " + str(cnt))

            self.pixmap_resized[n] = self.pixmap[n].scaled(40, 40, QtCore.Qt.KeepAspectRatio)
            self.label[n].setPixmap(self.pixmap_resized[n])
            self.label[n].resize(self.pixmap_resized[n].width(), self.pixmap_resized[n].height())

            QtTest.QTest.qWait(2000 / trial / math.log10(trial))

            self.pixmap_resized[2 * i-1].fill(Qt.transparent)
            self.label[2 * i-1].setPixmap(self.pixmap_resized[2 * i-1])
            self.label[2 * i-1].resize(self.pixmap_resized[2 * i-1].width(), self.pixmap_resized[2 * i-1].height())
            self.pixmap_resized[2 * i - 2].fill(Qt.transparent)
            self.label[2 * i - 2].setPixmap(self.pixmap_resized[2 * i - 2])
            self.label[2 * i - 2].resize(self.pixmap_resized[2 * i - 2].width(),
                                         self.pixmap_resized[2 * i - 2].height())

        print()
        print("@@@@@@@@@", cnt)
        print()

        if cnt == 14:
            print("!!!!!!!!!!")
            return 1
        else:
            return 0

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = BallWindow()
    myWindow.show()
    app.exec_()