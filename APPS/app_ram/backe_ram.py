from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1
from variaveis_uni.ESTADO import none,truepal,falsepal

class BeRam(QMainWindow):

    def leitura_tb_ram(self):

        self.ativar_banco()
            
        self.cursorsq.execute("SELECT RAM_MINIMO,RAM_MAXIMO,RAM_APRESENTAR FROM  RAM  WHERE ID_RAM = ?",(NUM_1,))
        spin = self.cursorsq.fetchone()
        
        self.SPINR2_MINIMO.setValue(spin[0])
        self.spinr2_2.setValue(spin[1])
        estad = none
        if spin[2] == NUM_0:
            estad = falsepal
        else:
            estad = truepal
        
        self.QCB_C.setChecked( estad )
        
        self.sair_banco()
    
    def gravar_dbram(self):

        self.ativar_banco()

        value =  self.SPINR2_MINIMO.value()
        value2 = self.spinr2_2.value()
        
        if value < value2:
            
            self.cursorsq.execute(
                "UPDATE RAM SET RAM_MINIMO = ?, RAM_MAXIMO = ? WHERE ID_RAM = ?",(value,value2,NUM_1,)) 

        else:

            self.cursorsq.execute("SELECT RAM_MINIMO,RAM_MAXIMO FROM  RAM  WHERE ID_RAM = ?",(NUM_1,))
            spin_n = self.cursorsq.fetchone()
            
            self.SPINR2_MINIMO.setValue(spin_n[0])
            self.spinr2_2.setValue(spin_n[1])

        self.commit_banco()
        self.sair_banco()

    def check_box_estado(self):

        self.ativar_banco()

        estado = none
        if self.QCB_C.isChecked():
            estado = NUM_1
          
        else:
            estado = NUM_0
            
        self.cursorsq.execute(
                "UPDATE RAM SET RAM_APRESENTAR = ? WHERE ID_RAM = ?",(estado,NUM_1,)) 

        self.commit_banco()
        self.sair_banco()
    
    