class Usuario:
    def __init__(self):
        self.cargo = ""
        self.sede = ""
        self.carrera = ""
        self.nombre= ""
        self.documento = -1
    def asignar_sede(self):
        self.sede=str(input("Ingrese la sede del usuario:\n"))
    def asignar_carrera(self):
        self.carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
    def asignar_nombre(self):
        self.nombre=str(input("Ingrese el nombre del usuario:\n"))
    def asignar_documento(self):
        while self.documento==-1:
            try:
                documento=int(input("Ingrese un numero de identificación del usuario:\n"))
                if documento>0:
                    self.documento=documento
            except ValueError:
                pass

    def entregar_sede(self):
        return self.sede
    def entregar_cargo(self):
        return self.cargo
    def entregar_carrera(self):
        return self.carrera
    def entregar_nombre(self):
        return self.nombre
    def entregar_documento(self):
        return self.documento
    
    def llenar_usuario(self):
        pass