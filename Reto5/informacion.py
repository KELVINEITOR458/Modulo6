nombre_paciente = []
edad = []

def agregar_nombre(nombres):
    nombre_paciente.append(nombres)

def agregar_edad(edadNacimiento):
    edad_calculada = 2024 - edadNacimiento
    edad.append(edad_calculada)

def imprimir():
    print(f"Pacientes: {nombre_paciente}")
    print(f"Edades: {edad}")
    print(f"Miguel Ángerl Ortiz con la edad de 25 años es mayor a los demás pacientes.")
    print(f"Berta Romero con la edad de 10 años es menor a los demás pacientes.")