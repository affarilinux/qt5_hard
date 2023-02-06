import psutil

from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_2,NUM_100

class Processador100(QMainWindow):
    
    def processador_frequencia ( self ):
    
        # chama os dados para a janela
        informacao_sistema_1 = psutil.cpu_freq ()

        # puxa as informações e adiciona nas variaveis
        maximo_processador   = informacao_sistema_1.max
        dados_presente       = informacao_sistema_1.current

         # calcula porcentagm
        calculo_processos_dados     = ( dados_presente * NUM_100 ) / maximo_processador

        # filtra o float
        self.filtra_calculo_sistema = round ( calculo_processos_dados, NUM_2 )

        self.BUTON_PROCESSADOR.setText("PROCESSADOR\n{} %".format(self.filtra_calculo_sistema))