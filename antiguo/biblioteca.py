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
            libro.biblioteca=self.nombre
            if len(contenido)>2:
                libro.prestado=True
                libro.poseedor.cargo=contenido[3]
                libro.poseedor.sede=contenido[4]
                libro.poseedor.carrera=contenido[5]
                libro.poseedor.nombre=contenido[2]
                libro.poseedor.documento=int(contenido[6])
            self.libros.append(libro)
        archivo.close()