# Principio Open Closed Principle - Princio de Open Closed
# Este no significa fragmentar los metodos como el SRP sino que es Abierto a agregar y cerrado a modificar
# Ya que agregamos en algun futuro clases para una funcion nueva, pero no modificamos la clase sino que agregamos otra que herede de esa
# es decir esta abierto a agregar nuevas funciones pero cerrado a modificar la clase padre.

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def Notificar(self):
        raise NotImplementedError
    
    
class NotificarEmail(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por MAIL a {self.usuario.email}')

    
class NotificarWhatsapp(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por Whatsapp a {self.usuario.Whatsapp}')

    
class NotificarSMS(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por SMS a {self.usuario.SMS}')

    
class NotificarTwitter(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por Twitter a {self.usuario.twitter}')