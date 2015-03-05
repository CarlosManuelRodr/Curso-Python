#Encoding: utf-8

# El while verifica una condición en cada iteración.
i = 0
while i <= 10:
    print(i)
    i += 1

# Secuencia de fibbonaci.
a, b = 0, 1    # Asignación múltiple. a = 0, b = 1
print("Fibbonaci")
while b < 50:
	print(b)
	a, b = b, a+b


'''
Ejercicio 1: Crear un programa que pida números positivos al usuario, y vaya calculando la suma
de todos ellos (terminará cuando se teclea un número negativo o cero).

Ejercicio 2: Hacer un programa que escriba el termino n de la serie de fibonnaci.
'''