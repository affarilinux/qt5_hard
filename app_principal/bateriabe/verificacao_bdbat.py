from datetime import datetime

from PyQt5.QtWidgets import QMainWindow

from variaveis_uni.numero import NUM_0,NUM_1,NUM_100
from variaveis_uni.ESTADO import none,truepal

class BateriaBD(QMainWindow):

    def bat_tb_bd(self,PC,ETCC):

        hoje = datetime.now()

        ## data
        self.hj = hoje.strftime('%d/%m/%Y')
    
        self.ativar_banco()
        
        self.cursorsq.execute("SELECT DATA__ FROM  DATA_  WHERE ID_DATA = ?",(NUM_1,))
        dt = self.cursorsq.fetchone()

        if dt == none:
            self.cursorsq.execute(
                "INSERT INTO DATA_( DATA__) VALUES (?)",(self.hj,))

        elif dt != none:

            self.cursorsq.execute("SELECT ID_DATA FROM  DATA_  WHERE DATA__ = ?",(self.hj,))
            dt_2 = self.cursorsq.fetchone()
            
            if dt_2 == none:
                self.cursorsq.execute(
                    "INSERT INTO DATA_( DATA__) VALUES (?)",(self.hj,))

        self.commit_banco()
        self.sair_banco()

        ##horas
        ######----------------------------------------------------------
        self.hr = hoje.strftime('%H:%M:%S')
        
        self.ativar_banco()
        self.cursorsq.execute("SELECT HORAS FROM  HORAS  WHERE ID_HORAS = ?",(NUM_1,))
        HR = self.cursorsq.fetchone()

        if HR == none:
            self.cursorsq.execute(
                "INSERT INTO HORAS( HORAS) VALUES (?)",(self.hr,))

        elif HR != none:

            self.cursorsq.execute("SELECT ID_HORAS FROM  HORAS  WHERE HORAS = ?",(self.hr,))
            HR_2 = self.cursorsq.fetchone()
                       
            if HR_2 == none:
                self.cursorsq.execute(
                    "INSERT INTO HORAS( HORAS) VALUES (?)",(self.hr,))

        
        self.commit_banco()
        self.sair_banco()
    
        ## nivel bateria
        ###-------------------------------------------------------------
        self.ativar_banco()

        self.cursorsq.execute("SELECT ID_BATER FROM  BATER  WHERE BATER = ?",(PC,))
        NIVBAT = self.cursorsq.fetchone()

        if NIVBAT == none:
            self.cursorsq.execute(
                "INSERT INTO BATER( BATER) VALUES (?)",(PC,))

        self.commit_banco()
        self.sair_banco()

        ###-----------------------------------------
        self.ativar_banco()

        self.cursorsq.execute("SELECT ESTADO_BATERIA FROM  ESTADO_BATERIA  WHERE ESTADO_BATERIA = ?",(ETCC,))
        NIVBAT = self.cursorsq.fetchone()

        if NIVBAT == none:
            self.cursorsq.execute(
                "INSERT INTO ESTADO_BATERIA( ESTADO_BATERIA) VALUES (?)",(ETCC,))

        self.commit_banco()
        self.sair_banco()

       