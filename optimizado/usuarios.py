from usuario import Usuario

class Admin(Usuario):
    def __init__(self):
        super().__init__()
        self.cargo="Administrativo"
        self.carrera="No aplica"
    def llenar_usuario(self):
        self.leer_nombre()
        self.leer_documento()
        self.leer_sede()

class Docente(Usuario):
    def __init__(self):
        super().__init__()
        self.cargo="Docente"
    def llenar_usuario(self):
        self.leer_nombre()
        self.leer_documento()
        self.leer_sede()
        self.leer_carrera()

class Estudiante(Usuario):
    def __init__(self):
        super().__init__()
        self.cargo="Estudiante"
    def llenar_usuario(self):
        self.leer_nombre()
        self.leer_documento()
        self.leer_sede()
        self.leer_carrera()