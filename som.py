from PyQt5.QtWidgets import *
import sys 
import pyqtgraph as pg 
from PyQt5.QtGui import *
  
from PyQt5.QtCore import Qt 
  
  
class BarGraphItem(pg.BarGraphItem): 
  
    
    
    def __init__(self, *args, **kwargs): 
        pg.BarGraphItem.__init__(self, *args, **kwargs) 
  
    
    def mouseDoubleClickEvent(self, e): 
        self.setScale(0.2) 
  
  
class Window(QMainWindow): 
  
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("PyQtGraph") 
        self.setGeometry(100, 100, 600, 500) 
        icon = QIcon("skin.png") 
        self.setWindowIcon(icon) 
        self.UiComponents() 
        self.show() 
  
    
    def UiComponents(self): 
        widget = QWidget() 
        label = QLabel("GeeksforGeeks Line Plot") 
        label.setWordWrap(True) 
        y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
        y2 = [3, 1, 5, 8, 9, 11, 16, 17, 14, 16] 
        x = range(0, 10) 
        plt = pg.plot() 
        plt.showGrid(x=True, y=True) 
        plt.addLegend() 
        plt.setLabel('left', 'Vertical Values', units='y') 
        plt.setLabel('bottom', 'Horizontal Vlaues', units='s') 
        plt.setXRange(0, 20) 
        plt.setYRange(0, 20) 
        line1 = plt.plot(x, y, pen='g', symbol='x', 
                         symbolPen='g', symbolBrush=0.2, name='green') 
        line2 = plt.plot(x, y2, pen='b', symbol='o', 
                         symbolPen='b', symbolBrush=0.2, name='blue') 
        cursor = Qt.PointingHandCursor 
        line1.setCursor(cursor) 
        value = line1.cursor() 
        label.setText("Cursor : " + str(value)) 
        label.setMinimumWidth(120) 
        layout = QGridLayout() 
        widget.setLayout(layout) 
        layout.addWidget(label, 1, 0) 
        layout.addWidget(plt, 0, 1, 3, 1) 
        self.setCentralWidget(widget) 
  
  
App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 