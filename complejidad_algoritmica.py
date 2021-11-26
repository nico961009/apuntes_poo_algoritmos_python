import time
import sys

# Vamos a probar la complejidad algoritmica basados en
# el tiempo.

# Función para calculo de factorial.
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

# Función de factorial recursivo (mismo resultado que la anterior).
def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__=='__main__':
    sys.setrecursionlimit(200000)
    n = 20000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print( final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print( final - comienzo)

    print(sys.getrecursionlimit())

