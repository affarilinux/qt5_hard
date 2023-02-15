from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui      import QIcon
from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA

import pyqtgraph as pg

class Guicanvasfe(QMainWindow):

    def canvas(self):
        
        y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
        y2 = [3, 1, 5, 8, 9, 11, 16, 17, 14, 16] 
        y3 = [6, 1, 5, 10, 9, 3, 16, 6, 14, 27] 
        x = range(0, 10) 
        plt = pg.plot() 
        plt.showGrid(x=True, y=True) 
        plt.addLegend() 
        plt.setLabel('left', 'NÍVEL CARGA', units='%') 
        plt.setLabel('bottom', 'TEMPO', units='T') 
        plt.setXRange(0, 100) 
        plt.setYRange(0, 100) 
        plt.setWindowTitle( 'BATERIA' )
        plt.move(400,550)
        plt.resize(1000,350)
        plt.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela
        line1 = plt.plot(x, y, pen='g', symbol='x', 
                         symbolPen='g', symbolBrush=0.2, symbolSize = 14,name='Carregando') 
        line2 = plt.plot(x, y2, pen='b', symbol='o', 
                         symbolPen='b', symbolBrush=0.2, symbolSize = 14,name='descarregando') 
        line3 = plt.plot(x, y3, pen='w', symbol='+', 
                         symbolPen='w', symbolBrush=0.2, symbolSize = 14,name='MEDIA VIDA') 
        plt.show()
