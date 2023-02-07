from PyQt5.QtWidgets import (QMainWindow, QLabel,
                QPushButton,QSpinBox,QCheckBox)


class GUIFe2Ram(QMainWindow):
    def __init__( self ):
    
        super ().__init__() # metodo 
        
        self.SPINR2_MINIMO = QSpinBox(self)
        self.SPINR2_MINIMO.move(100,50)
        self.SPINR2_MINIMO.resize(100,30)
        self.SPINR2_MINIMO.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.SPINR2_MINIMO.setMaximum(100)
        self.SPINR2_MINIMO.setMinimum(1)
        #self.spin.valueChanged.connect(self.widget_processador121)


        LABEL_INFO_M = QLabel(self)
        LABEL_INFO_M.move(220,52)
        LABEL_INFO_M.setText("MINIMO")
        LABEL_INFO_M.resize(100,20)
        LABEL_INFO_M.setStyleSheet('QLabel{; font: bold;font-size: 20px}')# 

        self.spinr2_2 = QSpinBox(self)
        self.spinr2_2.move(100,100)
        self.spinr2_2.resize(100,30)
        self.spinr2_2.setStyleSheet('QSpinBox{background-color: #EE82EE;font: bold; font-size: 20px}')# Violet
        self.spinr2_2.setMaximum(100)
        self.spinr2_2.setMinimum(1)

        LABEL_INFO_Max = QLabel(self)
        LABEL_INFO_Max.move(220,102)
        LABEL_INFO_Max.setText("MAXIMO")
        LABEL_INFO_Max.resize(100,20)
        LABEL_INFO_Max.setStyleSheet('QLabel{; font: bold;font-size: 20px}')# 

        self.botao2_r2= QPushButton("SALVAR",self)
        self.botao2_r2.move(160,150)#janela
        self.botao2_r2.resize(100,25)
        self.botao2_r2.setStyleSheet('QPushButton{background-color: #EE82EE; font: bold; font-size: 18px}')
        #self.botao2_r2.clicked.connect(self.whidget_ram_fun)

        self.QCB_C = QCheckBox(" APRESENTAR",self)
        self.QCB_C.move(100,190)
        self.QCB_C.resize(180,30)
        self.QCB_C.setStyleSheet('QCheckBox{font: bold; font-size: 20px;border : 2px solid #EE82EE}')# Violet
        #self.QCB_C.stateChanged.connect(self.widget_processador12)
        
        LABEL_INFO_NUM = QLabel(self)
        LABEL_INFO_NUM.move(100,240)
        LABEL_INFO_NUM.setText("  * VALIDO ENTRE 1 A 100%.")
        LABEL_INFO_NUM.resize(420,20)
        LABEL_INFO_NUM.setStyleSheet('QLabel{font: italic;font-size: 14px}')# 