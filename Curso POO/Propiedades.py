# Las propiedades son Decoradores!

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    # Getters - A traves de ellos podemos obtener informacion de las variables
    
    @property # Asigno el getter como una propiedad de la clase, haciendolo mas legible
    def nombre(self):
        return self.__nombre
    
    # Setters - A traves de ellos podemos cambiar la informacion de algunos valores
    
    @nombre.setter # Asigno el setter al decorador o Propiedad para poder acceder a ella
    def nombre(self,newnombre): # La funcion tiene que tener el mismo nombre
        self.__nombre = newnombre
    
    @nombre.deleter # Asigno un deleter al decorador o propiedad para poder eliminarlo
    def nombre(self): # La funcion tiene que tener el mismo nombre
        del self.__nombre


Maxi = Persona('Maxi',27)

nombre = Maxi.nombre
print(nombre)

Maxi.nombre = "Pepe"

nombre = Maxi.nombre
print(nombre)

del Maxi.nombre