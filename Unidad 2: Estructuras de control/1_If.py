#Encoding: utf-8

# El if permite controlar el flujo del programa.
num = int(input("Escribe el número tres: "))

if num == 3:
    print("El número es tres")
    # Todo lo que le pertenece al if está indentado.
else:
    print("Pendejo! El número no es tres.")

# Se pueden checar múltiples condiciones.
variable = int(input("Escribe el número tres, el dos u otra cosa: "))

if variable == 2:
    print("El número es dos.")
elif variable == 3:
    print("El número es tres")
else:
    print("Quien sabe qué madres escribiste")

'''
Operadores lógicos: and, or, not
'''

'''
Ejercicio: Crear un programa que pida al usuario un número entero y diga si es par (pista: habrá
que comprobar si el resto que se obtiene al dividir entre dos es cero: x % 2 == 0
'''