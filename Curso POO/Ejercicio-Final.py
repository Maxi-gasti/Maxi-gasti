# from textblob import TextBlob

# class AnalizadorDeSentimientos:
#     def analizar_sentimientos(self, texto):
#         analisis = TextBlob(texto)
#         print(analisis.sentiment.polarity)
#         if analisis.sentiment.polarity == 1:
#             return "\x1b[1;32m"+'muy positivo'+"\x1b[0;37m"
#         elif analisis.sentiment.polarity <= 0.9 and analisis.sentiment.polarity > 0.3:
#             return "\x1b[1;32m"+'positivo'+"\x1b[0;37m"
#         elif analisis.sentiment.polarity <= 0.3 and analisis.sentiment.polarity > 0:
#             return "\x1b[1;32m"+'algo positivo'+"\x1b[0;37m"
#         elif analisis.sentiment.polarity == 0:
#             return "\x1b[1;33m"+'neutral'+"\x1b[0;37m"
#         elif analisis.sentiment.polarity >= -0.3 and analisis.sentiment.polarity < 0:
#             return "\x1b[1;31m"+'algo negativo'+"\x1b[0;37m"
#         elif analisis.sentiment.polarity >= -0.9 and analisis.sentiment.polarity < -0.3:
#             return "\x1b[1;31m"+'negativo'+"\x1b[0;37m"
#         else:
#             return "\x1b[1;31m"+'muy negativo'+"\x1b[0;37m"
        
# analizador = AnalizadorDeSentimientos()



# while True:
#     user_prompt = input("\x1b[1;33m"+"Dime algo y lo analizo: "+"\x1b[0;37m")
#     resultador = analizador.analizar_sentimientos(user_prompt) # Solo funciona en ingles
#     print("\n",resultador)
    

# -- OPTIMIZADO con el principio SOLID
# respetamos 3 principios aqui SRP,OCP,ISP

from textblob import TextBlob

# SRP ya que Sentimiento se encarga de representar el sentimiento y color segmentandolo de analizador
# OPC ya que AnalizadorDeSentimientos usa rangos, el cual esta abierto a modificacion
# IPS ya que AnalizadorDeSentimientos no Depende de TextBlob sino de Sentimiento y rangos

class Sentimiento:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return '\x1b[1;{}m{}\x1b[0;37m'.format(self.color,self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos
    
    def analizar_sentimiento(self, polaridad):
        analisis = TextBlob(polaridad)
        polaridad = analisis.sentiment.polarity
        print(polaridad)
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy Negativo", "31")

rangos = [
    ((-0.9, -0.3), Sentimiento("negativo","31")),
    ((-0.3, -0.1), Sentimiento("algo negativo","31")),
    ((-0.1, 0.1), Sentimiento("neutral","33")),
    ((0.1, 0.3), Sentimiento("algo positivo","32")),
    ((0.3, 0.9), Sentimiento("positivo","32")),
    ((0.9, 1), Sentimiento("muy positivo","32")),
]
        
analizador = AnalizadorDeSentimientos(rangos)



while True:
    user_prompt = input("\x1b[1;33m"+"Dime algo y lo analizo: "+"\x1b[0;37m")
    sentimiento = analizador.analizar_sentimiento(user_prompt) # Solo funciona en ingles
    print(sentimiento)