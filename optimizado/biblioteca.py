from libro import Libro
from buscadorLibros import BuscadorLibros

class Biblioteca:
    def __init__(self):
        self.nombre: type[str]
        self.txt: type[str]
        self.libros=[]
        self.actualizar_biblioteca()

    def leer_libros(self):
        archivo=open(self.txt)
        for linea in archivo:
            libro = Libro()
            contenido= (linea.rstrip("\n")).split("/")
            libro.asignar_nombre(contenido[0])
            libro.asignar_autor(contenido[1])
            libro.asignar_biblioteca(self.nombre)
            if len(contenido)>2:
                libro.cambiar_estado()
                libro.poseedor.asignar_nombre(contenido[2])
                libro.poseedor.asignar_documento(int(contenido[3]))
                libro.poseedor.asignar_cargo(contenido[4])
                libro.poseedor.asignar_sede(contenido[5])
                libro.poseedor.asignar_carrera(contenido[6])
            self.libros.append(libro)
        archivo.close()

    def actualizar_biblioteca(self):
        self.leer_libros()
        self.buscador=BuscadorLibros(self)