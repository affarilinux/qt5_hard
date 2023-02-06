import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt

from app_principal.fe import GuiFrontPrincipal

from fechar_janela.key import KeyBoard

from appsinit.init import SubJanela
class Principal(
    GuiFrontPrincipal,
    KeyBoard,
    SubJanela,
    QMainWindow):

    def __init__(self):
        super(Principal, self).__init__()

        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, False)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1610, 100, 250, 540) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 20);}") #Aqua / Cyan


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()
