from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5.QtGui      import QIcon
from PyQt5 import QtWidgets, QtCore

from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA

import pyqtgraph as pg

class Guicanvasfe1a(QMainWindow):

    def canvas1a(self):

        self.ativar_banco()

        self.cursorsq.execute("SELECT count(ID_GRAFO) FROM BATERIA_PC")
        a1ctto = self.cursorsq.fetchone()

        listtcar = []
        sdffi = 0
        
        for i in range(1,a1ctto[0] + 1):

            self.cursorsq.execute("SELECT tempo_carga,TEMPO_MEDIO FROM MEDIA_TEMPO  WHERE id_ex = ?",(i,))
            vgaa = self.cursorsq.fetchone()

            self.cursorsq.execute("SELECT VALOR_GRAFO FROM BATERIA_PC   WHERE ID_GRAFO = ?",(i,))
            SEI = self.cursorsq.fetchone()

            self.cursorsq.execute("SELECT BATER FROM BATER  WHERE ID_BATER = ?",(SEI[0],))
            VIDA = self.cursorsq.fetchone()

            SDD = vgaa[1] * VIDA[0]
            
            listtcar.append(SDD)
            
            if SDD >= sdffi:

                sdffi = SDD

        self.plt = pg.plot()
        
        self.plt.showGrid(x=True, y=True) 
        self.plt.addLegend() 
        self.plt.setLabel('left', 'NÍVEL CARGA', units='%') 
        self.plt.setLabel('bottom', 'TEMPO', units='T') 
        self.plt.setXRange(0, a1ctto[0]) 
        self.plt.setYRange(0, sdffi)
        self.plt.setWindowTitle( 'BATERIA' )
        self.plt.move(400,550)
        self.plt.resize(1000,400)
        self.plt.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela

        self.canvasbef1(self.plt,a1ctto[0],listtcar)

        #funcao
        self.add_label()
        self.add_line()
        self.set_proxy()
        
        self.plt.show()
        
        self.commit_banco()
        self.sair_banco()

    def add_label (self):

        self.labele = pg.TextItem(text="X: {} \nY: {}".format(0, 0),anchor=(-0,6))
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

            self.ativar_banco()

            self.cursorsq.execute("SELECT count(ID_GRAFO) FROM BATERIA_PC")
            ct = self.cursorsq.fetchone()

            zeta = int(point.x())
            
            if zeta >= 1 and zeta <= ct[0]:
                
                self.cursorsq.execute("SELECT TEMPO_DATA FROM TEMPO  WHERE ID_TEMPO = ?",(zeta,))
                vga = self.cursorsq.fetchone()

                self.cursorsq.execute("SELECT DATA__ FROM DATA_  WHERE ID_DATA = ?",(vga[0],))
                vga1 = self.cursorsq.fetchone()

                self.cursorsq.execute("SELECT tempo_carga FROM  MEDIA_TEMPO WHERE ID_MEDIA_TEMPO = ?",(zeta,))
                vga2 = self.cursorsq.fetchone()

                xx ="DATA:{}, TEMPO:{}".format(vga1[0],vga2[0])
                yy = int(point.y())

            else:

                xx = float("{0:.3f}".format(point.x()))
                yy = float("{0:.3f}".format(point.y()))

            self.sair_banco()

            self.labele.setHtml(
                """<p style='color: #FFFF00;font-size: 11pt; font-family: Arial;font-weight: bold'>
                Y： {0} <br> X: {1}</p>""".format(yy,xx))

            self.vertical_line.setPos(point.x())
            self.horizontal_line.setPos(point.y())
       

            
