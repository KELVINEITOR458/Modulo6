class Libro:
    contador_libros = 0

    def __init__(self, titulo, autor, paginas = 0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.contador_libros +=1

    def mostrar_info(self):
        print(self.__dict__)

    @staticmethod
    def es_grande(paginas):
        if paginas > 300:
            return print("Es grande?", True)
        else:
            return print("Es grande?", False)
        
    @classmethod
    def total_libros(cls):
        return cls.contador_libros        


