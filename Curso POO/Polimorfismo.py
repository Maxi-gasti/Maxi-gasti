class Gato():
    def Sonido(self):
        return 'Miau'
    
class Perro():
    def Sonido(self):
        return 'Guau'
    
def hacer_sonido(animal):
    print(animal.Sonido())

gato = Gato()
perro = Perro()


# Este polimorfismo el metodo funciona diferente para diferentes argumentos
hacer_sonido(gato)

# Este polimorfismo el metodo funciona diferente para diferentes Objetos
print(gato.Sonido())

# Mas ejemplos de polimorfismo

# --1--
num1 = 2
num2 = 4.4

r = num1+num2

print(r)
print(type(r)) # Es polimorfismo ya que python automaticamente se adapto al diferente tipo de dato(int y float), y nos devolvio el resultado

# --2--

def recorrer (elemento):
    for item in elemento:
        print(f'El elemento es: {item}')
        
lista1 = [1,2,3,4]
lista2 = ["Hola",'Como','Andas']

recorrer(lista1)
recorrer(lista2)

# Es poliformismo ya que aunque las 2 listas tienen diferentes tipos de datos lo toma igual
# Duck Typing - Enlaces dinamicos y estaticos - tipo real, tipo declarado