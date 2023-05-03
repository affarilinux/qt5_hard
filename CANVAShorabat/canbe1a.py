from PyQt5.QtWidgets import QMainWindow

class Guicanvasbe1a(QMainWindow):

    def canvasbef1(self,pltt,cttoo,listtcar):

        
        x = range(1,cttoo + 1)
        
        line1 = pltt.plot(x, listtcar, pen='g', symbol='x', 
                         symbolPen='g', symbolBrush=0.2, symbolSize = 14,name='CARGA') 
        
        
      


        

        
       