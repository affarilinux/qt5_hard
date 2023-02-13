from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui      import QIcon

from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA
from variaveis_uni.PALAVRA import (RAM_LT,HARDWARE_LT,
    TEMPERATURA_LT,PROCESSADOR_LT)
from variaveis_uni.numero import NUM_200,NUM_300,NUM_500,NUM_600

class SubJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.j_bateria = Janela_bateria()
        self.J_TEMPERATURA =Janela_Temperatura()
        self.J_PROCESSADOR = Janela_Processador()
        

    def j_b(self):
        self.j_bateria.show()

    def j_t (self):

        self.J_TEMPERATURA.show()

    def J_P(self):
        self.J_PROCESSADOR.show()

##----------------------------------------------------------------------
# /home/waghtom/Downloads/CTRL-C/envs/QT5_hard/qt5_hard/appsinit/init.py (python
from APPS.app_ram.fe2 import GUIFe2Ram
from APPS.app_ram.backe_ram import BeRam

from banco_dados.estruturabase import BancoDadosInit

class Janela_bateria(
    GUIFe2Ram,
    BancoDadosInit,
    BeRam,
    QMainWindow):
    
    def __init__(self):
        super(Janela_bateria, self).__init__()        

        self.setGeometry(NUM_600, NUM_200, NUM_500, NUM_300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("{}-{}".format(HARDWARE_LT,RAM_LT))

        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela

##---------------------------------------------------------------------------
##----------------------------------------------------------------------

from APPS.app_temperatura.backe_temp import BeTemperatura
from APPS.app_temperatura.fe3 import GUIFe2Temperatura

from banco_dados.estruturabase import BancoDadosInit

class Janela_Temperatura(
    BancoDadosInit
    ,BeTemperatura,
    GUIFe2Temperatura,
    QMainWindow):
    
    def __init__(self):
        super(Janela_Temperatura, self).__init__()        

        self.setGeometry(NUM_600, NUM_200, NUM_500, NUM_300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("{}-{}".format(HARDWARE_LT,TEMPERATURA_LT))

        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela

##---------------------------------------------------------------------------
##----------------------------------------------------------------------

from APPS.app_processador.backe_PROCESSADOR import BeProcessador
from APPS.app_processador.fe4 import GUIFe2Processador

from banco_dados.estruturabase import BancoDadosInit

class Janela_Processador(
    BancoDadosInit
    ,BeProcessador,
    GUIFe2Processador,
    QMainWindow):
    
    def __init__(self):
        super(Janela_Processador, self).__init__()        

        self.setGeometry(NUM_600, NUM_200, NUM_500, NUM_300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("{}- {}".format(HARDWARE_LT,PROCESSADOR_LT))

        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela




        