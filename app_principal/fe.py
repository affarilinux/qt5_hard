from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel,QShortcut
from PyQt5.QtCore        import QTimer
from PyQt5.QtGui import QKeySequence

class GuiFrontPrincipal(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo 

        ## sistema fixo

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("HARDWARE")
        LABEL_MAIN_FIXO.move(50,5)
        LABEL_MAIN_FIXO.resize(145,40)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 25px}')# YELLOW
        
        dfgg = "BATERIA\nca 00:00\n 100 %"
        BUTON_BATERIA = QPushButton(dfgg, self) 
        BUTON_BATERIA.setGeometry(110, 60, 130, 130) 
        BUTON_BATERIA.setStyleSheet("border-radius : 65;  color: #FFFF00; font: bold; font-size: 22px;border : 5px solid #FFFF00")
        BUTON_BATERIA.clicked.connect(self.clickme) 

        dfgg1 = "RAM\n100 %"
        BUTON_RAM = QPushButton(dfgg1, self) 
        BUTON_RAM.setGeometry(10, 150, 120, 120) 
        BUTON_RAM.setStyleSheet("border-radius : 60;  color: #FFFF00; font: bold; font-size: 25px;border : 3px solid #FFFF00")
        BUTON_RAM.clicked.connect(self.j_b) 

        dfgg2 = "TEMPERATURA \nMEDIA\n100 ºC"
        BUTON_TM = QPushButton(dfgg2, self) 
        BUTON_TM.setGeometry(100, 230, 140, 140) 
        BUTON_TM.setStyleSheet("border-radius : 70;  color: #FFFF00; font: bold; font-size: 16px;border : 4px solid #FFFF00")
        #BUTON_BATERIA.clicked.connect(self.clickme) 

        dfgg3 = "PROCESSADOR\n100 %"
        BUTON_PROCESSADOR = QPushButton(dfgg3, self) 
        BUTON_PROCESSADOR.setGeometry(10, 330, 120, 120) 
        BUTON_PROCESSADOR.setStyleSheet("border-radius : 60;  color: #FFFF00; font: bold; font-size: 14px;border : 5px solid #FFFF00")
        #BUTON_BATERIA.clicked.connect(self.clickme) 

        dfgg4 = "COOLER\n 4500 RPM"
        BUTON_COOLER = QPushButton(dfgg4, self) 
        BUTON_COOLER.setGeometry(110, 410, 120, 120) 
        BUTON_COOLER.setStyleSheet("border-radius : 60;  color: #FFFF00; font: bold; font-size: 21px;border : 2px solid #FFFF00")
        #BUTON_BATERIA.clicked.connect(self.clickme) 

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("ctrl+q sair")
        LABEL_MAIN_FIXO.move(5,520)
        LABEL_MAIN_FIXO.resize(60,20)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 11px}')# YELLOW_
    
    def clickme(self): 
  
        print("pressed") 