class Miclase():
    def __init__(self):
        self.__Atrivuto_privado = "Quee" #Atributo privado por __
        
    def __hablar(self): # Metodo privado por __
        print("hola")

objeto = Miclase()
#print(objeto.__Atrivuto_privado)


# --------------------------------------

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    # Getters - A traves de ellos podemos obtener informacion de las variables
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    # Setters - A traves de ellos podemos cambiar la informacion de algunos valores
    
    def set_nombre(self,newnombre):
        self.__nombre = newnombre
    
dalto = Persona("Lucas",21)

nombre = dalto.get_nombre()
edad = dalto.get_edad()

dalto.set_nombre("Maximo")
nombre = dalto.get_nombre()
print(f'Nombre: {nombre} Edad: {edad}')