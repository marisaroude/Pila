from pila import Pila

#definimos pilas con la clase Pila
pila_datos = Pila()
pila_aux = Pila()

valores = [ 2, 5 , 6 ,1, 0, -1, 10, 7] #definimos los valores a apilar.

for i in range (len(valores)-1):
    valor = valores [i]

    if (pila_datos.pila_vacia()): #si la pila de datos esta vacia
        pila_datos.apilar(valor) #procedemos a apilar un elemento de la lista valores
    else:
        if (valor >= pila_datos.elemento_cima()): #sino, si el valor es mayor o igual al elemento de la cima de la pila d datos
            pila_datos.apilar(valor)                #se apila el valor y se estaria haciendo de forma creciente
        else: 
            while (not pila_datos.pila_vacia() and pila_datos.elemento_cima() > valor): #sino, mientras la pila de datos no este vacia y el elemento de la cima de esta pila sea mayor al valor a apilar
                pila_aux.apilar(pila_datos.desapilar()) #procede a apilar en la pila auxiliar los valores de la pila datos
            pila_datos.apilar(valor) #luego sigue apilando valores en la pila original.

            while(not pila_aux.pila_vacia()): # mientras que no este vacia la pila auxiliar
                pila_datos.apilar(pila_aux.desapilar())  # se van apilando datos en la pila original de la pila auxiliar que utilizamos.

while (not pila_datos.pila_vacia()): #por ultimo, mientras la pila de datos, no este vacia
    print (pila_datos.desapilar()) # imprimimos como se va desapilando la pila datos.