from PyQt5.QtWidgets import QMainWindow

class SubJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.j_bateria = Janela_bateria()

    def j_b(self):
        self.j_bateria.show()


class Janela_bateria(QMainWindow):
    

    def __init__(self):
        super(Janela_bateria, self).__init__()        

        self.setGeometry(600, 150, 800, 400) #j-XY app-XY
        self.setStyleSheet("background-color: #B0E0E6")#
        self.setWindowTitle("HARDWARE")



        