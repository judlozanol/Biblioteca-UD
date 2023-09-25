#Sera quien maneje los procesos dentro de todo
from bibliotecas import *
from usuarios import *
from libro import Libro
class Sistema():
    def __init__(self):
        self.bibliotecas=[Ingenieria(),Paiba(),Artes()]
        self.usuario=Usuario()

    def iniciar_sesion(self):
        lista=[Admon(),Docente(),Estudiante()]
        indice=int(input("Ingrese el cargo al que pertenece:\n\t(1)Administrativo\n\t(2)Docente\n\t(3)Estudiante\n"))
        self.usuario= lista[indice-1]
        self.usuario.llenar_usuario()

    def buscar_libro(self):
        nombre=str(input("Ingrese el nombre del libro que busca:\n")).upper()
        libro_pedido=[]
        for i in range(len(self.bibliotecas)):
            for j in range(len(self.bibliotecas[i].libros)):
                libro=self.bibliotecas[i].libros[j]
                if libro.nombre.upper()==nombre:
                    libro_pedido.append(libro)
        return libro_pedido
    
    def buscar_autor(self):
        autor=str(input("Ingrese el autor que busca:\n")).upper()
        libro_pedido=[]
        for i in range(len(self.bibliotecas)):
            for j in range(len(self.bibliotecas[i].libros)):
                libro=self.bibliotecas[i].libros[j]
                if libro.autor.upper()==autor:
                    libro_pedido.append(libro)
        return libro_pedido
    
    def buscar_biblioteca(self):
        print("Bibliotecas en nuestro sistema")
        for i in range(len(self.bibliotecas)):
                print("("+str(i+1)+") "+self.bibliotecas[i].nombre)        
        indice=int(input("Ingrese el número de la biblioteca que desea consultar:"))
        libro_pedido=[]
        for j in range(len(self.bibliotecas[indice-1].libros)):
            libro=self.bibliotecas[indice-1].libros[j]
            libro_pedido.append(libro)
        return libro_pedido
    
    def elegir_libro(self, libro_pedido):
        if len(libro_pedido)==0:
            print("El libro solicitado no se encuentra disponible en ninguna de nuestras bibliotecas")
            input("Presione enter para continuear...")
            return False
        else: 
            indice=0
            valido=False
            for i in range(len(libro_pedido)):
                print("("+str(i+1)+")")
                print("\tNombre: "+libro_pedido[i].nombre+"\n\tAutor: "+libro_pedido[i].autor+"\n\tBiblioteca: "+libro_pedido[i].biblioteca)
            print("\n("+str(i+2)+") Salir")
            while(indice>len(libro_pedido)+1 or indice<1):
                try:
                    indice=int(input("Ingrese el número del libro que desea:"))
                    if indice==len(libro_pedido)+1:
                        return False
                    if indice<len(libro_pedido)+1 and indice>0:
                        valido=True
                        libro=libro_pedido[indice-1]
                        if libro.prestado and valido:
                            indice=0
                            valido=False
                            print("El libro no se encuentra disponible.\nDatos del poseedor:\n\tNombre: "+libro.poseedor.nombre+"\n\tCargo: "+libro.poseedor.cargo+"\n\tSede: "+libro.poseedor.sede+"\n\tCarrera: "+libro.poseedor.carrera)
                except ValueError:
                    pass
            return libro
    def prestar_libro(self, libro:type[Libro]):
        if libro==False:
            pass
        else:
            for i in range(len(self.bibliotecas)):
                if self.bibliotecas[i].nombre==libro.biblioteca:
                    for j in range(len(self.bibliotecas[i].libros)):
                        if self.bibliotecas[i].libros[j].nombre==libro.nombre:
                            archivo=open(self.bibliotecas[i].txt)
                            texto=archivo.readlines()
                            archivo.close()
                            archivo=open(self.bibliotecas[i].txt,"w")
                            for linea in texto:
                                linea=linea.rstrip("\n")
                                contenido= linea.split("/")
                                if contenido[0]==libro.nombre and len(contenido)==2:
                                    linea=linea+"/"+self.usuario.nombre+"/"+self.usuario.cargo+"/"+self.usuario.sede+"/"+self.usuario.carrera+"/"+str(self.usuario.documento)
                                archivo.write(linea+"\n")
                            archivo.close()
            print("Prestamo Exitoso!")
            input("Presione enter para continuear...")
    def libros_prestados(self):
        libros_prestados=[]
        for i in range(len(self.bibliotecas)):
            for j in range(len(self.bibliotecas[i].libros)):
                libro=self.bibliotecas[i].libros[j]
                if libro.prestado:
                    if libro.poseedor.documento==self.usuario.documento:
                        libros_prestados.append(libro)
        return libros_prestados
    
    def consultar_libros_prestados(self):
        libros_prestados=self.libros_prestados()
        if len(libros_prestados)==0:
            print("Ningún libro que devolver ;)")
        else: 
            print("Libros prestados a "+self.usuario.nombre)
            for i in range(len(libros_prestados)):
                print("("+str(i+1)+")")
                print("\tNombre: "+libros_prestados[i].nombre+"\n\tAutor: "+libros_prestados[i].autor+"\n\tBiblioteca: "+libros_prestados[i].biblioteca)
        input("Presione enter para continuear...")
            
    def escoger_libro_prestado(self):
        libros_prestados=self.libros_prestados()
        if len(libros_prestados)==0:
            print("Ningún libro que devolver ;)")
            input("Presione enter para continuear...")
            return False
        else:
            indice=0
            for i in range(len(libros_prestados)):
                print("("+str(i+1)+")")
                print("\tNombre: "+libros_prestados[i].nombre+"\n\tAutor: "+libros_prestados[i].autor+"\n\tBiblioteca: "+libros_prestados[i].biblioteca)
            print("\n("+str(i+2)+") Salir")
            while(indice>len(libros_prestados)+1 or indice<1):
                try:
                    indice=int(input("Ingrese el número del libro que desea devolver:"))
                    if indice==len(libros_prestados)+1:
                        return False
                    elif indice<len(libros_prestados)+1 and indice>0:
                        libro=libros_prestados[indice-1]
                        return libro
                except ValueError:
                    pass
    def devolver_libro(self):
        libro=self.escoger_libro_prestado()
        if libro==False:
            pass
        else:
            ejecutado=False
            for i in range(len(self.bibliotecas)):
                if self.bibliotecas[i].nombre==libro.biblioteca:
                    for j in range(len(self.bibliotecas[i].libros)):
                        libro_iterante=self.bibliotecas[i].libros[j]
                        if libro_iterante.nombre==libro.nombre and ejecutado==False and libro_iterante.prestado==True:
                            ejecutado=True
                            archivo=open(self.bibliotecas[i].txt)
                            texto=archivo.readlines()
                            archivo.close()
                            archivo=open(self.bibliotecas[i].txt,"w")
                            for linea in texto:
                                linea=linea.rstrip("\n")
                                contenido= linea.split("/")
                                if contenido[0]==libro.nombre and len(contenido)==7 and int(contenido[6])==self.usuario.documento :
                                    linea=libro_iterante.nombre+"/"+libro_iterante.autor
                                archivo.write(linea+"\n")
                            archivo.close()

            print("Devolución Exitosa!")
            input("Presione enter para continuear...")
    def actualizar_bilioteca(self):
        for i in range(len(self.bibliotecas)):
            self.bibliotecas[i].libros=[]
            self.bibliotecas[i].agregar_libros()
            
        