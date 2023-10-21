class Usuario:
    def __init__(self):
        self.cargo = ""
        self.sede = ""
        self.carrera = ""
        self.nombre= ""
        self.documento = -1

    def asignar_sede(self, sede):
        self.sede=sede
    def asignar_carrera(self,carrera):
        self.carrera=carrera
    def asignar_nombre(self,nombre):
        self.nombre=nombre
    def asignar_documento(self,documento):
        self.documento=documento
    def asignar_cargo(self,cargo):
        self.cargo=cargo

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
    
    def leer_sede(self):
        sede=str(input("Ingrese la sede del usuario:\n"))
        self.asignar_sede(sede)
    def leer_carrera(self):
        carrera=str(input("Ingrese la carrera a la que pertenece el usuario:\n"))
        self.asignar_carrera(carrera)
    def leer_nombre(self):
        nombre=str(input("Ingrese el nombre del usuario:\n"))
        self.asignar_nombre(nombre)
    def leer_documento(self):
        while self.documento==-1:
            try:
                documento=int(input("Ingrese un numero de identificación del usuario:\n"))
                if documento>0:
                    self.asignar_documento(documento)
            except ValueError:
                pass
    
    def llenar_usuario(self):
        pass

    def mostrar_info(self):
        print("\tNombre: "+self.nombre)
        print("\tCargo: "+ self.cargo)
        print("\tSede: "+ self.sede)
        print("\tCarrera: "+ self.carrera)