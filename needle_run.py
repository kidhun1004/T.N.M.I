#-*-coding: utf-8-*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtTest
from PyQt5 import uic,QtCore,QtGui
import random
import math
import numpy as np
from mplwidget import MplWidget

form_class = uic.loadUiType("UI/needle.ui")[0]

class NeedleWindow(QMainWindow, form_class):
    tinterval = ''
    interval = 0
    tneedleLength = ''
    needleLength = 0
    th = 0
    thR = 0
    closeLine = 0
    trial = 0
    all = 0
    thN = round(math.pi,7)
    exN = 0
    prob = 0
    des = 0

    btncnt = True

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_10.clicked.connect(self.btn10_clicked)
        self.pushButton_100.clicked.connect(self.btn100_clicked)
        self.pushButton_1000.clicked.connect(self.btn1000_clicked)
        self.pushButton_des.clicked.connect(self.btndes_clicked)
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

        self.lineEdit_interval.returnPressed.connect(self.intervalChanged)
        self.lineEdit_length.returnPressed.connect(self.lengthChanged)

        self.des = QtGui.QPixmap('des/needle.PNG')
        self.des_resized = self.des.scaled(420,230)

        self.Mplwidget.canvas.draw()

        self.label_thN.setText(": "+str(self.thN))
        #self.label_thN.setText(":")

    def intervalChanged(self):
        try:
            self.interval = float(self.lineEdit_interval.text())
            #self.btncnt = False
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("실수만 입력해 주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        #self.tinterval = ''
        #self.lineEdit_interval.setText(self.tinterval)

        self.Mplwidget.canvas.axes.clear()
        self.all = 0
        self.trial = 0
        self.label_trial.setText(":")
        self.label_acnt.setText(":")
        self.label_prob.setText(":")

        self.label_exN.setText(":")
        self.label_error.setText(":")

        self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
        self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

        for i in range(0, 6):
            self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])

        self.Mplwidget.canvas.draw()

    def lengthChanged(self):
        try:
            self.needleLength = float(self.lineEdit_length.text())
            #self.btncnt = True
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("실수만 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        #self.tneedleLength = ''
        #self.lineEdit_length.setText(self.tneedleLength)

        self.Mplwidget.canvas.axes.clear()

        self.all = 0
        self.trial = 0
        self.label_trial.setText(":")
        self.label_acnt.setText(":")
        self.label_prob.setText(":")

        self.label_exN.setText(":")
        self.label_error.setText(":")

        self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
        self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

        for i in range(0, 6):
            self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])

        self.Mplwidget.canvas.draw()

    '''def btn0_clicked(self):
        if self.btncnt:
            self.tinterval += '0'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '0'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn1_clicked(self):
        if self.btncnt:
            self.tinterval += '1'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '1'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn2_clicked(self):
        if self.btncnt:
            self.tinterval += '2'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '2'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn3_clicked(self):
        if self.btncnt:
            self.tinterval += '3'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '3'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn4_clicked(self):
        if self.btncnt:
            self.tinterval += '4'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '4'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn5_clicked(self):
        if self.btncnt:
            self.tinterval += '5'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '5'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn6_clicked(self):
        if self.btncnt:
            self.tinterval += '6'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '6'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn7_clicked(self):
        if self.btncnt:
            self.tinterval += '7'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '7'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn8_clicked(self):
        if self.btncnt:
            self.tinterval += '8'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '8'
            self.lineEdit_length.setText(self.tneedleLength)
    def btn9_clicked(self):
        if self.btncnt:
            self.tinterval += '9'
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength += '9'
            self.lineEdit_length.setText(self.tneedleLength)
    def btnbs_clicked(self):
        if self.btncnt:
            self.tinterval = self.tinterval[:-1]
            self.lineEdit_interval.setText(self.tinterval)
        else:
            self.tneedleLength = self.tneedleLength[:-1]
            self.lineEdit_length.setText(self.tneedleLength)
    def btncf_clicked(self):
        if self.btncnt:
            try:
                self.interval = int(self.tinterval)
                self.btncnt = False
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("실수만 입력해 주세요")
                msg.setWindowTitle("경고!!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            self.tinterval = ''
            self.lineEdit_interval.setText(self.tinterval)

            self.Mplwidget.canvas.axes.clear()
            self.all = 0
            self.trial = 0
            self.label_trial.setText("총 시도 횟수 : ")
            self.label_acnt.setText("만난 횟수 : ")
            self.label_prob.setText("확률 : ")

            self.label_exN.setText("실험값 : ")
            self.label_error.setText("오차 : ")

            self.label_interval2.setText("줄사이 간격 : " + str(self.interval))
            print(self.interval)

            self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
            self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

            for i in range(0, 6):
                self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])

            self.Mplwidget.canvas.draw()
        else:
            try:
                self.needleLength = int(self.tneedleLength)
                self.btncnt = True
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("숫자를 입력해주세요")
                msg.setWindowTitle("경고!!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

            self.tneedleLength = ''
            self.lineEdit_length.setText(self.tneedleLength)

            self.Mplwidget.canvas.axes.clear()

            self.all = 0
            self.trial = 0
            self.label_trial.setText("총 시도 횟수 : ")
            self.label_acnt.setText("만난 횟수 : ")
            self.label_prob.setText("확률 : ")

            self.label_exN.setText("실험값 : ")
            self.label_error.setText("오차 : ")

            self.label_length2.setText("바늘 길이 : " + str(self.needleLength))
            print(self.interval)

            self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
            self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

            for i in range(0, 6):
                self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])

            self.Mplwidget.canvas.draw()'''


    def btn10_clicked(self):
        self.Mplwidget.canvas.axes.clear()
        self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
        self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

        for i in range(0, 6):
            self.Mplwidget.canvas.axes.plot([0, 5*self.interval], [i * self.interval, i * self.interval])

        QtTest.QTest.qWait(10)

        print(self.needleLength, self.interval)

        try:
            for i in range(10):
                self.all += self.cal(self.needleLength, self.interval)
                self.trial += 1
                self.prob = round(self.all / self.trial, 7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.prob))

                try:
                    self.exN = round((2 * self.needleLength) / ((self.prob) * self.interval),7)
                    self.label_exN.setText(": " + str(self.exN))
                    self.label_error.setText(": " + str(self.error))
                except:
                    self.label_exN.setText(": ")
                    self.label_error.setText(": ")

                QtTest.QTest.qWait(2)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("줄사이 간격과 바늘 길이 모두 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btn100_clicked(self):
        self.Mplwidget.canvas.axes.clear()
        self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
        self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

        for i in range(0, 6):
            self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])

        print(self.needleLength, self.interval)

        try:
            for i in range(100):
                self.all += self.cal(self.needleLength, self.interval)
                self.trial += 1
                self.prob = round(self.all / self.trial, 7)
                self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                self.label_trial.setText(": " + str(self.trial))
                self.label_acnt.setText(": " + str(self.all))
                self.label_prob.setText(": " + str(self.prob))

                try:
                    self.exN = round((2 * self.needleLength) / ((self.prob) * self.interval), 7)
                    self.label_exN.setText(": " + str(self.exN))
                    self.label_error.setText(": " + str(self.error))
                except:
                    self.label_exN.setText(": ")
                    self.label_error.setText(": ")

                QtTest.QTest.qWait(2)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("줄사이 간격과 바늘 길이 모두 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btn1000_clicked(self):
        self.Mplwidget.canvas.axes.clear()
        self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
        self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

        for i in range(0, 6):
            self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])

        print(self.needleLength, self.interval)

        try:
            for i in range(10):
                self.Mplwidget.canvas.axes.clear()
                self.Mplwidget.canvas.axes.set_xlim([0, 5 * self.interval])
                self.Mplwidget.canvas.axes.set_ylim([0, 5 * self.interval])

                for i in range(0, 6):
                    self.Mplwidget.canvas.axes.plot([0, 5 * self.interval], [i * self.interval, i * self.interval])
                for j in range(100):
                    self.all += self.cal(self.needleLength, self.interval)
                    self.trial += 1
                    self.prob = round(self.all / self.trial, 7)
                    self.error = round((abs(self.exN - self.thN) * 100) / self.thN, 7)
                    self.label_trial.setText(": " + str(self.trial))
                    self.label_acnt.setText(": " + str(self.all))
                    self.label_prob.setText(": " + str(self.prob))

                    try:
                        self.exN = round((2 * self.needleLength) / ((self.prob) * self.interval), 7)
                        self.label_exN.setText(": " + str(self.exN))
                        self.label_error.setText(": " + str(self.error))
                    except:
                        self.label_exN.setText(": ")
                        self.label_error.setText(": ")

                    QtTest.QTest.qWait(2)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("줄사이 간격과 바늘 길이 모두 입력해주세요")
            msg.setWindowTitle("경고!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def btndes_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setIconPixmap(self.des_resized)
        msg.setWindowTitle("뷔퐁의 바늘")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def cal(self, needleLength, interval):
        cnt = 0
        random.seed()
            #x,y,degree
        loc = [0, 0]
        loc[0] = (random.randrange(0, interval * 50000)) / 10000  # x
        loc[1] = (random.randrange(0, interval * 50000)) / 10000  # y
        th = (random.randrange(0, 1800000)) / 10000

        thR = math.radians(th)

        closeLine = ((loc[1] + (interval / 2)) // interval) * interval

        #draw
        p1 = [loc[0] - (needleLength/2) * np.cos(thR), loc[0] + (needleLength/2) * np.cos(thR)]
        p2 = [loc[1] - (needleLength/2) * np.sin(thR), loc[1] + (needleLength/2) * np.sin(thR)]

        self.Mplwidget.canvas.axes.plot(p1,p2)
        self.Mplwidget.canvas.draw()

        self.Mplwidget.canvas.axes.set_xlim([0, 5 * interval])
        self.Mplwidget.canvas.axes.set_ylim([0, 5 * interval])

        if abs((closeLine - loc[1])) <= ((needleLength / 2) * math.sin(thR)):
            return 1
        else:
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = NeedleWindow()
    myWindow.show()
    app.exec_()