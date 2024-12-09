import tkinter as tk   
from tkinter import ttk
from PIL import Image, ImageTk
from laptop_business import  Laptop_Business
import random

class AppBusiness:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.images = ['C:\\Users\\usuario\\Desktop\\Krakedev\\Modulo6\\class1\\images_bussines\\download.jpg',
                       'C:\\Users\\usuario\\Desktop\\Krakedev\\Modulo6\\class1\\images_bussines\\download1.jpg',
                       'C:\\Users\\usuario\\Desktop\\Krakedev\\Modulo6\\class1\\images_bussines\\download2.jpg',
                       'C:\\Users\\usuario\\Desktop\\Krakedev\\Modulo6\\class1\\images_bussines\\download3.jpg']

        root.title("Ingresar Datos")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=3, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1)

        ttk.Label(self.root, text="Duración Bateria").grid(row=4, column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=4, column=1)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=5, column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row= 1, column=3, rowspan=6)
        

    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria.get(), self.almacenamiento.get(), self.duracion_bateria.get())
        self.laptops.append(nueva_laptop)

        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aleatorio()
    
    def mostrar_imagen_aleatorio(self):
        image_path = random.choice(self.images)
        imagen = Image.open(image_path)
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0,0, anchor=tk.NW, image = photo)
        self.canva.image = photo

        pass

root = tk.Tk()

app = AppBusiness(root)
root.mainloop()