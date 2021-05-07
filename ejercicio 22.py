from pila import Pila


class Personajes(object):
    def __init__(self,personaje,cantidad_peliculas):
        self.personaje = personaje
        self.cantidad_peliculas = cantidad_peliculas

        

pila_personajesMCU = Pila()
pila_aux = Pila()
    
personajes = Personajes('Capitán América',6)
pila_personajesMCU.apilar(personajes)
personajes = Personajes ('Rocket Raccoon',2)
pila_personajesMCU.apilar(personajes)
personajes = Personajes ('Iron Man',3)
pila_personajesMCU.apilar(personajes)
personajes = Personajes('Groot',5)
pila_personajesMCU.apilar(personajes)
personajes = Personajes('Thor',4)
pila_personajesMCU.apilar(personajes)
personajes = Personajes('Loki',1)
pila_personajesMCU.apilar(personajes)
personajes = Personajes('Viuda Negra',6)
pila_personajesMCU.apilar(personajes)



i = pila_personajesMCU.elemento_cima()

#punto a
for i in range (pila_personajesMCU.tamanio()):
    x = pila_personajesMCU.desapilar()
    if (x.personaje == 'Rocket Raccoon'):
        print('El personaje Rocket Raccoon se encuentra en la posicion: ', i)
    if (x.personaje == 'Groot'):
        print('El personaje Groot se encuentra en la posicion: ', i)
    else: pila_aux.apilar(x) 

while (not pila_aux.pila_vacia()):
    pila_personajesMCU.apilar(pila_aux.desapilar())

#punto b
print('Los personajes que participaron en mas de 5 peliculas de la saga son: ')

for j in range (pila_personajesMCU.tamanio()):
    x = pila_personajesMCU.desapilar()
    if (x.cantidad_peliculas > 5):
        print (x.personaje,' aparece en ',x.cantidad_peliculas,' peliculas.')
    if (x.personaje == 'Viuda Negra'):
        cant = x.cantidad_peliculas

   
print('Cantidad de peliculas en las que aparece Viuda Negra: ', cant)




while (not pila_personajesMCU.pila_vacia()): 
    print (pila_personajesMCU.desapilar())

