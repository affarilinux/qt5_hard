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
        
        def ya_1(self,ie,mm,TM):

            self.cursorsq.execute("SELECT id_ex FROM MEDIA_TEMPO  WHERE id_ex = ?",(ie,))
            bidet = self.cursorsq.fetchone()

            if bidet == none:

                self.cursorsq.execute(
                        "INSERT INTO MEDIA_TEMPO(id_ex,tempo_carga,TEMPO_MEDIO) VALUES(?,?,?)",(ie,mm,TM))
                
            elif bidet != none:
    
                self.cursorsq.execute(
                        "UPDATE MEDIA_TEMPO SET tempo_carga = ?, TEMPO_MEDIO = ? WHERE id_ex = ?",(mm,TM,ie))
            
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

        self.cursorsq.execute("SELECT COUNT(id_ex) FROM MEDIA_TEMPO")
        CN = self.cursorsq.fetchone()

        yya = ya_(self,1)
        yyb = ya_(self,2)

        if yya[0] == yyb[0]:

            
            if CN[0] == 0 or CN[0] == 1:
                uy = convert_to_preferred_format(vgaya[0])
                ya_1(self,maxya[0], uy,0)

            elif CN[0] > 1:
                
                tarr0 = maxya[0] - 1
                
                self.cursorsq.execute("SELECT TEMPO_MEDIO FROM MEDIA_TEMPO  WHERE id_ex = ?",(tarr0,))
                MA = self.cursorsq.fetchone()

                
                tarr = MA[0]

                if MA[0] == 0:

                    tarr1 = vgaya[0]

                elif MA[0] != 0:
                    
                    if ttdes == "ca":

                        tarr1 = (100 - vgaya[0]) * tarr
                        
                    elif ttdes == "des":
                    
                        tarr1 = vgaya[0] * tarr

                uy1 = convert_to_preferred_format(tarr1)

                ya_1(self,maxya[0], uy1,tarr)

        elif yya[0] != yyb[0]:
            
            if yya[0] > yyb[0]:
    
                tarefa = yya[0] - yyb[0]

            elif yya[0] < yyb[0]:
                tarefa = yyb[0] - yya[0]

            tarefa1 = yyb[1] - yya[1]

            tarefa2 = int(tarefa1 / tarefa)

            self.cursorsq.execute("SELECT CA_DES FROM BATERIA_PC  WHERE ID_GRAFO = ?",(maxya[0],))
            ca_des = self.cursorsq.fetchone()

            self.cursorsq.execute("SELECT ESTADO_BATERIA FROM ESTADO_BATERIA  WHERE ID_ESTADO = ?",(ca_des[0],))
            ca_des1 = self.cursorsq.fetchone()

            if ca_des1[0] == "ca":
                tarefa3 = (100 - vgaya[0]) * tarefa2

            elif ca_des1[0] == "des":
                tarefa3 = vgaya[0] * tarefa2
                
            uy1 = convert_to_preferred_format(tarefa3)

            ya_1(self,maxya[0], uy1,tarefa1)

        self.commit_banco()
        self.sair_banco()

