from bibliotecas import *
from usuarios import *

class Sistema():
    def __init__(self):
        self.bibliotecas=[Ingenieria(),Paiba(),Artes()]
        self.usuarios=[Admin(),Docente(),Estudiante()]
        self.usuario=Usuario()
    
    def iniciar_sesion(self):
        for index,usuario in enumerate(self.usuarios):
            print("\t("+str(index+1)+") "+ usuario.cargo)
        indice=-1
        while indice<1 or indice>len(self.usuarios):
            try:
                indice=int(input("\nIngrese el cargo al que pertenece:"))
            except ValueError:
                pass

        self.usuario= self.usuarios[indice-1]
        self.usuario.llenar_usuario()
    
    def buscar_libro(self):
        nombre=str(input("Ingrese el nombre del libro que busca:\n"))
        libro_pedido=[]
        for biblioteca in self.bibliotecas:
            libro_pedido+=biblioteca.buscador.por_nombre(nombre)
        return libro_pedido
    def buscar_autor(self):
        autor=str(input("Ingrese el autor que busca:\n"))
        libro_pedido=[]
        for biblioteca in self.bibliotecas:
            libro_pedido+=biblioteca.buscador.por_autor(autor)
        return libro_pedido
    def buscar_biblioteca(self):
        for index,biblioteca in enumerate(self.bibliotecas):
            print("\t("+str(index+1)+") "+ biblioteca.nombre)
        indice=-1
        while indice<1 or indice>len(self.bibliotecas):
            try:
                indice=int(input("\nIngrese el número de la biblioteca que desea consultar:"))
            except ValueError:
                pass
        libro_pedido=self.bibliotecas[indice-1].buscador.por_biblioteca()
        return libro_pedido
if __name__=="__main__":
    s=Sistema()
    l=s.buscar_biblioteca()
    for libro in l:
        print(libro.nombre)