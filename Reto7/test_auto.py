from Auto import Auto

carro1 = Auto.auto_chevrolet(10000)
carro2 = Auto.auto_toyota(20000)

print(carro1.__dict__)
print(carro2.__dict__)
print(Auto.comparar_marca(carro1, carro2))
print(Auto.comparar_km(carro1, carro2))