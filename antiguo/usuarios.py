from usuario import Usuario

class Admon(Usuario):
    def __init__(self):
        self.cargo="Administrador"
        self.carrera="No aplica"
        super().__init__()
    def llenar_usuario(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.documento=-1
        while self.documento==-1:
            try:
                documento=int(input("Ingrese un numero de identificación del usuario:\n"))
                if documento>0:
                    self.documento=documento
            except ValueError:
                pass

class Docente(Usuario):
    def __init__(self):
        self.cargo="Docente"
        super().__init__()
    def llenar_usuario(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.documento=-1
        while self.documento==-1:
            try:
                documento=int(input("Ingrese un numero de identificación del usuario:\n"))
                if documento>0:
                    self.documento=documento
            except ValueError:
                pass

class Estudiante(Usuario):
    def __init__(self):
        self.cargo="Estudiante"
        super().__init__()
    def llenar_usuario(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.documento=-1
        while self.documento==-1:
            try:
                documento=int(input("Ingrese un numero de identificación del usuario:\n"))
                if documento>0:
                    self.documento=documento
            except ValueError:
                pass