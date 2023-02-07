import psutil

from PyQt5.QtWidgets import QMainWindow


from variaveis_uni.numero import NUM_0,NUM_1,NUM_2,NUM_5

class Temperatura100(QMainWindow):
    
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

            calculosoma = (processador_temp_cur + core_temp_cur + core_temp1_cur + 
                        core_temp2_cur + wifi_temp_cur ) / NUM_5

            
        except KeyError:

            wifi_temp_cur = NUM_0

            calculosoma = (processador_temp_cur + core_temp_cur + core_temp1_cur + 
                        core_temp2_cur + wifi_temp_cur ) / 4


        self.BUTON_TM.setText("TEMPERATURA\n{} ºC".format(calculosoma))

        