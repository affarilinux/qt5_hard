import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

from variaveis_uni.numero import NUM_0,NUM_1

class AvisoSon(QMainWindow):

    def __init__(self):

        super ().__init__() # metodo

        self.var_aviso_son = NUM_0

    def aviso_son(self):

        if self.var_aviso_son == NUM_1:

            self.player = QMediaPlayer()

            full_file_path = os.path.join(os.getcwd(), 'variaveis_uni/jk.mp3')
            url = QUrl.fromLocalFile(full_file_path)
            content = QMediaContent(url)

            self.player.setMedia(content)
            self.player.play()

            self.var_aviso_son = NUM_0


    def funcao_if_son(self):

         ## sinal de aviso tocar
            if self.var_aviso_son == NUM_0:
                self.var_aviso_son =NUM_1