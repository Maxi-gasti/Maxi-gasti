#Clase padre
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def Hablar(self):
        print("HOLAAAA")
        
#2 Clase Padre
class Artista:
    def __init__(self,Habilidad):
        self.Habilidad = Habilidad
    
    def Mostrar(self):
        print(f'{self.Habilidad}')

#Herencia simple - Hereda los atributos y metodos de la clase padre.

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad, trabajo,salario):
        self.trabajo = trabajo
        self.salario = salario
        super().__init__(nombre, edad, nacionalidad)
        
Empeado1 = Empleado("Pablo",28,'Argentino','diseño',10000)
Empeado1.Hablar()



#Herencia multiple - Hereda los atributos y Metodos de sus diversos padres

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,Habilidad):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, Habilidad)
    
    def Hablar(self):
        print("Hola")
    
    def Presentarse(self):
        # Si parte de las clases padre es sobreescrita en la hija podemos seguir accediendo a su herencia usando super()
        self.Hablar() # Utilizo la funcion de EmpleadoArtista
        super().Hablar() # Utilizo la funcion de PERSONA
        
        
Pedro = EmpleadoArtista("pedro",17,"peruano","programador")

print(Pedro.Habilidad)
Pedro.Presentarse()

# Forma de como confirmar si una clase es subclase de otra

#                  (Subclase)  ,  (Padre)
print(issubclass(EmpleadoArtista,Artista)) # True

# Forma de como confirmar si una instancia es de una clase

#              (Instancia/Objeto),(Clase)
print(isinstance(Pedro,Artista)) # true - Si la clase es una clase padre de la instancia devuelve True tambien por arbol jerarquico.
