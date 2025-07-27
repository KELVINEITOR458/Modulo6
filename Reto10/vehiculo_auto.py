from vehiculo import Vehiculo
class Vehiculo_Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas = 0, anio=0):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
       super().descripcion()

    