from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.ESTADO import none
class EXEC_bateria_2(QMainWindow):

    def funcao_tb_MEDIA_TEMPO(self,ttdes):

        self.ativar_banco()

        def ya_(self,nn):

            B = []

            self.cursorsq.execute("SELECT MEDIA_INT,MEDIA_SECOND FROM MEDIA  WHERE ID_MEDIA = ?",(nn,))
            bid = self.cursorsq.fetchone()

            B.append(bid[0])
            B.append(bid[1])

            return B 
        
        def ya_1(self,ie,mm):

            self.cursorsq.execute("SELECT id_ex FROM MEDIA_TEMPO  WHERE id_ex = ?",(ie,))
            bidet = self.cursorsq.fetchone()

            if bidet == none:

                self.cursorsq.execute(
                        "INSERT INTO MEDIA_TEMPO(id_ex,tempo_carga) VALUES(?,?)",(ie,mm))
                
            elif bidet != none:
    
                self.cursorsq.execute(
                        "UPDATE MEDIA_TEMPO SET tempo_carga = ? WHERE id_ex = ?",(mm,ie))
            
            self.commit_banco()

        def convert_to_preferred_format(sec): 

            sec = sec % (24 * 3600)
            hour = sec // 3600
            sec %= 3600
            min = sec // 60
            sec %= 60
            return "%02d:%02d:%02d" % (hour, min, sec)    


        self.cursorsq.execute("SELECT max(ID_GRAFO) FROM BATERIA_PC")
        maxya = self.cursorsq.fetchone()

        self.cursorsq.execute("SELECT VALOR_GRAFO FROM BATERIA_PC  WHERE ID_GRAFO = ?",(maxya[0],))
        vga = self.cursorsq.fetchone()

        self.cursorsq.execute("SELECT BATER FROM BATER  WHERE ID_BATER = ?",(vga[0],))
        vgaya = self.cursorsq.fetchone()

        yya = ya_(self,1)
        yyb = ya_(self,2)

        if yya[0] == yyb[0]:

            uy = convert_to_preferred_format(vgaya[0])
            ya_1(self,maxya[0], uy)

        elif yya[0] != yyb[0]:
            
            if yya[0] > yyb[0]:
    
                tarefa = yya[0] - yyb[0]

            elif yya[0] < yyb[0]:
                tarefa = yyb[0] - yya[0]

            tarefa1 = yyb[1] - yya[1]

            tarefa2 = int(tarefa1 / tarefa)

            if ttdes == "ca":
                tarefa3 = (100 - vgaya[0]) * tarefa2

            elif ttdes == "des":
                tarefa3 = vgaya[0] * tarefa2

            uy1 = convert_to_preferred_format(tarefa3)

            ya_1(self,maxya[0], uy1)

        self.commit_banco()
        self.sair_banco()

