# Principio Liskov's Substitution Principle - Princio de sustitucion de Liskov
# Barba liskov

# class Pajaro:
#     def volar(self):
#         return 'Estoy volando'
    
    
# class Pinguino(Pajaro):
#     def volar(self):
#         return 'No puedo volar'
    

# def hacer_volar(pajaro = Pajaro):
#     return pajaro.volar()

# print(hacer_volar(Pinguino()))

class ave:
    pass

class AveVoladora(ave):
    def volar(self):
        return 'Estoy volando'


class AveNoVoladora(ave):
    def volar(self):
        return 'Estoy volando'