#Encoding: utf-8

def funcion_sin_arg():
    print("Soy una función pendeja. No tengo argumentos ni hago nada.")
    jkj = 56*9834
    return 9

def funcion_con_arg(arg1, arg2):
    print("La suma de los argumentos es: " + str(arg1+arg2))

a = funcion_sin_arg()
funcion_con_arg(4,19)
print(a)

for i in range(0,10):
    funcion_con_arg(i, i+1)

'''
Ejercicio: Hacer un programa que calcule la solucion de una ec. cuadratica. Habra una funcion 
llamada "raiz_positiva" y otra "raiz_negativa". 
'''