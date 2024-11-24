from laptop import Laptop

laptop_Pepito = Laptop("Lenovo", "i7", 32)
Laptop_Maria = Laptop("Lenovo", "i7", 32, 600)
#Imprimir un objeto
#print(laptop_Pepito.__dict__)
#print(laptop_Pepito.valor_final())
#print(f"El valor de descuento es: {laptop_Pepito.valor_descuento(30)}")

print(Laptop.comparar_costo(laptop_Pepito, Laptop_Maria))

for i in range(1, 1000):
    asus_laptop = Laptop.asus_laptop(100)
    print(asus_laptop.__dict__)

