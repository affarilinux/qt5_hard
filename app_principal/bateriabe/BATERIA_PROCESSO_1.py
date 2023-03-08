import time
from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_1
from variaveis_uni.ESTADO import none
class EXEC_bateria_1(QMainWindow):

    def salvar_tb_temporaria(self,bt):

        self.ativar_banco()

        self.cursorsq.execute("SELECT ID_GRAFO FROM BATERIA_PC   WHERE ID_GRAFO = ?",(NUM_1,))
        nom = self.cursorsq.fetchone()

        if nom != none:

            def salvar_tbt(self,nu,bty,secc):

                A = []
                
                self.cursorsq.execute("SELECT MEDIA_INT,MEDIA_SECOND FROM MEDIA  WHERE ID_MEDIA = ?",(nu,))
                demm = self.cursorsq.fetchone()

                if demm == none:

                    self.cursorsq.execute(
                    "INSERT INTO MEDIA(ID_MEDIA,MEDIA_INT,MEDIA_SECOND) VALUES(?,?,?)",(nu,bty,secc))
            
                    self.commit_banco()

                    A.append(bty)
                    A.append(secc)
                    return A
                else:

                    A.append(demm[0])
                    A.append(demm[1])
                    return A
                    
                
            def salvar_tbt_2(self,sa0,sa1,idi):

                self.cursorsq.execute(
                """UPDATE MEDIA SET MEDIA_INT = ?, MEDIA_SECOND = ? 
                WHERE ID_MEDIA = ?""",(sa0,sa1,idi))

                self.commit_banco()

            seconds = int(time.time())

            salvar_tbt(self,1,bt,seconds)
            sall = salvar_tbt(self,2,bt,seconds)

            if bt > sall[0] or bt < sall[0]:

                if self.var__intervalo == 0:

                    salvar_tbt_2(self, bt,seconds,1)
                    salvar_tbt_2(self,bt,seconds,2)

                    self.var__intervalo = 1

                elif self.var__intervalo == 1:
                
                    salvar_tbt_2(self, sall[0],sall[1],1)
                    salvar_tbt_2(self,bt,seconds,2)

        self.sair_banco()
