from libro import Libro
class Biblioteca():
    def __init__(self):
        self.nombre: type[str]
        self.libros=[]
        self.txt: type[str]
        self.agregar_libros()
    def agregar_libros(self):
        archivo=open(self.txt)
        for linea in archivo:
            libro= Libro()
            contenido= (linea.rstrip("\n")).split("/")
            libro.nombre=contenido[0]
            libro.autor=contenido[1]
            if len(contenido)>2:
                libro.prestado=True
            self.libros.append(libro)
    def consultar_libros(self):
        print("libros en "+self.nombre)
        for i in range(len(self.libros)):
            print(self.libros[i].nombre+"/"+self.libros[i].autor)
