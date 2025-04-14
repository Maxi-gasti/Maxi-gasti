class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
        
    def estudiar(self):
        print('Estudiando....')
        
nombre = input('Igrense su nombre: ')
edad = input('Ingrese su edad: ')
grado = input('Ingrese su grado: ')

estudiante1 = Estudiante(nombre,edad,grado)

print(f'''
      Datos del estudiante:\n\n
      Nombre: {estudiante1.nombre}\n
      Edad: {estudiante1.edad}\n
      Grado: {estudiante1.grado}\n''')

estu = input("Estudiar?")

if estu.lower() == 'estudiar':
    estudiante1.estudiar()