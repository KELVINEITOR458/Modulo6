datos = []

cantidad = int(input("Cuantos datos vas a ingresar? "))

for i in range(cantidad):
    dato = input(f"Ingrese el dato: ")
    

    if dato.isnumeric():
        datos.append(int(dato))
    elif dato.isdecimal():
        datos.append(float(dato))
    else:
        datos.append(dato)


        

print(f"Su lista es: {datos}")
