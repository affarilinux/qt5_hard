
from variaveis_uni.numero import NUM_1,NUM_100,NUM_0
from variaveis_uni.ESTADO import none

class Verificacao:
   
    def organizacao_tabelas_inicializacao(self):

        self.cursorsq.execute(
            "SELECT * from RAM WHERE ID_RAM = ?",(NUM_1,))
        ex = self.cursorsq.fetchone()
        
        if ex == none:
            
            self.cursorsq.execute(
                "INSERT INTO RAM( RAM_MINIMO,RAM_MAXIMO,RAM_APRESENTAR) VALUES (?,?,?)",(NUM_1,NUM_100,NUM_0))

        self.cursorsq.execute(
            "SELECT * from TEMPERATURA WHERE ID_TEMP = ?",(NUM_1,))
        ex_1 = self.cursorsq.fetchone()
        
        if ex_1 == none:
            
            self.cursorsq.execute(
                "INSERT INTO TEMPERATURA( TEMP_MIN,TEMP_MAX,TEMP_APRESENTAR) VALUES (?,?,?)",(NUM_1,NUM_100,NUM_0))