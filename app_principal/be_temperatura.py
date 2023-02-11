import psutil

from PyQt5.QtWidgets import QMainWindow


from variaveis_uni.numero import NUM_0,NUM_1,NUM_2,NUM_3,NUM_4,NUM_5
from variaveis_uni.PALAVRA import TEMPERATURA_LT

class Temperatura100(QMainWindow):

    def __init__( self ):
        
        super ().__init__() # metodo

        self.var_2 = NUM_0
    
    def temperatura_lib(self):

        processador_temp = psutil.sensors_temperatures()['acpitz'][NUM_0]

        core_temp        = psutil.sensors_temperatures()['coretemp'][NUM_0]
        core_temp1       = psutil.sensors_temperatures()['coretemp'][NUM_1]
        core_temp2       = psutil.sensors_temperatures()['coretemp'][NUM_2]

        processador_temp_cur = processador_temp.current

        core_temp_cur = core_temp.current
        core_temp1_cur = core_temp1.current
        core_temp2_cur = core_temp2.current

        try:
            wifi_temp    = psutil.sensors_temperatures()['iwlwifi_1'][NUM_0]
            wifi_temp_cur  = wifi_temp.current

            self.calculo_temperatura (processador_temp_cur, core_temp_cur,
                core_temp1_cur,core_temp2_cur, wifi_temp_cur,NUM_5 )

            
        except KeyError:

            self.calculo_temperatura (processador_temp_cur, core_temp_cur,
                core_temp1_cur,core_temp2_cur, NUM_0,NUM_4 )

         ##---------------------------------------------------------------------
       
    def calculo_temperatura(self,ptc,ctc,ctc1,ctc2,wtc,div):

        calculosoma = (ptc + ctc  + ctc1 + ctc2 + wtc ) / div

        self.ativar_banco()

        self.cursorsq.execute("SELECT TEMP_MIN,TEMP_MAX,TEMP_APRESENTAR FROM  TEMPERATURA WHERE ID_TEMP = ?",(NUM_1,))
        SELEC = self.cursorsq.fetchone()

        if SELEC[NUM_2] ==  NUM_1:
            
            if ptc >= SELEC[NUM_1]:
                
                self.ap_temp_t1(NUM_0,ptc,calculosoma)

            elif  ctc >= SELEC[NUM_1]:
                
                self.ap_temp_t1(NUM_1,ctc,calculosoma)
            
            elif  ctc1 >= SELEC[NUM_1]:
                
                self.ap_temp_t1(NUM_2,ctc1,calculosoma)

            elif  ctc2 >= SELEC[NUM_1]:
                
                self.ap_temp_t1(NUM_3,ctc2,calculosoma)

            elif  wtc >= SELEC[NUM_1]:
                
                self.ap_temp_t1(NUM_4,wtc,calculosoma)
            
            elif  calculosoma >= SELEC[NUM_1]:
                
                self.ap_temp_t1(NUM_5,calculosoma,calculosoma)
            

            ##------------------------------------
            else:
                self.apresentar_temp(TEMPERATURA_LT,calculosoma)
                
                self.var_if_temp()

        elif SELEC[2] == NUM_0:

            self.apresentar_temp(TEMPERATURA_LT,calculosoma)

            self.var_if_temp()

        self.sair_banco()
    ##------------------------------------------------------------------
    def ap_temp_t1(self,i1,ap1,calc):

        self.var_2 = self.var_2 + NUM_1

        if self.var_2 == NUM_1:
    
            if i1 == NUM_0:
                self.apresentar_temp("PLACA MAE",ap1)

            elif i1 == NUM_1:
                self.apresentar_temp("CORE",ap1)
            
            elif i1 == NUM_2:
                self.apresentar_temp("CORE 1",ap1)
            
            elif i1 == NUM_3:
                self.apresentar_temp("CORE 2",ap1)
            
            elif i1 == NUM_4:
                self.apresentar_temp("WIFI",ap1)

            elif i1 == NUM_5:
                self.apresentar_temp(TEMPERATURA_LT,ap1)

            self.funcao_if_son()
            
        ##----------------------------------------
        elif self.var_2 != NUM_0:

            self.apresentar_temp(TEMPERATURA_LT,calc)

            if self.var_2 == NUM_3:
                
                self.var_2 = NUM_0

    def var_if_temp(self):

        if self.var_2 != NUM_0:
    
            self.var_2 = NUM_0
    ##__________________________________________________________________
    def apresentar_temp(self,a1,a2):
        self.BUTON_TM.setText("{}\n{} ºC".format(a1,a2))

        