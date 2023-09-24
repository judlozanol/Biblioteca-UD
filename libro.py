from usuario import Usuario
class Libro():
    def __init__(self):
        self.nombre: type[str]
        self.autor: type[str]
        self.biblioteca: type[str]
        self.prestado= False
        if self.prestado:
            self.poseedor: type[Usuario]