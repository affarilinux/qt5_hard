from PyQt5.QtWidgets import (QMainWindow, QLabel,
                QPushButton,QSpinBox,QCheckBox)


from variaveis_uni.numero import (NUM_1,NUM_20,NUM_30,NUM_50,
NUM_100,NUM_150,NUM_220)

class GUIFe2Ram(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo 
        
        self.SPINR2_MINIMO = QSpinBox(self)
        self.SPINR2_MINIMO.move(NUM_100,NUM_50)
        self.SPINR2_MINIMO.resize(NUM_100,NUM_30)
        self.SPINR2_MINIMO.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.SPINR2_MINIMO.setMaximum(NUM_100)
        self.SPINR2_MINIMO.setMinimum(NUM_1)
        #self.spin.valueChanged.connect(self.widget_processador121)


        LABEL_INFO_M = QLabel(self)
        LABEL_INFO_M.move(NUM_220,52)
        LABEL_INFO_M.setText("MINIMO")
        LABEL_INFO_M.resize(NUM_100,NUM_20)
        LABEL_INFO_M.setStyleSheet('QLabel{; font: bold;font-size: 20px}')# 

        self.spinr2_2 = QSpinBox(self)
        self.spinr2_2.move(NUM_100,NUM_100)
        self.spinr2_2.resize(NUM_100,NUM_30)
        self.spinr2_2.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.spinr2_2.setMaximum(NUM_100)
        self.spinr2_2.setMinimum(NUM_1)

        LABEL_INFO_Max = QLabel(self)
        LABEL_INFO_Max.move(NUM_220,102)
        LABEL_INFO_Max.setText("MAXIMO")
        LABEL_INFO_Max.resize(NUM_100,NUM_20)
        LABEL_INFO_Max.setStyleSheet('QLabel{; font: bold;font-size: 20px}')# 

        self.botao2_r2= QPushButton("SALVAR",self)
        self.botao2_r2.move(160,NUM_150)#janela
        self.botao2_r2.resize(NUM_100,25)
        self.botao2_r2.setStyleSheet('QPushButton{background-color: #EE82EE; font: bold; font-size: 18px}')
        self.botao2_r2.clicked.connect(self.gravar_dbram)

        self.QCB_C = QCheckBox(" APRESENTAR AVISO",self)
        self.QCB_C.move(NUM_100,190)
        self.QCB_C.resize(250,NUM_30)
        self.QCB_C.setStyleSheet('QCheckBox{font: bold; font-size: 20px;border : 2px solid #EE82EE}')# Violet
        self.QCB_C.clicked.connect(self.check_box_estado)

        
        LABEL_INFO_NUM = QLabel(self)
        LABEL_INFO_NUM.move(NUM_100,240)
        LABEL_INFO_NUM.setText("  * VALIDO ENTRE 1 A 100%.")
        LABEL_INFO_NUM.resize(420,NUM_20)
        LABEL_INFO_NUM.setStyleSheet('QLabel{font: italic;font-size: 14px}')# 

        self.leitura_tb_ram()