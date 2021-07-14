lista = [1,2,"verde", 5, "Libia"]
print(lista)

lista.pop()  #elimina el ultimo elemento de la lista
print(lista)

lista.pop(0)
print(lista) #eliminar el elemento en esta posicion

lista.reverse() #invierte el orden de la lista
print(lista)

lista = [1,2,4,7,8,5,9,6]
lista.sort()
print(lista)

lista = [1,2,3,5,56,['verde', 'rojo']]
print(lista)

elemento = lista[5] [1]
print(elemento)

matriz = [ [1,2,3], [5,6,7], [7,8,9] ]
lista_nueva = [elemento[0] for elemento in matriz]
print(lista_nueva)
