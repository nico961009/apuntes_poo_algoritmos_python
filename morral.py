
def morral(tamano_morral, pesos, valores, n):
    
    # Colocamos un caso base para evitar un loop infinito, en este caso tenemos: si ya no tenemos elementos que recorrer
    # o si nuestro morral ya se lleno:
    if n == 0 or tamano_morral == 0:
        return 0
    
    # Igualmente agregamos otro caso base, en este caso si el objeto es de mayor tamaño que nuestro morral
    # nos vamos al siguiente elemento y esto lo logramos con una función recursiva:
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)

    # Ahora nos preguntamos: si yo tomará este elemento, ¿Qué valor tendría? y si no lo tomo ¿Qué valor tendría?
    # y quiero escoger el máximo entre  estos dos.
    return max(valores[n-1] + morral(tamano_morral-pesos[n-1], pesos, valores, n-1), morral(tamano_morral, pesos, valores, n-1))
                # Aquí tengo dos opciones, la primera es escoger el elemento por lo que el morral se hace más chico 
                # y el segundo caso (separado por una coma) nuestro morral no se hace más chico.

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)