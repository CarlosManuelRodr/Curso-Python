#Encoding: utf-8

import matplotlib.pyplot as plt
import sys
import argparse
from numpy import *

min_re = -2.0;
max_re = 1.0;
min_im = -1.4;
max_im = 1.4;

# Mandelbrot normal.
def mandelbrot(w, h, smooth, maxit = 20):
    global min_re, max_re, min_im, max_im
    x_factor = (max_re-min_re)/(w-1);
    y_factor = (max_im-min_im)/(h-1);
    #max_im = min_im+(max_re-min_re)*h/w;
    matrix = zeros((h, w))
    log2 = log(2.0)

    for j in range(0, h):
        z_im = c_im = max_im - j*y_factor;
        for i in range(0, w):
            z_re = c_re = min_re + i*x_factor;
            c = z = complex(z_re, z_im)
            for it in range(0, maxit):
                z = z**2 + c
                if z.real**2 + z.imag**2 > 4:
                    if smooth:
                        # Mandelbrot con algoritmo de suavizado.
                        matrix[j,i] = abs(4.0*(it -  log(log(z.real**2 + z.imag**2))/log2))
                    else:
                        matrix[j,i] = it
                    break
    return matrix

# Se definen los argumentos opcionales.
parser = argparse.ArgumentParser(description='Genera fractal Mandelbrot')
parser.add_argument("-H", "--height", metavar='N', type=int, dest="height", default=500, help="Algura del fractal")
parser.add_argument("-w", "--width", metavar='N', type=int, dest="width", default=500, help="Anchura del fractal")
parser.add_argument("-i", "--iterations", metavar='N', type=int, dest="iterations", default=30, help="Número de iteraciones")
parser.add_argument("-s", "--smooth", help="Algoritmo de suavizado", dest='smooth',action='store_true')

# Se leen los opcionales.
args = parser.parse_args()

fractal = mandelbrot(w = args.width, h = args.height, maxit = args.iterations, smooth = args.smooth)
plt.imshow(fractal, extent=[min_re, max_re, min_im, max_im])
plt.title("Conjunto de mandelbrot")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()


'''
Ejercicio: Al analizar la convergencia del método de Newton-Rhapson se pueden obtener fractales. Crear un mapeo que
analice hacia cuál de las tres soluciones a la ecuación z^3 - 1 = 0 converge cada punto del plano complejo.
'''