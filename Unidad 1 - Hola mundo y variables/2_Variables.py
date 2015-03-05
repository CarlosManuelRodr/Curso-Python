#Encoding: utf-8

# Se pueden declarar variables sin especificar tipo.
numero_flotante = 20.23283
numero_entero = 5
frase = "La vida es miseria "

# Se pueden realizar operaciones entre variables.
suma = numero_entero + numero_flotante
frase_suma = frase + "en Xalapa"

# Se pueden converter los tipos de variable.
frase_num = frase + str(suma) + " veces"

# Las cadenas de texto se imprimen con print.
print(frase_suma)
print(frase_num)

# Los números también se pueden imprimir con print.
print(numero_entero)
print(numero_flotante)

# Las cadenas de texto están compuestas por un arreglo de varias letras.
# Se puede acceder a sus elementos.
print(frase[0])
print(frase[1])

# O extraer subcadenas de texto.
print(frase[0:4])
print(frase[4:10])

# Se puede omitir el primer índice.
print(frase[:4])

# O el segundo.
print(frase[2:])

'''
Los índices se contean así:
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

'''
Ejercicio 1: El usuario tecleará dos números (a y b), y el programa mostrar el resultado de la
operación (a+b)*(a-b) y el resultado de la operación a^2-b^2. Potenciación en python es: 3**2 = 9.

Ejercicio 2: Con el texto se pueden hacer tambien operaciones de suma. La suma en texto
une las cadenas de texto. Hacer un programa que le pregunte el nombre al usuario
y lo salude por su nombre
'''