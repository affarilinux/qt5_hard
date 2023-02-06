from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtCore        import QTimer

##VARIAVEIS
from variaveis_uni.numero import (NUM_5,NUM_100,NUM_110,
    NUM_130,NUM_120,NUM_140)

class GuiFrontPrincipal(QMainWindow):
    
    def __init__( self ):
    
        super ().__init__() # metodo
        

        qtimer_front = QTimer        ( self )

        qtimer_front.setInterval     ( 5000 )
        qtimer_front.start           ()

        #chamada de funçãO
        qtimer_front.timeout.connect ( self.be_app_principal ) 


        ## sistema fixo

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("HARDWARE")
        LABEL_MAIN_FIXO.move(50,NUM_5)
        LABEL_MAIN_FIXO.resize(145,40)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 25px}')# YELLOW
        
        #dfgg = "BATERIA\nca 00:00\n 100 %"
        self.BUTON_BATERIA = QPushButton( self) 
        self.BUTON_BATERIA.setGeometry(NUM_110, 60,NUM_130,NUM_130) 
        self.BUTON_BATERIA.setStyleSheet("border-radius : 65;  color: #FFFF00; font: bold; font-size: 22px;border : 5px solid #FFFF00")
        self.BUTON_BATERIA.clicked.connect(self.clickme) 

        #dfgg1 = "RAM\n100 %"
        self.BUTON_RAM = QPushButton(self) 
        self.BUTON_RAM.setGeometry(10, 150, NUM_120, NUM_120) 
        self.BUTON_RAM.setStyleSheet("border-radius : 60;  color: #FFFF00; font: bold; font-size: 25px;border : 3px solid #FFFF00")
        self.BUTON_RAM.clicked.connect(self.j_b) 

        #dfgg2 = "TEMPERATURA \nMEDIA\n100 ºC"
        self.BUTON_TM = QPushButton( self) 
        self.BUTON_TM.setGeometry(NUM_100, 230,NUM_140, NUM_140) 
        self.BUTON_TM.setStyleSheet("border-radius : 70;  color: #FFFF00; font: bold; font-size: 16px;border : 4px solid #FFFF00")
        #BUTON_BATERIA.clicked.connect(self.clickme) 

        #dfgg3 = "PROCESSADOR\n100 %"
        self.BUTON_PROCESSADOR = QPushButton( self) 
        self.BUTON_PROCESSADOR.setGeometry(10, 330, NUM_120, NUM_120) 
        self.BUTON_PROCESSADOR.setStyleSheet("border-radius : 60;  color: #FFFF00; font: bold; font-size: 14px;border : 5px solid #FFFF00")
        #BUTON_BATERIA.clicked.connect(self.clickme) 

        #dfgg4 = "COOLER\n 4500 RPM"
        self.BUTON_COOLER = QPushButton( self) 
        self.BUTON_COOLER.setGeometry(NUM_110, 410, NUM_120, NUM_120) 
        self.BUTON_COOLER.setStyleSheet("border-radius : 60;  color: #FFFF00; font: bold; font-size: 21px;border : 2px solid #FFFF00")
        #BUTON_BATERIA.clicked.connect(self.clickme) 

        LABEL_MAIN_FIXO = QLabel(self)
        LABEL_MAIN_FIXO.setText("ctrl+Q sair")
        LABEL_MAIN_FIXO.move(NUM_5,520)
        LABEL_MAIN_FIXO.resize(60,20)
        LABEL_MAIN_FIXO.setStyleSheet('QLabel{color: #FFFF00; font: bold; font-size: 11px}')# YELLOW_

        self.be_app_principal()
    def clickme(self): 
  
        print("pressed") 

    def be_app_principal(self):
        self.chamada_qtimerbateria()        
        self.ps_ram()
        self.processador_frequencia()
        self.temperatura_lib()
        self.leitura_fans()


        
