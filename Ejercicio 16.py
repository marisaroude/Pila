from pila import Pila


pila_episodioV = Pila()
pila_episodioVII = Pila() 
pila_interseccion = Pila()
pila_aux = Pila()


personajes_V = ['Luke','Obi','Yoda','Rey','Kylo Ren']
personajes_VII = ['Luke','Obi','Yoda']

for i in range(len(personajes_V)):
    personaje_V = personajes_V[i]
    pila_episodioV.apilar(personaje_V)

for j in range(len(personajes_VII)):
    personaje_VII = personajes_VII[j]
    pila_episodioVII.apilar(personaje_VII)


while (not pila_episodioV.pila_vacia()):  #Mientras q no este vacia la pila de episodio 5
    aux1 = pila_episodioV.desapilar()     #Se le asigna a aux 1 la pila 5 (para no perder los valores)
    while(not pila_episodioVII.pila_vacia()):  #Mientras no este vacia la pila de episodio 7
        aux2 = pila_episodioVII.desapilar()     #Se le asigna a aux 2 la pila 7 (para no perder los valores)
        if (aux1 == aux2):        #Si la aux 1 y aux 2 son iguales (aux1 y aux2 son variables simples de tipo string)
             pila_interseccion.apilar(aux1)  #A la pila interseccion se le apila el aux 1 (es igual q asignarle aux 2 ya q son mismos valores)
        pila_aux.apilar(aux2)               #A la pila auxiliar se le apila el aux 2 (en esta pila se van apilando los personajes que aparecen en ambas pilas.)
    while(not pila_aux.pila_vacia()):       #Mientras no este vacia la pila auxiliar (que contiene los personajes repetidos),
        pila_episodioVII.apilar(pila_aux.desapilar()) #se le apila a la pila episodio 7 esta misma pila

while (not pila_interseccion.pila_vacia()):
    print('El personaje que se repite es: ',pila_interseccion.desapilar())



