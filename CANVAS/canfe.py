from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui      import QIcon
from PyQt5 import QtWidgets, QtCore

from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA

import pyqtgraph as pg

class Guicanvasfe(QMainWindow):

    def canvas(self):

        self.xt = range(0, 10)
        self.plt = pg.plot()
        
        self.plt.showGrid(x=True, y=True) 
        self.plt.addLegend() 
        self.plt.setLabel('left', 'NÍVEL CARGA', units='%') 
        self.plt.setLabel('bottom', 'TEMPO', units='T') 
        self.plt.setXRange(0, 100) 
        self.plt.setYRange(0, 100) 
        self.plt.setWindowTitle( 'BATERIA' )
        self.plt.move(400,550)
        self.plt.resize(1000,400)
        self.plt.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela

        self.canvasbe(self.plt)

        #funcao
        self.add_label()
        self.add_line()
        self.set_proxy()
        
        self.plt.show()
        
    def add_label (self):

        self.labele = pg.TextItem(text="X: {} \nY: {}".format(0, 0),anchor=(-1,5))
        self.plt.addItem(self.labele)
    
    def add_line(self):

        self.vertical_line = pg.InfiniteLine(angle=90, movable=False, pen=pg.mkPen('#fff', width=1))
        self.horizontal_line = pg.InfiniteLine(angle=0, movable=False, pen=pg.mkPen('#fff', width=1))

        self.plt.addItem(self.vertical_line, ignoreBounds=True)
        self.plt.addItem(self.horizontal_line, ignoreBounds=True)

    def set_proxy(self):
    
        self.setMouseTracking(True)
        self.plt.scene().sigMouseMoved.connect(self.onMouseMoved)

    def onMouseMoved(self, evt):
        
        if self.plt.plotItem.vb.mapSceneToView(evt):
            point = self.plt.plotItem.vb.mapSceneToView(evt)
            xx = float("{0:.3f}".format(point.x()))
            yy = float("{0:.3f}".format(point.y()))
            self.labele.setHtml(
                """<p style='color: #FFFF00;font-size: 11pt; font-family: Arial;font-weight: bold'>
                X： {0} <br> Y: {1}</p>""".format(xx,yy))

            self.vertical_line.setPos(point.x())
            self.horizontal_line.setPos(point.y())

            
