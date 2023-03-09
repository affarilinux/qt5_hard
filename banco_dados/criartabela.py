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

        ### ---------------------------------------

        self.cursorsq.execute(
            """CREATE TABLE if not exists HORAS(
            ID_HORAS INTEGER PRIMARY KEY AUTOINCREMENT,
            HORAS TEXT
            )""")
        
        self.cursorsq.execute(
            """CREATE TABLE if not exists DATA_(
            ID_DATA INTEGER PRIMARY KEY AUTOINCREMENT,
            DATA__ TEXT
            )""")

        self.cursorsq.execute(
            """CREATE TABLE if not exists ESTADO_BATERIA(
            ID_ESTADO INTEGER PRIMARY KEY AUTOINCREMENT,
            ESTADO_BATERIA TEXT
            )""")
                
        self.cursorsq.execute(
            """CREATE TABLE if not exists BATER(
            ID_BATER INTEGER PRIMARY KEY AUTOINCREMENT,
            BATER INT
            )""")
        ###---------------------------------------
        ## tabela 1
        self.cursorsq.execute(
            """CREATE TABLE if not exists TEMPO(
            ID_TEMPO INTEGER PRIMARY KEY AUTOINCREMENT,
            TEMPO_DATA INT,
            TEMPO_HORA INT,
            FOREIGN KEY(TEMPO_HORA) REFERENCES HORAS(ID_HORAS),
            FOREIGN KEY(TEMPO_DATA) REFERENCES DATA_(ID_DATA)
            )""")
        
        ## tabel principal
        self.cursorsq.execute(
            """CREATE TABLE if not exists BATERIA_PC(
            ID_GRAFO INTEGER PRIMARY KEY AUTOINCREMENT,
            idx_tempo int,
            VALOR_GRAFO INT,
            CA_DES INT,
            idc_num int,
            FOREIGN KEY(idx_tempo) REFERENCES TEMPO(ID_TEMPO),
            FOREIGN KEY(VALOR_GRAFO) REFERENCES BATER(ID_BATER),
            FOREIGN KEY(CA_DES) REFERENCES ESTADO_BATERIA(ID_ESTADO)
            )""")
        
        ## tabela media intermediaria
        self.cursorsq.execute(
            """CREATE TABLE if not exists MEDIA(
            ID_MEDIA INTEGER PRIMARY KEY AUTOINCREMENT,
            MEDIA_INT INT,
            MEDIA_SECOND INT
            )""")
        
        ## tabela media intermediaria
        self.cursorsq.execute(
            """CREATE TABLE if not exists MEDIA_TEMPO(
            ID_MEDIA_TEMPO INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ex INT,
            tempo_carga text,
            FOREIGN KEY(id_ex) REFERENCES BATERIA_PC(ID_GRAFO)
            )""")
        
        self.commit_banco()
        self.sair_banco()

        self.organizacao_tabelas_inicializacao()

        

       