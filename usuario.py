class Usuario():
    def __init__(self):
        self.cargo: type[str]
        self.sede: type[str]
        self.carrera: type[str]
        self.nombre: type[str]
    def llenar_usuario(self):
        pass

class Admon(Usuario):
    def __init__(self):
        self.cargo="Administrador"
        self.carrera=None
        super().__init__()
    def llenar_usuario(self):
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.sede=str(input("Ingrese la sede del usuario:\n"))

class Docente(Usuario):
    def __init__(self):
        self.cargo="Docente"
        super().__init__()
    def llenar_usuario(self):
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))

class Estudiante(Usuario):
    def __init__(self):
        self.cargo="Estudiante"
        super().__init__()
    def llenar_usuario(self):
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
        