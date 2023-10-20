from biblioteca import Biblioteca

class Ingenieria(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Facultad de Ingeniería"
        self.txt="antiguo/archivosTexto/ingenieria.txt"
        super().__init__()
    
class Paiba(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Ramón Eduardo DLuyz Nieto"
        self.txt="antiguo/archivosTexto/paiba.txt"
        super().__init__()

class Artes(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Facultad de Artes Asab"
        self.txt="antiguo/archivosTexto/artes.txt"
        super().__init__()