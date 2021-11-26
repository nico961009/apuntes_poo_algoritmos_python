
import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break # Este break no sirve de nada si pensamos en el peor de los casos
                  # (encontrarlo al final o no encontrarlo)
                  # solo será de útilidad si lo encontramos pronto ya que nos ahorra tiempo.
    return match

if __name__ == '__main__':
    tamano_lista = int(input('¿De que tamaño será la lista?'))
    objetivo = int(input('¿Qué número quieres encontrar?'))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    # Esta última línea es una función ternaria ya que se escribe en una sola línea de código.