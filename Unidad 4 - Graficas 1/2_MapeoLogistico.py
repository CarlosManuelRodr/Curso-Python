#Encoding: utf-8

import matplotlib.pyplot as plt
import numpy
import math

'''
La función que define el mapeo logístico es la siguiente.
'''

def fl(x, r):
    return r*x*(1-x)


'''
Para graficar se utiliza la siguiente función.
'''

def plot_logistic():
    ys = []
    rs = numpy.linspace(0, 4, 400)
    for r in rs:
        x = 0.1

        # Estabiliza punto.
        for i in range(100):
            x = fl(x, r)

        for i in range(200):
            x = fl(x, r)
            ys.append([r, x])

    ys = numpy.array(ys)
    fig = plt.figure()
    fig.suptitle("Mapa de Logistico.", fontsize=14)
    plt.scatter(ys[:,0], ys[:,1], s = 0.1)
    plt.xlabel("r")
    plt.ylabel("x")
    plt.show()


if __name__ == "__main__":
    plot_logistic()