""" 

Ejercicio 1

Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


""" 

class Estudiante(): 
    def __init__(self, nombre, nota): 
        self.nombre = nombre 
        self.nota = nota

    def imprimir(self): 
        print("Nombre: {} \nNota: {}".format(self.nombre , self.nota))         
        
    def boleta(self): 
        if self.nota < 10: 
            print("¡REPROBADO!")
        else: 
            print("¡Felicitaciones, aprobaste! ")

estudiante1 = Estudiante("Luis Miguel" , 20)
estudiante1.imprimir()
estudiante1.boleta()