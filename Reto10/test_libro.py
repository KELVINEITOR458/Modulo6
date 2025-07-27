from libro import Libro

Libro1 = Libro("Kelvin", "Kelvin", 12)
Libro2 = Libro("No", "No", 1200)
Libro3 = Libro("Si", "si", 400)

Libro1.mostrar_info(), Libro1.es_grande(Libro1.paginas)
Libro2.mostrar_info(), Libro2.es_grande(Libro2.paginas)
Libro3.mostrar_info(), Libro3.es_grande(Libro3.paginas)
print(Libro.total_libros())