from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_Pepito = Laptop("Lenovo", "i7", 32)
Laptop_Maria = Laptop("Lenovo", "i7", 32, 600)
Laptop_Juanito = Laptop_Gaming("Asus", "I7", 4, "RTX 8GB")
laptop_chamba = Laptop_Business("Hp", "i3", 4, 500, 5)

#Imprimir un objeto
#print(laptop_Pepito.__dict__)
#print(laptop_Pepito.valor_final())
#print(f"El valor de descuento es: {laptop_Pepito.valor_descuento(30)}")

#print(Laptop.comparar_costo(laptop_Pepito, Laptop_Maria))

#for i in range(1, 1000):
#    asus_laptop = Laptop.asus_laptop(100)
#    print(asus_laptop.__dict__)

#print(Laptop_Juanito.realizar_diagnostico_sistema())

def imprimir_informe(Laptop):
    informe = Laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")

print("PEPITO:")
imprimir_informe(laptop_Pepito)
print("JUANITO:")
imprimir_informe(Laptop_Juanito)
