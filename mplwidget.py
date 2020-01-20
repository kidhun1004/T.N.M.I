#-*-coding: utf-8-*-

from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as mpl

class MplWidget(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self,parent)
        self.canvas = FigureCanvas(Figure())
        mpl.rcParams.update({'font.size' : 7})

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(1,1,1)
        self.setLayout(vertical_layout)