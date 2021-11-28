import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        posicion_actual = indice 
        # Este representa el índice de la lista, y comienza en 1 porque así lo indicamos en range.
        valor_actual = lista[indice] 
        # Devuelve el valor que le corresponde a cada índice de la lista.
        
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
        # Mientras que el índice sea mayor a cero y el valor que corresponde al índice - 1 sea mayor al valor que 
        # corresponde al índice actual, entonces ejecuta lo siguiente:
            lista[posicion_actual] = lista[posicion_actual - 1]
            # la posición actual se iguala al de la posición actual con un índice menor.
            posicion_actual -= 1
            # se la resta uno a la posición actual.

        lista[posicion_actual] = valor_actual
        # Se iguala el la lista con la posición actual con el valor actual.

    return lista
    #Se retorna la lista ordenada.

if __name__ == '__main__':
    tamano_lista = int(input('¿De que tamaño será la lista?'))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)