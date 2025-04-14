# La clase abstracta es una receta, es una plantilla para otras clases como nombre,edad,etc. este no puede ser instanciado
# La clase abstracta es como un contrato, si no tiene los metodos abstractos de la clase no se dejara ejecutar. Permite dejar todas sus herencias iguales
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self): # No es abstracta ya que todas se presentan igual
        print(f'Hola me llamo: {self.nombre} y tengo {self.edad} años')


class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f'Estoy Estudiando: {self.actividad}')


class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f'Estoy Trabajando actualmente: {self.actividad}')

Maxi = Estudiante('Maxi',17,'Hombre','Programacion')
Maxi.presentarse()
Maxi.hacer_actividad()

Pedro = Trabajador('Pedro',21,'Hombre','Programacion')
Pedro.presentarse()
Pedro.hacer_actividad()