import time
from PyQt5.QtWidgets import QMainWindow

class BateriaBD(QMainWindow):

    def bat_tb_bd(self,pc,std):

        self.ativar_banco()

        
        self.commit_banco()
        self.sair_banco()