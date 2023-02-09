from PyQt5.QtWidgets import QMainWindow
import psutil


##VARIAVEIS
from variaveis_uni.numero import NUM_0,NUM_1,NUM_2,NUM_100
from variaveis_uni.PALAVRA import RAM_LT

class BE_Ram(QMainWindow):
    
    def __init__( self ):
        
        super ().__init__() # metodo

        self.var_1 = NUM_0

    def ps_ram(self):

        #informações da memoria ram
        informacao           = psutil.virtual_memory ()

        # puxa as informações e adiciona nas variaveis
        total                = informacao.total
        usada                = informacao.active

        # calcula porcentagm
        calculo_por_centagem      = ( usada * NUM_100 ) / total

        # filtra o float
        calculo_filtro_informacao = round ( calculo_por_centagem, NUM_2 )

        ##---------------------------------------------------------------------
        self.ativar_banco()
        
        self.cursorsq.execute("SELECT RAM_MINIMO,RAM_MAXIMO,RAM_APRESENTAR FROM  RAM  WHERE ID_RAM = ?",(NUM_1,))
        sel = self.cursorsq.fetchone()

        if sel[2] == NUM_1:
            
            if calculo_filtro_informacao < sel[0]:

                self.ap_ram_processo('--',sel,NUM_0,calculo_filtro_informacao)

               
            elif calculo_filtro_informacao >= sel[0] and calculo_filtro_informacao <= sel[1]:

                self.ap_ram_normal(calculo_filtro_informacao)
            
            elif calculo_filtro_informacao > sel[1]:
                
                self.ap_ram_processo('++',sel,NUM_1,calculo_filtro_informacao)
                
        elif sel[2] == NUM_0:
    
            self.ap_ram_normal(calculo_filtro_informacao)

        self.sair_banco()

    ##------------------------------------------------------------------
    def ap_ram_normal(self,cfi):

        self.BUTON_RAM.setText("{}\n {} %".format(RAM_LT,cfi))

        if self.var_1 != NUM_0:

            self.var_1 = NUM_0

    def ap_ram_processo(self,sinal,sel_,NU,cfii):

        self.var_1 = self.var_1 + NUM_1

        if self.var_1 == NUM_1:

            self.BUTON_RAM.setText("{}\n{} {} %".format(RAM_LT,sinal,sel_[NU]))

        else:
            self.BUTON_RAM.setText("{}\n {} %".format(RAM_LT,cfii))

            if self.var_1 == 3:

                self.var_1 = NUM_0    

