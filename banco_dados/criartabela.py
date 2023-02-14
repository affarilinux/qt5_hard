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

        self.cursorsq.execute(
            """CREATE TABLE if not exists TEMPERATURA(
            ID_TEMP INTEGER PRIMARY KEY AUTOINCREMENT,
            TEMP_MIN INT,
            TEMP_MAX INT,
            TEMP_APRESENTAR INT
            )""")

        self.cursorsq.execute(
            """CREATE TABLE if not exists PROCESSADOR(
            ID_PROC INTEGER PRIMARY KEY AUTOINCREMENT,
            PROC_MIN INT,
            PROC_MAX INT,
            PROC_APRESENTAR INT
            )""")

        self.cursorsq.execute(
            """CREATE TABLE if not exists BATERIA(
            ID_BAT INTEGER PRIMARY KEY AUTOINCREMENT,
            BAT_MIN INT,
            BAT_MAX INT,
            BAT_APRESENTAR INT
            )""")

        self.organizacao_tabelas_inicializacao()

        self.commit_banco()
        self.sair_banco()