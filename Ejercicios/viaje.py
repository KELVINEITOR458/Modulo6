import random
pais = input("Ingresa al pais que te gustaría viajar: ")
velocidad = random.randint(0, 140)

if pais == "Ecuador":
    zona = input("Ingresa la zona a la que quieres entrar: ")
    print(f"Velocidad: {velocidad}km/h")
    if zona == "urbana":
        if velocidad > 50 or velocidad < 10:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
    elif zona == "rural":
        if velocidad > 70 or velocidad < 51:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
    elif zona == "perimetral":
        if velocidad > 90 or velocidad < 71:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
elif pais == "Colombia":
    zona = input("Ingresa la zona a la que quieres entrar: ")
    print(f"Velocidad: {velocidad}km/h")
    if zona == "urbana":
        if velocidad > 30 or velocidad < 10:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
    elif zona == "rural":
        if velocidad > 80 or velocidad < 31:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
    elif zona == "perimetral":
        if velocidad > 100 or velocidad < 81:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
elif pais == "Peru":
    zona = input("Ingresa la zona a la que quieres entrar: ")
    print(f"Velocidad: {velocidad}km/h")
    if zona == "urbana":
        if velocidad > 40 or velocidad < 10:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
    elif zona == "rural":
        if velocidad > 60 or velocidad < 41:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")
    elif zona == "perimetral":
        if velocidad > 120 or velocidad < 61:
            print("No estas yendo a la velociad adecuada.")
        else:
            print("Disfruta tu viaje.")

