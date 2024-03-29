from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui      import QIcon

from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA
from variaveis_uni.PALAVRA import (RAM_LT,HARDWARE_LT,
    TEMPERATURA_LT,PROCESSADOR_LT,BATERIA_LT)
from variaveis_uni.numero import NUM_200,NUM_300,NUM_500,NUM_600

from banco_dados.estruturabase import BancoDadosInit

class SubJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.j_RAM = Janela_bateriaRam()
        self.J_TEMPERATURA =Janela_Temperatura()
        self.J_PROCESSADOR = Janela_Processador()
       
        #RAM
    def j_b(self):
        self.j_RAM.show()

    def j_t (self):

        self.J_TEMPERATURA.show()

    def J_P(self):
        self.J_PROCESSADOR.show()

        #BATERIA
    def J_B(self):
        self.J_bateria = Janela_Bateria()
        self.J_bateria.show()

    def inicial_grafo(self):
        
        self.grafo = Janela_grafico()

    def inicial_grafico1z(self):
        self.grafo1z = Janela_grafico1z()
        
##----------------------------------------------------------------------
# /home/waghtom/Downloads/CTRL-C/envs/QT5_hard/qt5_hard/appsinit/init.py (python
from APPS.app_ram.fe2 import GUIFe2Ram
from APPS.app_ram.backe_ram import BeRam

class Janela_bateriaRam(
    GUIFe2Ram,
    BancoDadosInit,
    BeRam,
    QMainWindow):
    
    def __init__(self):
        super(Janela_bateriaRam, self).__init__()        

        self.setGeometry(NUM_600, NUM_200, NUM_500, NUM_300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("{}-{}".format(HARDWARE_LT,RAM_LT))

        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela

##---------------------------------------------------------------------------
##----------------------------------------------------------------------

from APPS.app_temperatura.backe_temp import BeTemperatura
from APPS.app_temperatura.fe3 import GUIFe2Temperatura


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

from APPS.app_bateria.backe_bateria import BeBateria
from APPS.app_bateria.fe5 import GUIFe2Bateria
from banco_dados.apagar_dados import ApagarDados

class Janela_Bateria(
    BancoDadosInit
    ,BeBateria,GUIFe2Bateria,ApagarDados,
    QMainWindow):
    
    def __init__(self):
        super(Janela_Bateria, self).__init__()        

        self.setGeometry(NUM_600, NUM_200, 600, 300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("{}- {}".format(HARDWARE_LT,BATERIA_LT))

        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela


from CANVAS.canfe import Guicanvasfe
from CANVAS.canbe import Guicanvasbe

class Janela_grafico(
    BancoDadosInit,
    Guicanvasfe,Guicanvasbe,
    QMainWindow):
    
    def __init__(self):
        super(Janela_grafico, self).__init__()        

        self.canvas()

from CANVAShorabat.canfe1a import Guicanvasfe1a
from CANVAShorabat.canbe1a import Guicanvasbe1a

class Janela_grafico1z(
    BancoDadosInit,
    Guicanvasfe1a,Guicanvasbe1a,
    QMainWindow):
    
    def __init__(self):
        super(Janela_grafico1z, self).__init__()        

        self.canvas1a()

        




        