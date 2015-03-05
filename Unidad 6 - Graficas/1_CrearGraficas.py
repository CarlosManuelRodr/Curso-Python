#Encoding: utf-8

# Importa módulo de matplotlib y numpy.
import matplotlib.pyplot as plt
import numpy as np

# Crea array de x, & calcula array de sin() para y.
x = np.arange(0, 10, 0.2)
y = np.sin(x)

# Grafica y modifica parámetros de la gráfica.
plt.plot(x, y)
plt.title("Grafica pendeja")
plt.xlabel("El eje X.")
plt.ylabel("El eje Y.")

# Muestra gráfica en la pantalla.
plt.show()

'''
    El método de Newton-Rhapson es un bastante eficiente para resolver ecuaciones
    numéricamente. Para usarlo se requiere conocer la función f(x) y su derivada
    fPrime(x). Funciona tanto para números reales como para complejos. Su desventaja
    es que sólo permite calcular una solución por condición inicial. 

    Esta definido por la relación recurrente:

      x_(n+1) = x_n - f(x_n)/fPrime(x_n)

Ejercicio: Implementar el método de Newton-Rhapson para x^2 - 5x + 6 = 0, y graficar la convergencia de los valores.
Ejercicio: Implementar el método de Newton-Rhapson para z^2 - 1 = 0, donde z es un número complejo.
'''