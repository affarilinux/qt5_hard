import psutil

from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1,NUM_2,NUM_3,NUM_100
from variaveis_uni.PALAVRA import PROCESSADOR_LT

class Processador100(QMainWindow):

    def __init__( self ):
        
        super ().__init__() # metodo

        self.var_ppc = NUM_0
    
    def processador_frequencia ( self ):
    
        # chama os dados para a janela
        informacao_sistema_1 = psutil.cpu_freq ()

        if not informacao_sistema_1:

            self.BUTON_PROCESSADOR.setText("Processador\n S\I")

        else:

            # puxa as informações e adiciona nas variaveis
            maximo_processador   = informacao_sistema_1.max
            dados_presente       = informacao_sistema_1.current

            # calcula porcentagm
            calculo_processos_dados     = ( dados_presente * NUM_100 ) / maximo_processador        

            # filtra o float
            filtra_calculo_sistema = round ( calculo_processos_dados, NUM_2 )

            ##---------------------------------------------------------------------
            self.ativar_banco()
            
            self.cursorsq.execute("SELECT PROC_MIN,PROC_MAX,PROC_APRESENTAR FROM  PROCESSADOR  WHERE ID_PROC = ?",(NUM_1,))
            PRC = self.cursorsq.fetchone()

            if PRC[NUM_2] == NUM_1:

                if filtra_calculo_sistema >= PRC[NUM_1]:

                    self.var_ppc = self.var_ppc + NUM_1

                    if self.var_ppc == NUM_1:

                        self.BUTON_PROCESSADOR.setText("{}\n ++ {} %".format(PROCESSADOR_LT,PRC[NUM_1]))

                        self.funcao_if_son()

                    elif self.var_ppc != NUM_1:

                        self.proc_apresentar(filtra_calculo_sistema)

                        if self.var_ppc == NUM_3:
                            self.var_ppc = NUM_0

                elif filtra_calculo_sistema <= PRC[NUM_1]:
        
                    self.proc_apresentar(filtra_calculo_sistema)
                    self.zero_var_ppc()

            elif PRC[NUM_2] == NUM_0:

                self.proc_apresentar(filtra_calculo_sistema)
                self.zero_var_ppc()
                
            self.commit_banco()
            self.sair_banco()

    def zero_var_ppc(self):

        if self.var_ppc != NUM_0:

            self.var_ppc = NUM_0
    def proc_apresentar(self,fcs):

        self.BUTON_PROCESSADOR.setText("{}\n{} %".format(PROCESSADOR_LT,fcs))


        

       