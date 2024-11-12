planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
# print(planetas[-1])
# print(planetas[1:6])
# print(len(planetas[1:3]))


gravedad_planetas=[0.37, 0.90, 1, 0.37, 2.36, 0.91, 0.88, 1.12]
peso_bus = 124054 #Newtons en la tierra

print(f"En la tierra, un autobús de dos pisos pesa {peso_bus} N")
print(f"En Mercurio, un autobús de dos pisos pesa {peso_bus * gravedad_planetas[0]} N")

print(f"Lo mas liviano que sería un autobus en el sistema solar es: {peso_bus * min(gravedad_planetas)}")
print(f"Lo mas pesadp que sería un autobus en el sistema solar es: {peso_bus * max(gravedad_planetas)}")