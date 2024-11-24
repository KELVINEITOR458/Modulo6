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


hola = Auto("Toyota", "Nose", "2020")
hola.mostrar_informacion()
nuevo_kilometraje = int(input("Ingrese el nuevo kilometraje: "))
hola.actualizar_kilometraje(nuevo_kilometraje)
viaje1 = int(input("Ingrese la distancia viaje 1: "))
viaje2 = int(input("Ingrese la distancia viaje 2: "))
hola.realizar_viaje(viaje1, viaje2)
hola.estado_auto()