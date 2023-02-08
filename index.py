import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import Qt
from PyQt5.QtGui      import QIcon

##VARIAVEIS
from variaveis_uni.numero import NUM_100
from variaveis_uni.palavra import truepal,falsepal
from variaveis_uni.universal import QICONE_BARRA_DE_TAREFA
##SISTEMA
from app_principal.fe import GuiFrontPrincipal
from app_principal.be_bateria import Bateria100
from app_principal.be_ram import BE_Ram
from app_principal.be_processador import Processador100
from app_principal.be_temperatura import Temperatura100
from app_principal.be_cooler      import CoolerAtivo

from fechar_janela.key import KeyBoard

from appsinit.init import SubJanela

from banco_dados.estruturabase import BancoDadosInit
from banco_dados.criartabela import CriarTabela
from banco_dados.verificacao import Verificacao

class Principal(
    GuiFrontPrincipal,Bateria100,BE_Ram,
    Processador100,Temperatura100,CoolerAtivo,
    KeyBoard,
    SubJanela,
    BancoDadosInit,CriarTabela,Verificacao,
    QMainWindow):

    def __init__(self):
        super(Principal, self).__init__()

        self.setAttribute(Qt.Qt.WA_TranslucentBackground, truepal )   
        self.setAttribute(Qt.Qt.WA_NoSystemBackground, falsepal)      
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setGeometry(1610, NUM_100, 250, 540) #j-XY app-XY
        self.setStyleSheet("Principal{background-color: rgba(0,255,255, 20);}") #Aqua / 
        
        self.setWindowIcon   ( QIcon ( QICONE_BARRA_DE_TAREFA ))   #icone da janela


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = Principal()
    p.show()
    app.exec_()
