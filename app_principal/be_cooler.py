import psutil

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore        import QTimer

from variaveis_uni.palavra import none
class CoolerAtivo(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo construtor

        qtimer_fans = QTimer        ( self )

        qtimer_fans.setInterval     ( 100000 )
        qtimer_fans.start           ()

        #chamada de funçãO
        qtimer_fans.timeout.connect ( self.leitura_fans ) 

    def leitura_fans(self):
        fans_leiint = psutil.sensors_fans()
        fans_sis = none

        if not fans_leiint:
            fans_sis = "COOLER\n S\I"

        else: 
            fans_sis = "COOLER\n C\I"
            
        self.BUTON_COOLER.setText("{}".format(fans_sis))