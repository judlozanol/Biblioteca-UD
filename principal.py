from sistema import *
import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

s=Sistema()
clear()
print("\tBIENVENIDO A BIBLIOTECAS UD ;)")
print("\t      # #    #    # ###       ")
print("\t      # #    #    #    #      ")
print("\t      # #    #    #    #      ")
print("\t      # #    #    #    #      ")
print("\t      # ######    # ###       ")
input("Presione enter para iniciar seseión...")
clear()

s.iniciar_sesion()
opcion=0
while opcion<=0 or opcion>=4:
    try:
        clear()
        opcion=int(input("Que acción desea realizar:\n\t(1)Pedir un libro\n\t(2)Devolver un libro\n\t(3)Consultar libros prestados\n"))
    except ValueError:
        pass
clear()
if opcion==1:
    opcion=0
    while opcion<=0 or opcion>=4:
        try:
            clear()
            opcion=int(input("Seleccione el metodo de busqueda:\n\t(1)Busqueda por nombre\n\t(2)Busqueda por autor\n\t(3)Busqueda por biblioteca\n"))
        except ValueError:
            pass
    clear()
    if opcion==1:
        libros=s.buscar_libro()
    elif opcion==2:
        libros=s.buscar_autor()
    else:
        libros=s.buscar_biblioteca()
    clear()
    libro=s.elegir_libro(libros)
    s.prestar_libro(libro)
elif opcion==2:
    s.devolver_libro()
else:
    s.consultar_libros_prestados()
