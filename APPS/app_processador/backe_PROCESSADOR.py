from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1,NUM_2
from variaveis_uni.ESTADO import none,truepal,falsepal

class BeProcessador(QMainWindow):

    ## INICIO
    def leitura_tb_PROC(self):

        self.ativar_banco()
            
        self.cursorsq.execute("SELECT PROC_MIN,PROC_MAX,PROC_APRESENTAR FROM  PROCESSADOR  WHERE ID_PROC = ?",(NUM_1,))
        spin_PRO = self.cursorsq.fetchone()
        
        self.SPINR4_MINIMO.setValue(spin_PRO[NUM_0])
        self.spinr2_4.setValue(spin_PRO[NUM_1])

        estad_PROC = none

        if spin_PRO[NUM_2] == NUM_0:
            estad_PROC = falsepal
        else:
            estad_PROC = truepal
        
        self.QCB_C_4.setChecked( estad_PROC )
        
        self.sair_banco()
    

    ## BOTAO
    def gravar_dbPROC(self):

        self.ativar_banco()

        value_PRO =  self.SPINR4_MINIMO.value()
        value2_PRO = self.spinr2_4.value()
        
        if value_PRO < value2_PRO:
            
            self.cursorsq.execute(
                "UPDATE PROCESSADOR SET PROC_MIN = ?, PROC_MAX = ? WHERE ID_PROC = ?",(value_PRO,value2_PRO,NUM_1,)) 

        else:

            self.cursorsq.execute("SELECT PROC_MIN,PROC_MAX FROM  PROCESSADOR  WHERE ID_PROC = ?",(NUM_1,))
            spin_PRO = self.cursorsq.fetchone()
            
            self.SPINR4_MINIMO.setValue(spin_PRO[NUM_0])
            self.spinr2_4.setValue(spin_PRO[NUM_1])

        self.commit_banco()
        self.sair_banco()

    ## ATIVAR E DESATIVAR AVISO
    def check_box_estado_PROC(self):

        self.ativar_banco()

        estado_PRO = none
        if self.QCB_C_4.isChecked():
            estado_PRO = NUM_1
          
        else:
            estado_PRO = NUM_0
            
        self.cursorsq.execute(
                "UPDATE PROCESSADOR SET PROC_APRESENTAR = ? WHERE ID_PROC = ?",(estado_PRO,NUM_1,)) 

        self.commit_banco()
        self.sair_banco()
    
    