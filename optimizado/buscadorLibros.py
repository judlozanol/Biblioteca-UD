"""El buscador de libros recibe una lista de libros y devuelve dicha lista filtrada"""
class BuscadorLibros:
    def __init__(self,biblioteca):
        self.librosEncontrados=[]
        self.listaLibros= biblioteca.libros
    def limpiar_librosEncontrados(self):
        self.librosEncontrados=[]

    def por_autor(self,autor):
        self.limpiar_librosEncontrados()
        for libro in self.listaLibros:
            if libro.entregar_autor()==autor:
                self.librosEncontrados.append(libro)
        return self.librosEncontrados
    def por_nombre(self,nombre):
        self.limpiar_librosEncontrados()
        for libro in self.listaLibros:
            if libro.entregar_nombre()==nombre:
                self.librosEncontrados.append(nombre)
        return self.librosEncontrados
    def por_biblioteca(self):
        self.limpiar_librosEncontrados()
        self.librosEncontrados=self.listaLibros
        return self.librosEncontrados