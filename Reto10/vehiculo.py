class Vehiculo:
    def __init__(self, marca, modelo, anio = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def descripcion(self):
        print(self.__dict__)
        