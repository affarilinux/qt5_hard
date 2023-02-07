import sqlite3

class CriarTabela:
    def __init__( self ):
        
        super ().__init__() # metodo 

        self.ativar_banco()
        
        self.cursorsq.execute(
            """CREATE TABLE if not exists RAM(
            ID_RAM INTEGER PRIMARY KEY AUTOINCREMENT,
            RAM_MINIMO INT,
            RAM_MAXIMO INT,
            RAM_APRESENTAR INT
            )""")
            
        self.sair_banco()