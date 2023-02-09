from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui      import QIcon

from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA
from variaveis_uni.PALAVRA import RAM_LT

class SubJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.j_bateria = Janela_bateria()

    def j_b(self):
        self.j_bateria.show()
##----------------------------------------------------------------------
# /home/waghtom/Downloads/CTRL-C/envs/QT5_hard/qt5_hard/appsinit/init.py (python
from app_ram.fe2 import GUIFe2Ram
from banco_dados.estruturabase import BancoDadosInit
from app_ram.backe_ram import BeRam

class Janela_bateria(
    GUIFe2Ram,
    BancoDadosInit,
    BeRam,
    QMainWindow):
    
    def __init__(self):
        super(Janela_bateria, self).__init__()        

        self.setGeometry(600, 200, 500, 300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("HARDWARE-{}".format(RAM_LT))

        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela




        