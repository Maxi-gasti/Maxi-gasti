class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self): # Utilizado para reconstruir una representacion del objeto
        return f'Persona("{self.nombre}",{self.edad})'
    
    def __add__(self,otro): # Permite la suma de objetos entre si, asignando como se comportan
        nuevoValor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevoValor)

maxi = Persona('Maxi',17)

repre = repr(maxi) #Creo una representacion del objeto
resultado = eval(repre) # la evaluo

print(resultado) # la muestro
print(maxi)

pedro = Persona('Pedro',30)
maria = Persona('Maria',21)

resultado = pedro + maria
print(resultado) # DEVUELVE Persona(nombre=Maxi,edad=17) YA QUE LO DEFINIMOS COMO RETRUN EN EL STR !!!
print(resultado.edad)