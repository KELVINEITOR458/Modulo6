class Auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(self.__dict__)
    
    def actualizar_kilometraje(self, new_kilometraje):
        if new_kilometraje < self.kilometraje :
            print("No se puede reducir el kilometraje")
        else:
            self.kilometraje = new_kilometraje
            print(self.__dict__)

    def realizar_viaje(self, km_viaje1, km_viaje2):
        if km_viaje1 < 0 | km_viaje2 < 0:
            print("La cantidad de kilometros debe ser positiva")
        else:
            new_km = km_viaje1 + km_viaje2
            self.kilometraje =+ new_km
            print(self.__dict__)
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje > 20000 & self.kilometraje < 100000:
            print("Ya estoy usado")
        elif self.kilometraje > 100000:
            print("Estoy cansado jefe")

    @classmethod
    def auto_toyota(cls, kilometraje):
        marca = "Toyota"
        modelo = "Si"
        año = "2024"
        return cls(marca, modelo, año, kilometraje)
    
    @classmethod
    def auto_chevrolet(cls, kilometraje):
        marca = "Chevrolet"
        modelo = "No"
        año = "2024"
        return cls(marca, modelo, año, kilometraje)

    @staticmethod
    def comparar_km(carro1, carro2):
        if carro1.kilometraje == carro2.kilometraje:
            return "Los carros tienen el mismo kilometraje"
        else:
            return "Los carros tienen diferente kilometraje"
        
    @staticmethod
    def comparar_marca(carro1, carro2):
        if carro1.marca == carro2.marca:
            return "Los carros tienen la mismo marca"
        else:
            return "Los carros tienen diferente marca"



#hola = Auto("Toyota", "Nose", "2020")
#hola.mostrar_informacion()
#nuevo_kilometraje = int(input("Ingrese el nuevo kilometraje: "))
#hola.actualizar_kilometraje(nuevo_kilometraje)
#viaje1 = int(input("Ingrese la distancia viaje 1: "))
#viaje2 = int(input("Ingrese la distancia viaje 2: "))
#hola.realizar_viaje(viaje1, viaje2)
#hola.estado_auto()