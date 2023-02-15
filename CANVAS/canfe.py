from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui      import QIcon

from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA

import pyqtgraph as pg

class Guicanvasfe(QMainWindow):

    '''def __init__( self ):
        
        super ().__init__() # metodo '''

    def canvas(self):
         #.graphWidget = ImageView()
        #self.graphWidget = pg.PlotWidget()
        #self.graphWidget.setBackground('w')
        #self.graphWidget.move(NUM_100,100)
        #self.graphWidget.resize(100,100)
        #self.graphWidget.setLabel('left', 'TEMPERATURA', 'ºC')
        #self.graphWidget.setLabel('bottom', 'TEM

       

        self.graphWidget = pg.PlotWidget()
        #self.setCentralWidget(self.graphWidget)
        
        self.graphWidget.move(400,550)
        self.graphWidget.resize(1000,350)

        self.canvasbe(self.graphWidget)
        
        self.graphWidget.show()
