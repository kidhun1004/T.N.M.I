#-*-coding: utf-8-*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from carddraw_run import CardWindow
from gyoran_run import GyoranWindow
from coupon_run import CouponWindow
from needle_run import NeedleWindow
from ball_run import BallWindow

form_class = uic.loadUiType("UI/mainwindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_carddraw.clicked.connect(self.btncarddraw_clicked)
        self.pushButton_gyoran.clicked.connect(self.btngyoran_clicked)
        self.pushButton_coupon.clicked.connect(self.btncoupon_clicked)
        self.pushButton_needle.clicked.connect(self.btnneedle_clicked)
        self.pushButton_ball.clicked.connect(self.btnball_clicked)

    def btncarddraw_clicked(self):
        self.ui = CardWindow()
        self.ui.show()

    def btngyoran_clicked(self):
        self.ui = GyoranWindow()
        self.ui.show()

    def btncoupon_clicked(self):
        self.ui = CouponWindow()
        self.ui.show()

    def btnneedle_clicked(self):
        self.ui = NeedleWindow()
        self.ui.show()

    def btnball_clicked(self):
        self.ui = BallWindow()
        self.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()