#-*-coding: utf-8-*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtTest
import numpy
import math
import random

form_class = uic.loadUiType("UI/carddraw.ui")[0]

class CardWindow(QMainWindow, form_class):
    all = 0
    trial = 0
    thN = 1 / numpy.e
    exN = 0
    n = 0
    error = 0
    tn = ''

    pixmap = list(range(53))
    pixmap_resized = list(range(53))
    pixmap_back = [0]
    pixmap_back_resized = [0]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap_back[0] = QtGui.QPixmap('cards_png_zip/PNG/blue_back.png')
        self.pixmap_back_resized[0] = self.pixmap_back[0].scaled(190, 190, QtCore.Qt.KeepAspectRatio)

        self.pixmap = [0, QtGui.QPixmap('cards_png_zip/PNG/SA.png'), QtGui.QPixmap('cards_png_zip/PNG/S2.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S3.png'), QtGui.QPixmap('cards_png_zip/PNG/S4.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S5.png'), QtGui.QPixmap('cards_png_zip/PNG/S6.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S7.png'), QtGui.QPixmap('cards_png_zip/PNG/S8.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S9.png'), QtGui.QPixmap('cards_png_zip/PNG/S10.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/SJ.png'), QtGui.QPixmap('cards_png_zip/PNG/SQ.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/SK.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/DA.png'), QtGui.QPixmap('cards_png_zip/PNG/D2.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/D3.png'), QtGui.QPixmap('cards_png_zip/PNG/D4.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/D5.png'), QtGui.QPixmap('cards_png_zip/PNG/D6.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/D7.png'), QtGui.QPixmap('cards_png_zip/PNG/D8.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/D9.png'), QtGui.QPixmap('cards_png_zip/PNG/D10.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/DJ.png'), QtGui.QPixmap('cards_png_zip/PNG/DQ.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/DK.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/HA.png'), QtGui.QPixmap('cards_png_zip/PNG/H2.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/H3.png'), QtGui.QPixmap('cards_png_zip/PNG/H4.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/H5.png'), QtGui.QPixmap('cards_png_zip/PNG/H6.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/H7.png'), QtGui.QPixmap('cards_png_zip/PNG/H8.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/H9.png'), QtGui.QPixmap('cards_png_zip/PNG/H10.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/HJ.png'), QtGui.QPixmap('cards_png_zip/PNG/HQ.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/HK.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/CA.png'), QtGui.QPixmap('cards_png_zip/PNG/C2.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/C3.png'), QtGui.QPixmap('cards_png_zip/PNG/C4.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/C5.png'), QtGui.QPixmap('cards_png_zip/PNG/C6.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/C7.png'), QtGui.QPixmap('cards_png_zip/PNG/C8.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/C9.png'), QtGui.QPixmap('cards_png_zip/PNG/C10.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/CJ.png'), QtGui.QPixmap('cards_png_zip/PNG/CQ.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/CK.png')]

        for i in range(1, 53):
            self.pixmap_resized[i] = self.pixmap[i].scaled(190, 190, QtCore.Qt.KeepAspectRatio)

        self.label_back.resize(self.pixmap_back_resized[0].width(), self.pixmap_back_resized[0].height())
        self.label_back.setPixmap(self.pixmap_back_resized[0])
        self.thN = round(1 / math.e,7)
        self.label_exN.setText(": " + str(self.thN))

        self.pushButton_10.clicked.connect(self.btn10_clicked)
        self.pushButton_100.clicked.connect(self.btn100_clicked)
        self.pushButton_1000.clicked.connect(self.btn1000_clicked)
        self.pushButton_des.clicked.connect(self.btndes_clicked)

        self.des = QtGui.QPixmap('des/card.PNG')
        self.des_resized = self.des.scaled(420,230)

        self.lineEdit.returnPressed.connect(self.lineEditChanged)
        '''self.pushButton_bs.clicked.connect(self.btnbs_clicked)
        self.pushButton_0.clicked.connect(self.btn0_clicked)
        self.pushButton_cf.clicked.connect(self.btncf_clicked)
        self.pushButton_1.clicked.connect(self.btn1_clicked)
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        self.pushButton_3.clicked.connect(self.btn3_clicked)
        self.pushButton_4.clicked.connect(self.btn4_clicked)
        self.pushButton_5.clicked.connect(self.btn5_clicked)
        self.pushButton_6.clicked.connect(self.btn6_clicked)
        self.pushButton_7.clicked.connect(self.btn7_clicked)
        self.pushButton_8.clicked.connect(self.btn8_clicked)
        self.pushButton_9.clicked.connect(self.btn9_clicked)'''

    '''def btn0_clicked(self):
        self.tn += '0'
        self.lineEdit.setText(self.tn)
    def btn1_clicked(self):
        self.tn += '1'
        self.lineEdit.setText(self.tn)
    def btn2_clicked(self):
        self.tn += '2'
        self.lineEdit.setText(self.tn)
    def btn3_clicked(self):
        self.tn += '3'
        self.lineEdit.setText(self.tn)
    def btn4_clicked(self):
        self.tn += '4'
        self.lineEdit.setText(self.tn)
    def btn5_clicked(self):
        self.tn += '5'
        self.lineEdit.setText(self.tn)
    def btn6_clicked(self):
        self.tn += '6'
        self.lineEdit.setText(self.tn)
    def btn7_clicked(self):
        self.tn += '7'
        self.lineEdit.setText(self.tn)
    def btn8_clicked(self):
        self.tn += '8'
        self.lineEdit.setText(self.tn)
    def btn9_clicked(self):
        self.tn += '9'
        self.lineEdit.setText(self.tn)
    def btnbs_clicked(self):
        self.tn = self.tn[:-1]
        self.lineEdit.setText(self.tn)
    def btncf_clicked(self):
        self.all = 0
        self.trial = 0
        shape = ""
        num = ""
        self.label_trial.setText("총 시도 횟수 : ")
        self.label_acnt.setText("못뽑은 횟수 : ")
        self.label_prob.setText("못뽑을 확률 : ")
        self.label_error.setText("오차 : ")
        try:
            self.n = int(self.tn)
            self.tn = ''
            self.lineEdit.setText(self.tn)
            if self.n > 52 or self.n <= 0:
                1 / 0

            if (self.n - 1) // 13 == 0:
                shape = "스페이드"
            elif (self.n - 1) // 13 == 1:
                shape = "다이아몬드"
            elif (self.n - 1) // 13 == 2:
                shape = "하트"
            else:
                shape = "클로버"

            if self.n - ((self.n // 13) * 13) >= 2 and self.n - ((self.n // 13) * 13) <= 10:
                num = str(self.n - (self.n // 13) * 13)
            elif self.n - (self.n // 13) * 13 == 1:
                num = "에이스"
            elif self.n - (self.n // 13) * 13 == 11:
                num = "J"
            elif self.n - (self.n // 13) * 13 == 12:
                num = "Q"
            else:
                num = "K"

            self.label_n.setText("못뽑아야할 숫자 : " + str(self.n) + "(" + shape + " " + num + ")")
            self.thN = 1 / math.e
            self.label_exN.setText("이론값 : " + str(self.thN))

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("1~52사이 정수만 입력해 주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.n = 0
            self.label_n.setText("못뽑아야할 숫자 : ")
        print(self.n)'''

    def lineEditChanged(self):
        self.all = 0
        self.trial = 0
        shape = ""
        num = ""
        self.label_trial.setText(":")
        self.label_acnt.setText(":")
        self.label_prob.setText(":")
        self.label_error.setText(":")
        try:
            #self.n = int(self.tn)
            #self.tn = ''
            #self.lineEdit.setText(self.tn)
            self.n = int(self.lineEdit.text())
            if self.n > 52 or self.n <= 0:
                1 / 0

            if (self.n - 1) // 13 == 0:
                shape = "스페이드"
            elif (self.n - 1) // 13 == 1:
                shape = "다이아몬드"
            elif (self.n - 1) // 13 == 2:
                shape = "하트"
            else:
                shape = "클로버"

            if self.n - ((self.n // 13) * 13) >= 2 and self.n - ((self.n // 13) * 13) <= 10:
                num = str(self.n - (self.n // 13) * 13)
            elif self.n - (self.n // 13) * 13 == 1:
                num = "에이스"
            elif self.n - (self.n // 13) * 13 == 11:
                num = "J"
            elif self.n - (self.n // 13) * 13 == 12:
                num = "Q"
            else:
                num = "K"

            self.label_n.setText("선택한 카드 : " + str(self.n) + "(" + shape + " " + num + ")")

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("1~52사이 정수만 입력해 주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.n = 0
            self.label_n.setText("못뽑아야할 숫자 : ")

    def btn10_clicked(self):
        try:
            1/self.n
            for i in range(0, 10):
                self.all += self.cal(10)
                self.trial += 1
                self.exN = round(self.all / self.trial,7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN,7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.exN))
                self.label_error.setText(": " + str(self.error))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("못뽑아야할 숫자를 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btn100_clicked(self):
        try:
            1/self.n
            for i in range(0, 100):
                self.all += self.cal(100)
                self.trial += 1
                self.exN = round(self.all / self.trial, 7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.exN))
                self.label_error.setText(": " + str(self.error))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("못뽑아야할 숫자를 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btn1000_clicked(self):
        try:
            1/self.n
            for i in range(0, 1000):
                self.all += self.cal(1000)
                self.trial += 1
                self.exN = round(self.all / self.trial, 7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.exN))
                self.label_error.setText(": " + str(self.error))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("못뽑아야할 숫자를 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btndes_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setIconPixmap(self.des_resized)
        msg.setWindowTitle("카드 뽑기")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def cal(self,nu):
        cnt = 0
        random.seed()
        for i in range(0, 52):
            num = random.randrange(1, 53)
            self.label_cnt.setText(str(i+1))

            self.label_front.resize(self.pixmap_back_resized[0].width(), self.pixmap_back_resized[0].height())
            self.label_front.setPixmap(self.pixmap_back_resized[0])
            QtTest.QTest.qWait(500 / nu)
            self.label_front.resize(self.pixmap_resized[num].width(), self.pixmap_resized[num].height())
            self.label_front.setPixmap(self.pixmap_resized[num])
            QtTest.QTest.qWait(500 / nu)

            #print(num)
            if num != self.n:
                cnt = cnt+1
            else:
                QtTest.QTest.qWait(1000 / nu)
                break

        QtTest.QTest.qWait(1000 / nu)

        if cnt == 52:
            return 1
        else:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = CardWindow()
    myWindow.show()
    app.exec_()