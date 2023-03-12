import sys
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg


class Draw_interface(QtWidgets.QMainWindow):
    def __init__(self):

        super(Draw_interface, self).__init__()
  
        # Add two charts
        p1 = pg.PlotWidget(name = "Plot1")
        p2 = pg.PlotWidget(name = "Plot2")
        
        # Draw charts
        y = [2.2, 3.0, 1.3, 2.5, 1.9, 2.2, 5.5, 6.6]
        y2 = [2.3, 3.3, 2.8, 2.2, 3.3, 3.1, 2.8, 4.4]
        p1.plot(y)
        p2.plot(y2)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(p1, stretch=2)
        l.addWidget(p2, stretch=2)

        w = QtWidgets.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)
        self.setStyleSheet("QWidget { background-color: black; }")
    
def main():
    QtWidgets.QApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    
    main = Draw_interface()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()