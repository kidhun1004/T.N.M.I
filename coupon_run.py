#-*-coding: utf-8-*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtTest
import numpy
import math
import random

form_class = uic.loadUiType("UI/coupon.ui")[0]


class CouponWindow(QMainWindow, form_class):
    all = 0
    trial = 0
    exN = 0
    n = 0
    error = 0
    tn = ''

    pixmap = list(range(10))
    pixmap_resized = list(range(10))
    pixmap_back = [0]
    pixmap_back_resized = [0]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = [QtGui.QPixmap('cards_png_zip/PNG/SA.png'), QtGui.QPixmap('cards_png_zip/PNG/S2.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S3.png'), QtGui.QPixmap('cards_png_zip/PNG/S4.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S5.png'), QtGui.QPixmap('cards_png_zip/PNG/S6.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S7.png'), QtGui.QPixmap('cards_png_zip/PNG/S8.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S9.png'), QtGui.QPixmap('cards_png_zip/PNG/S10.png')]
        self.pixmap_resized = list(range(10))
        for i in range(0, 10):
            self.pixmap_resized[i] = self.pixmap[i].scaled(160, 160, QtCore.Qt.KeepAspectRatio)

        self.pixmap_back[0] = QtGui.QPixmap('cards_png_zip/PNG/gray_back.png')
        self.pixmap_back_resized[0] = self.pixmap_back[0].scaled(160, 160, QtCore.Qt.KeepAspectRatio)
        self.label_back.resize(self.pixmap_back_resized[0].width(), self.pixmap_back_resized[0].height())
        self.label_back.setPixmap(self.pixmap_back_resized[0])

        self.pushButton_10.clicked.connect(self.btn10_clicked)
        self.pushButton_100.clicked.connect(self.btn100_clicked)
        self.pushButton_1000.clicked.connect(self.btn1000_clicked)
        self.pushButton_des.clicked.connect(self.btndes_clicked)

        self.des = QtGui.QPixmap('des/coupon.PNG')
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
        self.pushButton_9.clicked.connect(self.btn9_clicked)

    def btn0_clicked(self):
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
        gamma = 0.57721
        self.all = 0
        self.trial = 0
        self.label_trial.setText("총 시도 횟수 : ")
        self.label_acnt.setText("뽑은 횟수 : ")
        self.label_prob.setText("평균 뽑은 횟수 : ")
        self.label_error.setText("오차 : ")
        try:    
            self.n = int(self.tn)
            self.tn = ''
            self.lineEdit.setText(self.tn)
            if self.n > 10 or self.n < 0:
                1/0
            self.label_n.setText("쿠폰 개수 : "+str(self.n))
            self.thN = self.n*(math.log(self.n))+gamma*self.n+0.5
            self.label_exN.setText("이론값 : " + str(self.thN))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("1~10사이 정수만 입력해 주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.n = 0
            self.label_n.setText("쿠폰 개수 : ")
        print(self.n)'''

    def lineEditChanged(self):
        gamma = 0.57721
        self.all = 0
        self.trial = 0
        self.label_trial.setText(": ")
        self.label_acnt.setText(": ")
        self.label_prob.setText(": ")
        self.label_error.setText(": ")
        try:
            self.n = int(self.lineEdit.text())
            if self.n > 10 or self.n < 0:
                1 / 0
            self.label_n.setText("쿠폰 개수 : " + str(self.n))
            self.thN = round(self.n * (math.log(self.n)) + gamma * self.n + 0.5,7)
            self.label_exN.setText(": " + str(self.thN))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("1~10사이 정수만 입력해 주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.n = 0
            self.label_n.setText("쿠폰 개수 : ")

    def btn10_clicked(self):
        try:
            1/self.n
            for i in range(0,10):
                self.all += self.cal(10,self.n)
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
            msg.setText("쿠폰 개수를 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btn100_clicked(self):
        try:
            1/self.n
            for i in range(0,100):
                self.all += self.cal(100,self.n)
                self.trial += 1
                self.exN = round(self.all / self.trial,7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.exN))
                self.label_error.setText(": " + str(self.error))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("쿠폰 개수를 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btn1000_clicked(self):
        try:
            1/self.n
            for i in range(0,1000):
                self.all += self.cal(1000,self.n)
                self.trial += 1
                self.exN = round(self.all / self.trial,7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.exN))
                self.label_error.setText(": " + str(self.error))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("쿠폰 개수를 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btndes_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setIconPixmap(self.des_resized)
        msg.setWindowTitle("쿠폰 콜렉터")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def listCheck(self,len,n):
        count = 0
        for i in range(0,len):
            if(n[i]==""):
                count += 1
        if(count == len):
            return False
        else:
            return True

    def cal(self,num,a):
        cnt = 0
        random.seed()
        n=list()
        for i in range(1,a+1):
            n.append(i)

        while self.listCheck(len(n),n) :
            nu = random.randrange(0, a)
            print(nu)
            self.label_front.resize(self.pixmap_back_resized[0].width(), self.pixmap_back_resized[0].height())
            self.label_front.setPixmap(self.pixmap_back_resized[0])
            QtTest.QTest.qWait(1000 / num)
            self.label_front.resize(self.pixmap_resized[nu].width(), self.pixmap_resized[nu].height())
            self.label_front.setPixmap(self.pixmap_resized[nu])
            QtTest.QTest.qWait(1000 / num)

            text = "남은 숫자:"
            for i in range(0, a):
                text = text + str(n[i]) + " "
            self.label_cnt.setText(str(text))

            n[nu]=""
            print(n)
            cnt += 1

        text = "남은 숫자:"
        for i in range(0, a):
            text = text + str(n[i]) + " "
        self.label_cnt.setText(str(text))

        QtTest.QTest.qWait(1500/num)

        print()

        return cnt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = CouponWindow()
    myWindow.show()
    app.exec_()