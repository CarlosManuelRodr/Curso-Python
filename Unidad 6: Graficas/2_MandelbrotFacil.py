#Encoding: utf-8

import matplotlib.pyplot as plt
import sys
from numpy import *

min_re = -2.0;
max_re = 1.0;
min_im = -1.2;
max_im = 1;

def mandelbrot(w, h, maxit = 20):
    global min_re, max_re, min_im, max_im
    x_factor = (max_re-min_re)/(w-1);
    y_factor = (max_im-min_im)/(h-1);
    max_im = min_im+(max_re-min_re)*h/w;
    matrix = zeros((h, w))

    for j in range(0, h):
        z_im = c_im = max_im - j*y_factor;
        for i in range(0, w):
            z_re = c_re = min_re + i*x_factor;
            c = z = complex(z_re, z_im)
            for it in range(0, maxit):
                z = z**2 + c
                if z.real**2 + z.imag**2 > 4:
                    matrix[j,i] = it
                    break
    return matrix


def mandelbrot_smooth(w, h, maxit = 20):
    global min_re, max_re, min_im, max_im
    x_factor = (max_re-min_re)/(w-1);
    y_factor = (max_im-min_im)/(h-1);
    max_im = min_im+(max_re-min_re)*h/w;
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
                    matrix[j,i] = abs(4.0*(it -  log(log(z.real**2 + z.imag**2))/log2))
                    break
    return matrix

plt.imshow(mandelbrot_smooth(500,400,30), extent=[min_re, max_re, min_im, max_im])
plt.title("Conjunto de mandelbrot")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()