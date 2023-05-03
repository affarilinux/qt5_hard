class ApagarDados:

    def Apagarr(self):

        self.ativar_banco()

        self.cursorsq.execute(" DELETE FROM MEDIA_TEMPO")
        self.cursorsq.execute(" DELETE FROM BATERIA_PC")
        self.cursorsq.execute(" DELETE FROM TEMPO")

        self.cursorsq.execute(" DELETE FROM DATA_")

        self.cursorsq.execute(" DELETE FROM MEDIA")

        self.cursorsq.execute(
            """ DELETE FROM sqlite_sequence where name in (
                'MEDIA_TEMPO', 'BATERIA_PC','TEMPO','DATA_','MEDIA') """)
        

        self.commit_banco()
        self.sair_banco()