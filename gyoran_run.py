#-*-coding: utf-8-*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtCore,QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtTest
import numpy
import random
from PyQt5.QtCore import Qt

form_class = uic.loadUiType("UI/gyoran.ui")[0]

class GyoranWindow(QMainWindow, form_class):
    all = 0
    trial = 0
    thN = round(1/numpy.e,7)
    exN = 0
    error = 0

    pixmap = list(range(10))
    pixmap_resized = list(range(10))
    label = list(range(10))

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = [QtGui.QPixmap('cards_png_zip/PNG\SA.png'), QtGui.QPixmap('cards_png_zip/PNG/S2.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S3.png'), QtGui.QPixmap('cards_png_zip/PNG/S4.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S5.png'), QtGui.QPixmap('cards_png_zip/PNG/S6.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S7.png'), QtGui.QPixmap('cards_png_zip/PNG/S8.png'),
                  QtGui.QPixmap('cards_png_zip/PNG/S9.png'), QtGui.QPixmap('cards_png_zip/PNG/S10.png')]

        self.label = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                 self.label_8, self.label_9, self.label_10]

        self.des = QtGui.QPixmap('des/gyoran.PNG')
        self.des_resized = self.des.scaled(420,230)

        self.label_exN.setText(": "+str(self.thN))
        self.pushButton_10.clicked.connect(self.btn10_clicked)
        self.pushButton_100.clicked.connect(self.btn100_clicked)
        self.pushButton_1000.clicked.connect(self.btn1000_clicked)
        self.pushButton_des.clicked.connect(self.btndes_clicked)

    def btn10_clicked(self):
        for i in range(0,10):
            self.all += self.cal(10)
            self.trial += 1
            self.exN = round(self.all/self.trial,7)
            self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
            self.label_trial.setText(": "+str(self.trial))
            self.label_acnt.setText(": "+str(self.all))
            self.label_prob.setText(": " + str(self.exN))
            self.label_error.setText(": "+str(self.error))

    def btn100_clicked(self):
        for i in range(0,100):
            self.all += self.cal(100)
            self.trial += 1
            self.exN = round(self.all / self.trial, 7)
            self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
            self.label_trial.setText(": " + str(self.trial))
            self.label_acnt.setText(": " + str(self.all))
            self.label_prob.setText(": " + str(self.exN))
            self.label_error.setText(": " + str(self.error))

    def btn1000_clicked(self):
        for i in range(0,1000):
            self.all += self.cal(1000)
            self.trial += 1
            self.exN = round(self.all / self.trial, 7)
            self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
            self.label_trial.setText(": " + str(self.trial))
            self.label_acnt.setText(": " + str(self.all))
            self.label_prob.setText(": " + str(self.exN))
            self.label_error.setText(": " + str(self.error))
        
    def cal(self, num):
        cnt = 0
        n = list(range(0,10))
        random.seed()

        for i in range(0, 10):
            self.pixmap_resized[i] = self.pixmap[i].scaled(90, 90, QtCore.Qt.KeepAspectRatio)

        random.shuffle(n)

        for i in range(0, 10):
            if n[i] != i:
                cnt = cnt + 1

        for i in range(0,10):
            self.label[i].setPixmap(self.pixmap_resized[int(n[i])])
            self.label[i].resize(self.pixmap_resized[int(n[i])].width(), self.pixmap_resized[int(n[i])].height())
            self.show()

        QtTest.QTest.qWait(3000 / num)

        for i in range(0,10):
            if n[i] == i:
                self.pixmap_resized[int(n[i])].fill(Qt.transparent)

            self.label[i].setPixmap(self.pixmap_resized[int(n[i])])
            self.label[i].resize(self.pixmap_resized[int(n[i])].width(), self.pixmap_resized[int(n[i])].height())
            self.show()

        QtTest.QTest.qWait(3000 / num)

        print(n, cnt)
        print()

        if cnt == 10:
            return 1
        else:
            return 0

    def btndes_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setIconPixmap(self.des_resized)
        msg.setWindowTitle("교란순열")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = GyoranWindow()
    myWindow.show()
    app.exec_()