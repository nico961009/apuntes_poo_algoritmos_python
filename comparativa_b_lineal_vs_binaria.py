import random

def busqueda_binaria(lista, comienzo, final, objetivo):

    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final -1]}')

    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

def busqueda_lineal(lista, objetivo):
    match = False
    counter= 0

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        counter = counter + 1
    return match, counter
    

if __name__ == '__main__':
    tamano_lista = int(input('¿De que tamaño será la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontradob = busqueda_binaria(lista, 0, len(lista), objetivo) 
    encontradol = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontradob else "no esta"} en la lista (binario)')

    print(f'El elemento {objetivo} {"esta" if encontradol else "no esta"} en la lista (lineal)')