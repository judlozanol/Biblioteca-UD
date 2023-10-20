from biblioteca import Biblioteca

class Ingenieria(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Facultad de Ingeniería"
        self.txt="ingenieria.txt"
        super().__init__()
    
class Paiba(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Ramón Eduardo DLuyz Nieto"
        self.txt="paiba.txt"
        super().__init__()

class Artes(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Facultad de Artes Asab"
        self.txt="artes.txt"
        super().__init__()