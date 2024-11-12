menu = ["Seco de pollo", "Seco de carne", "Ceviche", "Encebollado"]

print("Bienvenido al menú de segunda es todo")
eleccion = int(input("¿Qué deseas hacer? 1:Añadir Plato - 2:Buscar menú - 3:Eliminar plato - 4:Mostrar platos: "))
if eleccion == 1:
    plato_añadir = input("Escriba el nombre del plato que quiere que sea añadido: ")
    print(plato_añadir)
    menu.append(plato_añadir)
    print(f"Su plato se a añadido con éxito: {menu[-1]}")
elif eleccion == 2:
    print(menu)
    indice_plato = input("Escriba el plato que desea buscar: ")
    if indice_plato == menu[0]:
        print(f"Plato encontrado: {menu[0]}")
    elif indice_plato == menu[1]:
        print(f"Plato encontrado: {menu[1]}")
    elif indice_plato == menu[2]:
        print(f"Plato encontrado: {menu[2]}")
    elif indice_plato == menu[3]:
        print(f"Plato encontrado: {menu[3]}")
elif eleccion == 3:
    print(menu)
    eliminar_plato = input("Escriba el plato que desea eliminar: ")
    menu.remove(eliminar_plato)
    print(f"Plato eliminado con éxito {menu}")
elif eleccion == 4: 
    print(menu)