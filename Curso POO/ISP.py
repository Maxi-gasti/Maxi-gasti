# Interface Segretion Principle - Princio de segreacion de interfaz
# Cuando trabajamos con interfaces (clases abstractas), evitar que otras clases utilizen interfaces que ocupan metodos innecesarios.
# Robot no necesita comer o dormir.

from abc import ABC, abstractmethod

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador,Comedor,Durmiente):
    
    def dormir(self):
        return 'Durmiendo...'
    
    def trabajar(self):
        return 'Trabajando..'
    
    def comer(self):
        return 'Comer.. '

class Robot(Trabajador):
    
    def trabajar(self):
        return 'trabajando..'


pedro = Humano()
Robi = Robot()

print(pedro.comer())
print(pedro.dormir())
print(pedro.trabajar())
print(Robi.trabajar())