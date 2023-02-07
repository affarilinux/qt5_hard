from PyQt5.QtWidgets import QMainWindow

class SubJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.j_bateria = Janela_bateria()

    def j_b(self):
        self.j_bateria.show()
##----------------------------------------------------------------------
# /home/waghtom/Downloads/CTRL-C/envs/QT5_hard/qt5_hard/appsinit/init.py (python
from app_ram.fe2 import GUIFe2Ram

class Janela_bateria(
    GUIFe2Ram,
    QMainWindow):
    
    def __init__(self):
        super(Janela_bateria, self).__init__()        

        self.setGeometry(600, 200, 500, 300) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("HARDWARE-RAM")



        