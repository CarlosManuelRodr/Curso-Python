#Encoding: utf-8

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if len(sys.argv) > 1:
    argumento = int(sys.argv[1])
    print(factorial(argumento))
else:
    print("Número incorrecto de argumentos.")


'''
Ejercicio: Escribe una función recursiva que realice una cuenta regresiva, empezando desde 
un valor especificado por el usuario, y termine en cero.

Ejercicio 2: Escribe un programa que eleve un número a una potencia n, considerando que una
potencia se puede escribir como una función recursiva.
'''