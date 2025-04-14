# MRO: Metodo de resolucion de ordenes (Method Resolution Order)

class A:
    def Hablar(self):
        print('hola desde A')
        

class B(A):
    def Hablar(self):
        print('hola desde B')

class F:
    def Hablar(self):
        print('hola desde B')

class G:
    def Hablar(self):
        print('hola desde B')

class C(F,G):
    def Hablar(self):
        print('hola desde C')
        
        
class D(B,C):
    def Hablar(self):
        print('hola desde D')
        
# D>B>A>C>F>G
    
clase = D()

# Ver el MRO 
print(D.mro())

# Le doy la clase que quiero utilizar el metodo y le doy la instancia (objeto)
B.Hablar(clase)