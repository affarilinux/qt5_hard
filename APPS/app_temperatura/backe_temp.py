from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1
from variaveis_uni.ESTADO import none,truepal,falsepal

class BeTemperatura(QMainWindow):

    def leitura_tb_temperatura(self):

        self.ativar_banco()
            
        self.cursorsq.execute("SELECT TEMP_MIN,TEMP_MAX,TEMP_APRESENTAR FROM  TEMPERATURA  WHERE ID_TEMP = ?",(NUM_1,))
        spin_T = self.cursorsq.fetchone()
        
        self.SPINR3_MINIMO.setValue(spin_T[0])
        self.spinr2_3.setValue(spin_T[1])
        estad_T = none
        if spin_T[2] == NUM_0:
            estad_T = falsepal
        else:
            estad_T = truepal
        
        self.QCB_C_3.setChecked( estad_T )
        
        self.sair_banco()
    
    def gravar_dbram(self):

        self.ativar_banco()

        value_T =  self.SPINR3_MINIMO.value()
        value2_T = self.spinr2_3.value()
        
        if value_T < value2_T:
            
            self.cursorsq.execute(
                "UPDATE TEMPERATURA SET TEMP_MIN = ?, TEMP_MAX = ? WHERE ID_TEMP = ?",(value_T,value2_T,NUM_1,)) 

        else:

            self.cursorsq.execute("SELECT TEMP_MIN,TEMP_MAX FROM  TEMPERATURA  WHERE ID_TEMP = ?",(NUM_1,))
            spin_n = self.cursorsq.fetchone()
            
            self.SPINR3_MINIMO.setValue(spin_n[0])
            self.spinr2_3.setValue(spin_n[1])

        self.commit_banco()
        self.sair_banco()

    def check_box_estado(self):

        self.ativar_banco()

        estado_T = none
        if self.QCB_C_3.isChecked():
            estado_T = NUM_1
          
        else:
            estado_T = NUM_0
            
        self.cursorsq.execute(
                "UPDATE TEMPERATURA SET TEMP_APRESENTAR = ? WHERE ID_TEMP = ?",(estado_T,NUM_1,)) 

        self.commit_banco()
        self.sair_banco()
    
    