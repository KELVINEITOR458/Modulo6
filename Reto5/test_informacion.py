import informacion

for i in range(13):
    nombres = input("Ingrese su nombre y apellido: ")
    informacion.agregar_nombre(nombres)
    edad = int(input("Ingrese su edad: "))
    informacion.agregar_edad(edad)
informacion.imprimir()