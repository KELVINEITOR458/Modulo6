class Empleado:
    def __init__(self, nombre, salario_base = 0.0):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base
        
    
class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.20
    
class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.10
    
empleados = [
    EmpleadoTiempoCompleto("Ana", 1000),
    EmpleadoMedioTiempo("Luis", 800),
    EmpleadoTiempoCompleto("Juan", 200),
    EmpleadoMedioTiempo("Marcelo", 460),
    EmpleadoTiempoCompleto("Amanda", 230),
    EmpleadoMedioTiempo("Luisa", 730),
    EmpleadoTiempoCompleto("Daniel", 370),
    EmpleadoMedioTiempo("Joel", 100)  
]

for emp in empleados:
    print(f"{emp.nombre}: ${emp.calcular_salario()}")
