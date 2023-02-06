from PyQt5.QtWidgets import QMainWindow
import psutil


##VARIAVEIS
from variaveis_uni.numero import NUM_100

class BE_Ram(QMainWindow):
    
    def ps_ram(self):

        #informações da memoria ram
        informacao           = psutil.virtual_memory ()

        # puxa as informações e adiciona nas variaveis
        total                = informacao.total
        usada                = informacao.active

        # calcula porcentagm
        calculo_por_centagem      = ( usada * NUM_100 ) / total

        # filtra o float
        calculo_filtro_informacao = round ( calculo_por_centagem, 2 )

        self.BUTON_RAM.setText("RAM\n {} %".format(calculo_filtro_informacao))