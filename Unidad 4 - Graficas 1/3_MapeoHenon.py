#Encoding: utf-8

import matplotlib.pyplot as plt
import numpy
import math

a = 1.4
b = 0.3
x0 = 0
y0 = 0

def henon_x(x, y, a):
    return 1.0 - a*x**2.0 + y

def henon_y(x, b):
    return b*x

def plot_henon():
    global a, b, x0, y0
    xys = []
    x = x0
    y = y0

    for i in range(20):
        tmp_x = x
        x = henon_x(x, y, a)
        y = henon_y(tmp_x, b)

    for i in range(1000):
        tmp_x = x
        x = henon_x(x, y, a)
        y = henon_y(tmp_x, b)
        xys.append([x, y])

    xys = numpy.array(xys)
    fig = plt.figure()
    plt.plot(xys[:,0], xys[:,1], '.')
    fig.suptitle("Mapa de Henon.", fontsize=14)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

if __name__ == "__main__":
    plot_henon()