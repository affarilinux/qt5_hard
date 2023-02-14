from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1,NUM_2
from variaveis_uni.ESTADO import none,truepal,falsepal

class BeBateria(QMainWindow):

    ## INICIO
    def leitura_tb_BATE(self):

        self.ativar_banco()
            
        self.cursorsq.execute("SELECT BAT_MIN,BAT_MAX,BAT_APRESENTAR FROM  BATERIA  WHERE ID_BAT = ?",(NUM_1,))
        spin_BT = self.cursorsq.fetchone()
        
        self.SPINR5_MINIMO.setValue(spin_BT[NUM_0])
        self.spinr2_5.setValue(spin_BT[NUM_1])

        estad_BT = none

        if spin_BT[NUM_2] == NUM_0:
            estad_BT = falsepal
        else:
            estad_BT = truepal
        
        self.QCB_C_5.setChecked( estad_BT )
        
        self.sair_banco()
    

    ## BOTAO
    def gravar_dbBATE(self):

        self.ativar_banco()

        value_BTR =  self.SPINR5_MINIMO.value()
        value2_BTR = self.spinr2_5.value()
        
        if value_BTR < value2_BTR:
            
            self.cursorsq.execute(
                "UPDATE BATERIA SET BAT_MIN = ?, BAT_MAX = ? WHERE ID_BAT = ?",(value_BTR,value2_BTR,NUM_1,)) 

        else:

            self.cursorsq.execute("SELECT BAT_MIN,BAT_MAX FROM  BATERIA  WHERE ID_BAT = ?",(NUM_1,))
            spin_BTR = self.cursorsq.fetchone()
            
            self.SPINR5_MINIMO.setValue(spin_BTR[NUM_0])
            self.spinr2_5.setValue(spin_BTR[NUM_1])

        self.commit_banco()
        self.sair_banco()

    ## ATIVAR E DESATIVAR AVISO
    def check_box_estado_BATE(self):

        self.ativar_banco()

        estado_BTA = none
        if self.QCB_C_5.isChecked():
            estado_BTA = NUM_1
          
        else:
            estado_BTA = NUM_0
            
        self.cursorsq.execute(
                "UPDATE BATERIA SET BAT_APRESENTAR = ? WHERE ID_BAT = ?",(estado_BTA,NUM_1,)) 

        self.commit_banco()
        self.sair_banco()
    
    