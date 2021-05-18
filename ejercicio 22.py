from pila import Pila

pila_BobaFett = Pila()
pila_DinDjarin = Pila()
pila_aux1 = Pila()
pila_aux2 = Pila()
acumulador1 = 0
acumulador2 = 0

class Mision_caza (object):
    def __init__(self,planeta_visitado,capturado,costo_recompensa):
        self.planeta_visitado = planeta_visitado
        self.capturado = capturado
        self.costo_recompensa = costo_recompensa

#Nave de Boba Fett
mision = Mision_caza('Marte','Yoda',15000)
pila_BobaFett.apilar(mision)
mision = Mision_caza('Jupiter','Han Solo',5000)
pila_BobaFett.apilar(mision)

#Nave de Din Djarin 
mision = Mision_caza('Saturno','Darth Vader',10000)
pila_DinDjarin.apilar(mision)
mision = Mision_caza('Neptuno','Obi',12000)
pila_DinDjarin.apilar(mision)

#punto a
#boba primero marte y despues jupiter
while(not pila_BobaFett.pila_vacia()):
    pila_aux1.apilar(pila_BobaFett.desapilar())

while(not pila_aux1.pila_vacia()):
    dato = pila_aux1.desapilar()
    print(dato.planeta_visitado)
    acumulador1 += dato.costo_recompensa
    pila_BobaFett.apilar(dato)

#dindjarin primero saturno y despues neptuno
while(not pila_DinDjarin.pila_vacia()):
    pila_aux1.apilar(pila_DinDjarin.desapilar())

while(not pila_aux1.pila_vacia()):
    dato = pila_aux1.desapilar()
    print(dato.planeta_visitado)
    acumulador2 += dato.costo_recompensa
    pila_DinDjarin.apilar(dato)


#Orden en que se cargan,        Como se deberian mostrar        Como se muestran:
# siendo marte el primero :      cargados en la pila:
# Marte                         Neptuno                         Jupiter
# Jupiter                       Saturno                         Marte
# Saturno                       Jupiter                         Neptuno
# Neptuno                       Marte                           Saturno


if (acumulador1 > acumulador2):
    print ('El cazarrecompensas que obtuvo mayor fortuna fue Boba Fett con ',acumulador1,'$')
else:
    print ('El cazarrecompensas que obtuvo mayor fortuna fue Din Djarin con ',acumulador2,'$')

#punto c 
posicion = 0
while(not pila_BobaFett.pila_vacia()):
    pila_aux1.apilar(pila_BobaFett.desapilar())

while(not pila_aux1.pila_vacia()):
    dato = pila_aux1.desapilar()
    posicion += 1
    if(dato.capturado == "Han Solo"):
        print('el numero de la mision es', posicion)
    pila_BobaFett.apilar(dato)

# while (not pila_BobaFett.pila_vacia()): 
#     print (pila_BobaFett.desapilar())