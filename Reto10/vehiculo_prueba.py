from vehiculo import Vehiculo
from vehiculo_auto import Vehiculo_Auto
from vehiculo_moto import Vehiculo_Moto

carro1 = Vehiculo_Auto("si", "no", 2, 200)
carro2 = Vehiculo_Auto("sí", "sí", 4, 180)
moto1 = Vehiculo_Moto("a", "b", ["sí", "no"], 10)
moto2 = Vehiculo_Moto("x", "y", ["no", "sí"], 15)

vehiculos = [carro1, moto1, carro2, moto2]

for vehiculo in vehiculos:
    vehiculo.descripcion()