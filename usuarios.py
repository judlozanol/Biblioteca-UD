from usuario import Usuario

class Admon(Usuario):
    def __init__(self):
        self.cargo="Administrador"
        self.carrera="No aplica"
        super().__init__()
    def llenar_usuario(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))

class Docente(Usuario):
    def __init__(self):
        self.cargo="Docente"
        super().__init__()
    def llenar_usuario(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
class Estudiante(Usuario):
    def __init__(self):
        self.cargo="Estudiante"
        super().__init__()
    def llenar_usuario(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))