'''import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout
from playsound import playsound

class App(QWidget):
from PyQt5.QtMultimedia import QSound

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Press Ctrl + O', self)

        self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.on_open)

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(self.closeApp) # or lambda : app.quit()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.resize(150, 150)

    def on_open(self):
       
        self.meusom = QSound("jk.mp3")
        self.meusom.play()

    def closeApp(self):
        self.meuson.stop()
app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())       

#qsound.stop() # 停止'''

'''from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()'''

'''from PyQt5 import QtWidgets  # Should work with PyQt5 / PySide2 / PySide6 as well
import pyqtgraph as pg

## Always start by initializing Qt (only once per application)
app = QtWidgets.QApplication([])

## Define a top-level widget to hold everything
w = QtWidgets.QWidget()
w.setWindowTitle('PyQtGraph example')

## Create some widgets to be placed inside
btn = QtWidgets.QPushButton('press me')
text = QtWidgets.QLineEdit('enter text')
listw = QtWidgets.QListWidget()
plot = pg.PlotWidget()

## Create a grid layout to manage the widgets size and position
layout = QtWidgets.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)  # button goes in upper-left
layout.addWidget(text, 1, 0)  # text edit goes in middle-left
layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows
## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec()  # or app.exec_() for PyQt5 / PySide2'''

# -*- coding: utf-8 -*-
"""
Demonstrates a way to put multiple axes around a single plot. 

(This will eventually become a built-in feature of Plosatem)

"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QListWidget, QVBoxLayout, QMainWindow
import pyqtgraph as pg


class Draw_interface(QMainWindow):
    def __init__(self):
        global time_update

        super(Draw_interface, self).__init__()
        uic.loadUi('charts.ui', self)

        # Add two charts
        self.my_draw = pg.GraphicsLayoutWidget(show=True)
        self.p1 = self.my_draw.addPlot(row=0, col=0, stretch=3)
        self.p2 = self.my_draw.addPlot(row=1, col=0, stretch=1)

        # Set widget for chart
        my_layout = QVBoxLayout()
        my_layout.addWidget(self.my_draw)
        self.frame_for_charts.setLayout(my_layout)

        # Draw charts
        y = [2.2, 3.0, 1.3, 2.5, 1.9, 2.2, 5.5, 6.6]
        y2 = [2.3, 3.3, 2.8, 2.2, 3.3, 3.1, 2.8, 4.4]
        curve1 = self.p1.plot(y)
        curve2 = self.p2.plot(y2)

        self.show()

my_app = QtWidgets.QApplication([])
my_main_window = Draw_interface()
sys.exit(my_app.exec_())