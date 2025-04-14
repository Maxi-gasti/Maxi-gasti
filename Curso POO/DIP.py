# Dependency Inversion Principle - Principio de inversion de dependencias
# Que las clases de bajo nivel no dependan de las de alto sino de una clase abstracta


# class Diccionario:
#     def verificar_palabra(self,palabra):
#         #Logica para verificar palabras
#         pass
        


# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self,texto):
#         # Usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self,palabra):
        #Logica para verificar palabras si esta en
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        #Logica para verificar palabras si esta en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self,verificador):
        self,verificador = verificador
    
    def corregir_texto(self,texto):
        # usamos el verificador para corregir texto
        pass 
    

corrector = CorrectorOrtografico(Diccionario)