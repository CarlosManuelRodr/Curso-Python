#Encoding: utf-8
import sys   # Importa módulo.

# Se puede crear una lista con varios elementos.
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Los elementos pueden ser de distinto tipo.
varios = ['a', 'b', 23, 'd', 'e', 98.3938, 'g']

# Las listas no tienen tamaño fijo. Se pueden añadir elementos.
letras = letras + ['h', 'i']
print(letras[8])

# Se pueden remplazar los elementos.
letras[7] = 'y'
letras[2:5] = ['C', 'D', 'E']

# Se puede medir el tamaño
print("El tamaño de la lista 'letras' es: " + str(len(letras)))

# Escribe las letras.
for letra in letras:
    sys.stdout.write(letra)

print('')

'''
Ejercicio: Hacer un programa que pida tu nombre y que escriba la primera y tercera letra.
'''