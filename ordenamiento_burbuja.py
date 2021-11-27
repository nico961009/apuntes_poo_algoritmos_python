import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i -1): # n-i es el rango menos lo que ya recorrimos (y el -1 típico de longitud)
            #En terminos de O() tenemos: O(n) * O(n - i - 1) = O(n**2)

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] # Recordar el swaping.
    
    return lista

if __name__ == '__main__':
    tamano_lista = int(input('¿De que tamaño será la lista?'))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

