from PyQt5.QtWidgets import QMainWindow,QShortcut
from PyQt5.QtGui import QKeySequence

from variaveis_uni.numero import NUM_0,NUM_1

class KeyBoard(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo 

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(self.closeApp)

        self.shortcut_closer = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_closer.activated.connect(self.key_var_if)
  
    def closeApp(self):
        self.close()

    def key_var_if(self):

        if self.var_estado_bat == NUM_1:

            self.var_estado_bat = NUM_0
        
        elif self.var_estado_bat == NUM_0:
    
            self.var_estado_bat = NUM_1