import os

class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad {self.velocidad})'
    
    def __add__(self,otroPJ):
        new_nombre = self.nombre + '-' + otroPJ.nombre
        new_fuerza = round(((self.fuerza+otroPJ.fuerza)/2)**2)
        new_velocidad = round(((self.fuerza+otroPJ.velocidad)/2)**2)
        return Personaje(new_nombre,new_fuerza,new_velocidad)
    
def LimpiarTerminal():
    os.system("cls" if os.name == "nt" else "clear")
    
def CrearPersonaje():
    pj_nombre = input('Ingrese el nombre: ')
    pj_fuerza = float(input('Ingrese el fuerza: '))
    pj_velocidad = float(input('Ingrese el velocidad: '))
    return Personaje(pj_nombre,pj_fuerza,pj_velocidad)

def Mostrar_Personajes():
    if personajes:
        print('Personajes disponibles: ')
        for i in personajes:
            print(i)
            print(' - ')
    else:
        print('No hay personajes')

personajes = []

while True:
    print('Ingrese una opcion: \n1. Crear Personaje\n2. Fusionar Personaje\n3. Mostrar Personajes\n4. Salir')
    opcion = int(input())
    if opcion == 1:
        LimpiarTerminal()
        new_personaje = CrearPersonaje()
        personajes.append(new_personaje)
        print('Personaje creado exitosamente!')
    elif opcion == 2:
        LimpiarTerminal()
        if len(personajes) < 2:
            print('Se necesitan almenos 2 personajes!')
        else:
            print(personajes)
            pj1 = int(input('Elija al primer personaje: '))
            pj2 = int(input('Elija al segundo personaje: '))
            if pj1 != pj2:
                fusion = personajes[pj1-1]+personajes[pj2-1]
                personajes.append(fusion)
                print(f'Nuevo personaje: {fusion}!')
            else:
                print('No puede elejir 2 personajes iguales!')
    elif opcion == 3:
        LimpiarTerminal()
        Mostrar_Personajes()
    elif opcion == 4:
        print('Saliendo...')
        break
    else:
        LimpiarTerminal()
        print('Opcion Invalida!')
        

# Goku = Personaje('goku',100,100)
# vegeta = Personaje('vegeta',100,120)
# fusion = Goku+vegeta
# print(fusion)