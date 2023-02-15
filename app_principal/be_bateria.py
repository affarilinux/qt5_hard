import psutil
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

from variaveis_uni.numero import NUM_0,NUM_1,NUM_2,NUM_3
from variaveis_uni.PALAVRA import BATERIA_LT

from variaveis_uni.ESTADO import falsepal,truepal,none

class Bateria100(QMainWindow):

    def __init__( self ):
            
        super ().__init__() # metodo

        self.var_bty = NUM_0
        self.var_estado_bat = NUM_0
        self.var_qtcore = NUM_0

    def chamada_qtimerbateria(self):

        #---------------------------------------------------------------
        # chama os dados para a janela
        BATERIA_sistema = psutil.sensors_battery()

        # chama o tipo de informação
        nivel_bateria   = BATERIA_sistema.percent

        # transforma em int
        entrada_informacao = int(nivel_bateria)

        #---------------------------------------------------------------
        # puxa os dado do sistema operacional
        informacao_bateria = psutil.sensors_battery()

        # puxa uma informação se esta plugado na internet
        informacao_carregamento = informacao_bateria.power_plugged 

        est = none

        if informacao_carregamento   == truepal :
                
               est = "ca"
                
        elif informacao_carregamento == falsepal :
                est = "des"

        self.ativar_banco()

        self.cursorsq.execute("SELECT BAT_MIN, BAT_MAX,BAT_APRESENTAR FROM  BATERIA  WHERE ID_BAT = ?",(NUM_1,))
        batere = self.cursorsq.fetchone()
        
        if batere[NUM_2] == NUM_1:

            if nivel_bateria <= batere[NUM_0]:

                self.if_bt_(NUM_1,batere[NUM_0],est,entrada_informacao)

            elif nivel_bateria > batere[NUM_0] and nivel_bateria <= batere[NUM_1]:

                self.apt_funcao(est,entrada_informacao)
                self.funcao_var_bat()
            
            elif nivel_bateria > batere[NUM_1]:

                  self.if_bt_(NUM_0,batere[NUM_1],est,entrada_informacao)

        ##--------------------------------------------------------------
        elif batere[NUM_2] == NUM_0:

            self.apt_funcao(est,entrada_informacao)
            self.funcao_var_bat()

        self.commit_banco()
        self.sair_banco()

    ###----------------------------------------------------------------
    def if_bt_ (self,se,tbb,estt,enin):

        if self.var_estado_bat == NUM_0:

            self.var_bty = self.var_bty + NUM_1

            if self.var_bty == NUM_1:

                    ## sinal de menor
                    if se == NUM_1:
                        self.apt_funcao_alter("--",tbb)
                        

                        if estt == "des":
                            print(estt)
    
                            self.funcao_if_son()

                    elif se == NUM_0:
                        
                        self.apt_funcao_alter("++",tbb)

                        if estt == "ca":
    
                            self.funcao_if_son()

            elif self.var_bty != NUM_0:

                self.apt_funcao(estt,enin)

                if self.var_bty == NUM_3:
                    self.var_bty = NUM_0

        elif self.var_estado_bat == NUM_1:

            self.apt_funcao(estt,enin)
            self.funcao_var_bat()

            if self.var_qtcore == NUM_0:

                self.var_qtcore = NUM_1

                QtCore.QTimer.singleShot(120000, self.if_btest)

    def if_btest(self):

        self.var_qtcore = NUM_0
        self.var_estado_bat = NUM_0

    ###----------------------------------------------------------------
        #---------------------------------------------------------------
        # chama a janela'
    ###-----------------------------------------------------------------
    def apt_funcao(self,etd,ei):

        self.BUTON_BATERIA.setText(
            "{}\n{} 00:00\n{} %".format(BATERIA_LT,etd,ei))
    
    def apt_funcao_alter(self, prc,tb):

          self.BUTON_BATERIA.setText(
            "{}\n {} {} %".format(BATERIA_LT,prc,tb))

    def funcao_var_bat(self):
    
        if self.var_bty != NUM_0:
            self.var_bty = NUM_0

    


       
       