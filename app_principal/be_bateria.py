import psutil
from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.palavra import falsepal,truepal,none
class Bateria100(QMainWindow):

    def chamada_qtimerbateria(self):

        #---------------------------------------------------------------
        # chama os dados para a janela
        BATERIA_sistema = psutil.sensors_battery()

        # chama o tipo de informação
        nivel_bateria   = BATERIA_sistema.percent

        # transforma em int
        entrada_informacao = int(nivel_bateria)

        #---------------------------------------------------------------
        # puxa os dado do sistema operacional
        informacao_bateria = psutil.sensors_battery()

        # puxa uma informação se esta plugado na internet
        informacao_carregamento = informacao_bateria.power_plugged 
        est = none

        if informacao_carregamento   == truepal :
                
               est = "ca"
                
        elif informacao_carregamento == falsepal :
                est = "des"
        
        #---------------------------------------------------------------
        # chama a janela'
        self.BUTON_BATERIA.setText(
            "BATERIA\n{} 00:00\n{} %".format(est,entrada_informacao))

       
       