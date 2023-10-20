from biblioteca import Biblioteca

class Ingenieria(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Facultad de Ingeniería"
        self.txt="optimizado/archivosTexto/ingenieria.txt"
        super().__init__()
    
class Paiba(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Ramón Eduardo DLuyz Nieto"
        self.txt="optimizado/archivosTexto/paiba.txt"
        super().__init__()

class Artes(Biblioteca):
    def __init__(self):
        self.nombre="Biblioteca Facultad de Artes Asab"
        self.txt="optimizado/archivosTexto/artes.txt"
        super().__init__()

if __name__=="__main__":
    p=Paiba()
    print("#######"+p.nombre)
    for libro in p.libros:
        print(libro.nombre)
