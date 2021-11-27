import random

def busqueda_binaria(lista, comienzo, final, objetivo):
# En este caso estamos utilizando recursividad con la palabra "return".

    # Utilizaremos un print para ver que esta pasando en este algoritmo internamente:
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final -1]}')
    # Importante recordar que cuando se viene de un len() y despues se quiere acceder por medio de indices
    # hay que restar un uno.

    if comienzo > final: #Esto queire decir que ya no lo encontramos (o la lista no esta ordenada).
        return False
    
    medio = (comienzo + final) // 2 # El // indica división de enteros.

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)
    

if __name__ == '__main__':
    tamano_lista = int(input('¿De que tamaño será la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo) # Le estamos indicando como parámetros que comenzaremos
                                                                  # en cero, terminaremos según la longitud de la lista y nos
                                                                  # moveremos de acurdo a un objetivo.
    
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')