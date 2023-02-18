import os

from PyQt5.QtWidgets import QMainWindow
from pydub import AudioSegment
from pydub.playback import play



from variaveis_uni.numero import NUM_0,NUM_1

class AvisoSon(QMainWindow):

    def __init__(self):

        super ().__init__() # metodo

        self.var_aviso_son = NUM_0

    def aviso_son(self):

        if self.var_aviso_son == NUM_1:

            sound = AudioSegment.from_file(file = 'variaveis_uni/jk.wav', format = "wav")
            play(sound)

            self.var_aviso_son = NUM_0
        
    def funcao_if_son(self):

         ## sinal de aviso tocar
            if self.var_aviso_son == NUM_0:
                self.var_aviso_son =NUM_1