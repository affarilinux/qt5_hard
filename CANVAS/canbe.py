from PyQt5.QtWidgets import QMainWindow

class Guicanvasbe(QMainWindow):

    def canvasbe(self,pltt,cttoo):

        listtcar = []
        
        for i in range(1,cttoo + 1):

            self.cursorsq.execute("SELECT VALOR_GRAFO FROM BATERIA_PC  WHERE ID_GRAFO = ?",(i,))
            vgaa = self.cursorsq.fetchone()
            
            self.cursorsq.execute("SELECT BATER FROM BATER  WHERE ID_BATER = ?",(vgaa[0],))
            btzz = self.cursorsq.fetchone()
            
            listtcar.append(btzz[0])

        x = range(1,cttoo + 1)
        
        line1 = pltt.plot(x, listtcar, pen='g', symbol='x', 
                         symbolPen='g', symbolBrush=0.2, symbolSize = 14,name='CARGA') 
        
        
      


        

        
       