from PyQt5.QtWidgets import (QMainWindow, QLabel,
                QPushButton,QSpinBox,QCheckBox)


from variaveis_uni.numero import (NUM_1,NUM_20,NUM_30,NUM_50,
NUM_100,NUM_150,NUM_220)

class GUIFe2Processador(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo 
        
        self.SPINR4_MINIMO = QSpinBox(self)
        self.SPINR4_MINIMO.move(NUM_100,NUM_50)
        self.SPINR4_MINIMO.resize(NUM_100,NUM_30)
        self.SPINR4_MINIMO.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.SPINR4_MINIMO.setMaximum(NUM_100)
        self.SPINR4_MINIMO.setMinimum(NUM_1)


        LABEL_INFO_MAX = QLabel(self)
        LABEL_INFO_MAX.move(NUM_220,52)
        LABEL_INFO_MAX.setText("MINIMO")
        LABEL_INFO_MAX.resize(NUM_100,NUM_20)
        LABEL_INFO_MAX.setStyleSheet('QLabel{; font: bold;font-size: 20px}')# 

        self.spinr2_4 = QSpinBox(self)
        self.spinr2_4.move(NUM_100,NUM_100)
        self.spinr2_4.resize(NUM_100,NUM_30)
        self.spinr2_4.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.spinr2_4.setMaximum(NUM_100)
        self.spinr2_4.setMinimum(NUM_1)

        LABEL_INFO_Max = QLabel(self)
        LABEL_INFO_Max.move(NUM_220,102)
        LABEL_INFO_Max.setText("MAXIMO")
        LABEL_INFO_Max.resize(NUM_100,NUM_20)
        LABEL_INFO_Max.setStyleSheet('QLabel{; font: bold;font-size: 20px}')# 

        self.botao2_r3= QPushButton("SALVAR",self)
        self.botao2_r3.move(160,NUM_150)#janela
        self.botao2_r3.resize(NUM_100,25)
        self.botao2_r3.setStyleSheet('QPushButton{background-color: #EE82EE; font: bold; font-size: 18px}')
        self.botao2_r3.clicked.connect(self.gravar_dbPROC)

        self.QCB_C_4 = QCheckBox(" APRESENTAR AVISO",self)
        self.QCB_C_4.move(NUM_100,190)
        self.QCB_C_4.resize(250,NUM_30)
        self.QCB_C_4.setStyleSheet('QCheckBox{font: bold; font-size: 20px;border : 2px solid #EE82EE}')# Violet
        self.QCB_C_4.clicked.connect(self.check_box_estado_PROC)

        
        LABEL_INFO_NUM_T = QLabel(self)
        LABEL_INFO_NUM_T.move(NUM_100,240)
        LABEL_INFO_NUM_T.setText("  * VALIDO ENTRE 1 A 100%.")
        LABEL_INFO_NUM_T.resize(420,NUM_20)
        LABEL_INFO_NUM_T.setStyleSheet('QLabel{font: italic;font-size: 14px}')# 

        self.leitura_tb_PROC()