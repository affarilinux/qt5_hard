
from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1
from variaveis_uni.ESTADO import none, truepal
class EXEC_bateria(QMainWindow):

    #####--------------------------------------------------------------
    def exec_procesos_carreagndo(self,pc,et):

        self.abc = none
        self.asb = none
        
        self.ativar_banco()

        self.cursorsq.execute("SELECT ID_GRAFO FROM BATERIA_PC   WHERE ID_GRAFO = ?",(NUM_1,))
        batpc = self.cursorsq.fetchone()

        if batpc == none:
            
            # inserir dados
            self.exec_inter_b1()
            self.commit_banco()
            
            self.asb = 1
            self.exec_inter_b2(pc,et)
            self.commit_banco()

        elif batpc != none:
            
            ### varificar se e para atualizar dados 
            self.cursorsq.execute("SELECT max(ID_GRAFO) FROM BATERIA_PC")
            m_batpc = self.cursorsq.fetchone()

            self.cursorsq.execute("SELECT VALOR_GRAFO,CA_DES FROM BATERIA_PC   WHERE ID_GRAFO = ?",(m_batpc[0],))
            mm_batpc = self.cursorsq.fetchone()

            self.cursorsq.execute(
                    """SELECT  BATER FROM BATER   
                    WHERE ID_BATER = ? """,(mm_batpc[0],))
            BP = self.cursorsq.fetchone()

            if pc > BP[0] or pc < BP[0]:

                ## estado da bateria 
                self.cursorsq.execute(
                    """SELECT  ESTADO_BATERIA  FROM ESTADO_BATERIA  
                    WHERE ID_ESTADO = ? """,(mm_batpc[1],))
                eb = self.cursorsq.fetchone()

                ## estado da bateria
                if et == eb[0]:

                    self.asb = 0

                    ### atualizar dados
                    self.cursorsq.execute("SELECT count(ID_GRAFO) FROM BATERIA_PC")
                    coou = self.cursorsq.fetchone()

                    ## 1 linha
                    if coou[0]  == 1:

                        self.exec_inter_b1()
                        self.commit_banco()

                        self.exec_inter_b2(pc,et)
                        self.commit_banco()

                    ## 2 ou + linhas
                    elif coou[0]  > 1:
    
                        self.cursorsq.execute("SELECT max(idc_num) FROM BATERIA_PC")
                        maxxy = self.cursorsq.fetchone()

                        self.cursorsq.execute("SELECT ID_GRAFO FROM BATERIA_PC   WHERE idc_num = ?",(maxxy[0],))
                        ma = self.cursorsq.fetchone()

                        ### numero indice idc estado
                        if ma[0] == m_batpc[0]:
                            
                            self.exec_inter_b1()
                            self.commit_banco()

                            self.exec_inter_b2(pc,et)
                            self.commit_banco()

                        elif ma[0] != m_batpc[0]:
                            
                            self.exec_inter_up()
                            self.commit_banco()

                            self.exec_upp(pc,et,m_batpc[0])
                            self.commit_banco()

                ### estado da bateria
                elif et != eb[0]:
                    
                    self.exec_inter_b1()
                    self.commit_banco()

                    self.cursorsq.execute("SELECT max(idc_num) FROM BATERIA_PC")
                    maxx = self.cursorsq.fetchone()

                    self.asb = maxx[0] + 1
                    self.exec_inter_b2(pc,et)
                    self.commit_banco()

        self.sair_banco()

    ###-----------------------------------------------------------------
    def exec_inter_b1(self):
         
        self.cursorsq.execute("SELECT ID_HORAS FROM HORAS   WHERE HORAS = ?",(self.hr,))
        HRR = self.cursorsq.fetchone()

        self.cursorsq.execute("SELECT ID_DATA FROM DATA_   WHERE DATA__ = ?",(self.hj,))
        DTT = self.cursorsq.fetchone()

        print(self.hj)

        ### FUNCAO INTERNA
        def ess(self,hrr,dtt):

            self.cursorsq.execute(
                """SELECT  ID_TEMPO FROM TEMPO   
                WHERE TEMPO_HORA == ? and TEMPO_DATA == ? """,(hrr,dtt))
            tb1 = self.cursorsq.fetchone()

            if tb1 == none:
                self.cursorsq.execute(
                        "INSERT INTO TEMPO(TEMPO_DATA,TEMPO_HORA ) VALUES (?,?)",(dtt,hrr))

            elif tb1 != none:    
                
                self.cursorsq.execute(
                    """SELECT  ID_TEMPO FROM TEMPO   
                    WHERE TEMPO_HORA == ? and TEMPO_DATA == ? """,(hrr,dtt))
                tb2 = self.cursorsq.fetchone()

                self.abc = tb2[0]
        
        ess(self,HRR[0],DTT[0])
        ess(self,HRR[0],DTT[0])

    def exec_inter_up(self):
         
        self.cursorsq.execute("SELECT ID_HORAS FROM HORAS   WHERE HORAS = ?",(self.hr,))
        HRR4u = self.cursorsq.fetchone()

        self.cursorsq.execute("SELECT ID_DATA FROM DATA_   WHERE DATA__ = ?",(self.hj,))
        DTT4u = self.cursorsq.fetchone()

        self.cursorsq.execute("SELECT max(idc_num) FROM BATERIA_PC")
        maxy = self.cursorsq.fetchone()

        self.cursorsq.execute(
                """UPDATE TEMPO SET TEMPO_HORA = ?, TEMPO_DATA = ? 
                WHERE ID_TEMPO = ?""",(HRR4u[0],DTT4u[0],maxy[0]))
        
        self.abc = maxy[0]
        
    ##--------------------------------------------
    def exec_inter_b2(self,pcc,ett):

        self.cursorsq.execute(
                    """SELECT  ID_BATER FROM BATER   
                    WHERE BATER = ? """,(pcc,))
        abc1 = self.cursorsq.fetchone()

        self.cursorsq.execute(
                    """SELECT  ID_ESTADO FROM ESTADO_BATERIA  
                    WHERE ESTADO_BATERIA = ? """,(ett,))
        abc2 = self.cursorsq.fetchone()
        
        self.cursorsq.execute(
                """INSERT INTO BATERIA_PC(idx_tempo,VALOR_GRAFO,CA_DES,idc_num ) 
                VALUES (?,?,?,?)""",(self.abc,abc1[0],abc2[0],self.asb))
        
    def exec_upp(self,pcc,ett,m_):
    
        
        self.cursorsq.execute(
                    """SELECT  ID_BATER FROM BATER   
                    WHERE BATER = ? """,(pcc,))
        abc1u = self.cursorsq.fetchone()

        self.cursorsq.execute(
                    """SELECT  ID_ESTADO FROM ESTADO_BATERIA  
                    WHERE ESTADO_BATERIA = ? """,(ett,))
        abc2u = self.cursorsq.fetchone()

        self.cursorsq.execute(
                """UPDATE BATERIA_PC SET idx_tempo = ?,VALOR_GRAFO = ?,CA_DES = ?,idc_num = ?
                WHERE ID_GRAFO = ?""",(self.abc,abc1u[0],abc2u[0],self.asb,m_))