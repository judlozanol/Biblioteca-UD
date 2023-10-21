from usuario import Usuario

class Libro:
    def __init__(self):
        self.nombre=""
        self.autor=""
        self.biblioteca=""
        self.prestado=False
        self.poseedor=Usuario()

    def asignar_biblioteca(self, biblioteca):
        self.biblioteca=biblioteca
    def asignar_nombre(self,nombre):
        self.nombre=nombre
    def asignar_autor(self,autor):
        self.autor=autor
    def agregar_poseedor(self,poseedor):
        self.poseedor=poseedor
    
    def entregar_biblioteca(self):
        return self.biblioteca
    def entregar_nombre(self):
        return self.nombre
    def entregar_autor(self):
        return self.autor
    def entregar_estado(self):
        return self.prestado
    def entregar_poseedor(self):
        return self.poseedor
    
    def cambiar_estado(self):
        if self.prestado:
            self.prestado=False
        else:
            self.prestado=True
    
    def mostrar_info(self):
        print("\tNombre: "+ self.nombre)
        print("\tAutor: "+ self.autor)
        print("\tBiblioteca: "+ self.biblioteca)