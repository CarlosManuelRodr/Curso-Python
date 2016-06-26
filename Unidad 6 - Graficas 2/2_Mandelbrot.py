#Encoding: utf-8

from numpy import *
import matplotlib.pyplot as plt
import sys
import csv
import os

def progress(now, total):
    # Crea barra de progreso en la terminal.
    progress = now/total
    barLength = 20
    status = ""
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rProgreso: [{0}] {1}%".format( "#"*block + "-"*(barLength-block), round(progress*100,2), status)
    sys.stdout.write(text)
    sys.stdout.flush()

def save_matrix(matrix, filename):
    # Crea archivo csv.
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        # Recorre todas las filas de la matriz y las copia al csv.
        for row in matrix:
            writer.writerow(row)

    # Cierra archivo.
    csvfile.close()

def load_matrix(filename, datatype=int):
    matrix = None
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        # Se calcula número de filas y columnas.
        h = len(list(reader))
        csvfile.seek(0)
        w = len(next(reader))
        csvfile.seek(0)

        # Se crea matriz.
        matrix = zeros((h,w),dtype=datatype)

        # Copia elementos del csv a la matriz.
        i = 0
        for row in reader:
            matrix[i] = list(map(datatype, row))
            i += 1

    csvfile.close()
    return matrix

def save_iter(iter):
    try:
        f = open('iterations.txt', 'w')
        f.write(str(iter))
        f.close()
        return True
    except IOError:
        print("Error al abrir archivo!")
        return False

def load_iter():
    try:
        f = open('iterations.txt', 'r')
        iter = int(f.read())
        f.close()
        return iter
    except IOError:
        return None

def rm_temp():
    # Elimina los archivos que ya no son necesarios.
    os.remove('iterations.txt')
    os.remove('z.csv')
    os.remove('divtime.csv')


def mandelbrot(h,w, maxit=20):
    # Crea variables.
    y,x = ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    divtime = maxit + zeros(c.shape, dtype=int)
    minit = 0

    # Trata de cargar archivo de sesión anterior.
    l_iter = load_iter()

    # Si no existe archivo es que no hay proceso pendiente.
    if l_iter is None:
        z = c
    else:
        divtime = load_matrix('divtime.csv')
        z = load_matrix('z.csv', complex)
        minit = l_iter

    # Loop principal del fractal.
    for i in range(minit, maxit):
        try:
            progress(i, maxit)
            z  = z**2 + c
            diverge = z*conj(z) > 2**2            # Matriz con elementos que divergen.
            div_now = diverge & (divtime==maxit)  # Elementos que divergieron en esta iteraciíon.
            divtime[div_now] = i                  # Especifica en que iteración divergieron.
            z[diverge] = 2                        # Los que ya divergieron se dejan en un lugar fijo.
        except KeyboardInterrupt:
            # Guarda todas las matrices y variables que se estaban usando.
            print("Programa interrumpido por el usuario.")
            save_matrix(divtime, 'divtime.csv')
            save_matrix(z, 'z.csv')
            save_iter(i)
            sys.exit(0)
        except:
            print("Excepción desconocida.")

    # Si se había cargado archivo, hay que eliminarlos, ya no son necesarios.
    if l_iter is not None:
        rm_temp()
    return divtime

plt.imshow(mandelbrot(500,500,100))
plt.show()


'''
Ejercicio: Implementar la solución a f(x) = sen(x) - x = 0 con el método de Newton-Rhapson, haciendo que el
programa se pueda cerrar y que al cargar de nuevo continúe en el lugar donde se quedó.
'''