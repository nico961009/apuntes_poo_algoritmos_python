# Se realiza la importación de librerías para generar la ventana y poder visualizar
# en el navegador, así como también para prender un servidor que nos permitirá ver la 
# gráfica.
from bokeh.plotting import figure, output_file, show
# Se importó la función para la figura, para decidir cual es el archivo de salida y la función
# para poder generar la figura.  

if __name__=='__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('¿Cuántos valores quieres graficar? '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'valor "y" para {x} ')) #generamos una y por cada valor de la x.
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2) #forma de generar la figura
    show(fig) # Forma de mostrar la figura generada.