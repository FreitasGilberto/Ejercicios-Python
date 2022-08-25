""" 
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
"""

from tkinter import MOVETO


class Fabrica(): 
    def __init__(self, llantas, color, precio): 
        self.llantas = llantas 
        self.color = color
        self.precio = precio

class Carro(Fabrica): 
    def datos(self): 
        print("La cantidad de llantas es de: ",self.llantas) 
        print("El color del carro es: ",self.color)
        print("El precio del carro es de: ",self.precio)

class Moto(Fabrica): 
    def datos(self): 
        print("La cantidad de llantas de la moto es de: ",self.llantas)
        print("El color de la moto es: ",self.color)
        print("El precio de la moto es: ",self.precio)

moto = Moto(2,"Negro", 4000)
moto.datos()

carro = Carro(4,"Blanco", 5000)
carro.datos()

