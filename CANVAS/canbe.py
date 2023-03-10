from PyQt5.QtWidgets import QMainWindow

class Guicanvasbe(QMainWindow):

    def canvasbe(self,pltt):

        y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
        y2 = [3, 1, 5, 8, 9, 11, 16, 17, 14, 16] 
        x = range(0, 10) 

        line1 = pltt.plot(x, y, pen='g', symbol='x', 
                         symbolPen='g', symbolBrush=0.2, symbolSize = 14,name='CARGA') 
        line2 = pltt.plot(x, y2, pen='b', symbol='o', 
                         symbolPen='b', symbolBrush=0.2, symbolSize = 14,name='MEDIA DE CARGA') 
       