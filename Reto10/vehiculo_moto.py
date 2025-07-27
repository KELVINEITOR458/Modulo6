from vehiculo import Vehiculo
class Vehiculo_Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo = [],anio=0):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        super().descripcion()
