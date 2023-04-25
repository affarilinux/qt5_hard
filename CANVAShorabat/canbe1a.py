from PyQt5.QtWidgets import QMainWindow

class Guicanvasbe1a(QMainWindow):

    def canvasbef1(self,pltt,cttoo,listtcar):

        '''listtcar = []
        
        for i in range(1,cttoo + 1):

            self.cursorsq.execute("SELECT tempo_carga,TEMPO_MEDIO FROM MEDIA_TEMPO  WHERE id_ex = ?",(i,))
            vgaa = self.cursorsq.fetchone()

            self.cursorsq.execute("SELECT VALOR_GRAFO FROM BATERIA_PC   WHERE ID_GRAFO = ?",(i,))
            SEI = self.cursorsq.fetchone()

            self.cursorsq.execute("SELECT BATER FROM BATER  WHERE ID_BATER = ?",(SEI[0],))
            VIDA = self.cursorsq.fetchone()

            print(vgaa,VIDA)
            SDD = vgaa[1] * VIDA[0]
            print(SDD)'''
            

            
            
            #listtcar.append(vgaa[0])

            ## usar dicionario para fazer a leitura

        x = range(1,cttoo + 1)
        
        line1 = pltt.plot(x, listtcar, pen='g', symbol='x', 
                         symbolPen='g', symbolBrush=0.2, symbolSize = 14,name='CARGA') 
        
        
      


        

        
       