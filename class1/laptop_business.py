from laptop import Laptop
class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        diagnostico_mas = self.realizar_diagnostico_mas()
        resultado_diagnostico["Detalles exta:"] = diagnostico_mas
        conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Verificar Conectividad: "] = conectividad
        return resultado_diagnostico

    def realizar_diagnostico_mas(self):
        return f"Almacenamiento: {self.almacenamiento}, Batería: {self.duracion_bateria} " 
    
    def verificar_conectividad_red(self):
        print("ACCESO A SERVIDORES:")
        print(True)

        print("WIFI:")
        print(True)

        print("LATENCIA")

        for i in range(10):
            print("Respuesta desde 192.140.100.1: bytes=32 tiempo=71ms TTL=116")

            
        

        
        