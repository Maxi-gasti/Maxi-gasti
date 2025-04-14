# El decorador es una funcion modificada a la cual le agregamos codigo, podemos elejir donde este codigo empezara.

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion() # Aca empieza el codigo añadido
        print('Despues de llamar a la funcion')
    
    return funcion_modificada # Devuelve la funcion Modificada

# 1ra Forma de usar Decorador

# def saludo():
#     print('Hola Dalto')
    

# saludo_M = decorador(saludo)
# saludo_M


# 2da Forma, mas legible

@decorador
def saludo():
    print('Hola Dalto como anadas')
    

saludo()