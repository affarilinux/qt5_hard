from PyQt5.QtWidgets import QMainWindow,QShortcut
from PyQt5.QtGui import QKeySequence

class KeyBoard(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo 

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(self.closeApp)
  
    def closeApp(self):
        self.close()