""" 
Ejercicio 2
Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente
"""

class Exponente():
    def __init__(self, base=0, exponente=0): 
        self.base = base 
        self.exponente = exponente

    def calculadora(self): 
        self.resultado = self.base ** self.exponente 

    def imprimir(self): 
        print("El resultado es: {}".format(self.resultado))

Resultado = Exponente(3,4)
Resultado.calculadora()
Resultado.imprimir()
