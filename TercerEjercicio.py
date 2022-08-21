"""
Ejercicio 3

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

"""

class Calcular(): 
    def __init__(self): 
        self.valor1 = int(input("Ingrese valor: "))
        self.valor2 = int(input("Ingrese valor: "))

    def suma(self): 
        self.suma = self.valor1 + self.valor2
        return "El resultado es: ",self.suma
    
    def resta(self): 
        self.resta = self.valor1 - self.valor2
        return "El resultado es: ",self.resta
    
    def multi(self): 
        self.multi = self.valor1 * self.valor2
        return "El resultado es: ",self.multi 
    
    def division(self): 
        self.division = self.valor1 / self.valor2
        return "El resultado es: ",self.division

Calculadora = Calcular()
print(Calculadora.suma())
print(Calculadora.resta())
print(Calculadora.multi())
print(Calculadora.division())