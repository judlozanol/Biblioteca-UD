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
    
    def elegir_libro(self, listaLibros):
        if len(listaLibros)==0:
            print("El libro solicitado no se encuentra disponible en ninguna de nuestras bibliotecas.")
            input("Presione enter para continuear...")
            return False
        else: 
            indice=-1
            for index,libro in enumerate(listaLibros):
                print("("+str(index+1)+")")
                libro.mostrar_info()
            print("\n("+str(index+2)+") Salir")
            while indice>len(listaLibros)+1 or indice<1:
                try:
                    indice=int(input("Ingrese el número del libro que desea:"))
                    if indice==len(listaLibros)+1:
                        return False
                    if indice<len(listaLibros)+1 and indice>0:
                        libro=listaLibros[indice-1]
                        if libro.prestado:
                            indice=0
                            print("El libro no se encuentra disponible")
                            print("Datos del poseedor:")
                            libro.poseedor.mostrar_info()
                except ValueError:
                    pass
            return libro
    
    def prestar_libro(self, libro):
        if libro:
            for biblioteca in self.bibliotecas:
                if biblioteca.nombre==libro.entregar_biblioteca():
                    for libroB in biblioteca.libros:
                        if libroB.entregar_nombre()==libro.entregar_nombre():
                            archivo=open(biblioteca.txt)
                            texto=archivo.readlines()
                            archivo.close()
                            archivo=open(biblioteca.txt,"w")
                            prestamoCompletado=False
                            for linea in texto:
                                linea=linea.rstrip("\n")
                                contenido= linea.split("/")
                                if contenido[0]==libro.nombre and len(contenido)==2 and prestamoCompletado==False:
                                    prestamoCompletado=True
                                    linea=linea+"/"+self.usuario.nombre+"/"+self.usuario.documento+"/"+self.usuario.cargo+"/"+self.usuario.sede+"/"+self.usuario.carrera
                                archivo.write(linea+"\n")
                            archivo.close()
            print("Prestamo Exitoso!")
            input("Presione enter para continuear...")

if __name__=="__main__":
    s=Sistema()