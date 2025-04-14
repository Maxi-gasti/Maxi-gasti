# Ejercicio 1 - Herencias

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def MostrarDatos(self):
        print(f'Nombre: {self.nombre}\n Edad: {self.edad}')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def MostrarGrado(self):
        print(f'Grado:{self.grado}')
        

Estudiante1 = Estudiante('Maxi',17,12)

Estudiante1.MostrarDatos()
Estudiante1.MostrarGrado()

# Ejercicio 2 - Herencia multiple y MRO

class Animal:
    def Comer(self):
        print("Comiendo..")

class Mamifero(Animal):
    def Amamantar(self):
        print('Amamantando..')

class Ave(Animal):
    def Volar(self):
        print('Volando..')
        

class Murcielago(Mamifero,Ave):
    def Comer(self):
        print('Comiendo..')
        
M1 = Ave()

M1.Comer()
M1.Volar()

print(Murcielago.mro())