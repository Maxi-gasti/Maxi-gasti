class Celular:
    def __init__(self, marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f'Llamando desde: {self.modelo}')
    
    def Cortar(self):
        print(f'Cortaste desde: {self.modelo}')

celular1 = Celular('PepitoBobella',"Cualquiera",'0MP')
print(celular1.marca)
celular1.llamar()
celular1.Cortar()