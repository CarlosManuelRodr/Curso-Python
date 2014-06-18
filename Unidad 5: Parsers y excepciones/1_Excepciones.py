#Encoding: utf-8

import sys

while True:
    try:
        # Código que puede caer en error.
        num = int(input("Introduce un denominador para que divida a 2: "))
        if num == 3:
            raise Exception("Terrible error! Has introducido el 3")

        res = 2/num
        print("2/" + str(num) + " = " + str(res))


    # Excepción de división entre cero.
    except ZeroDivisionError as err:
        print("Estúpido!:", err)

    # Excepción de variable de tipo incorrecto.
    except ValueError:
        print("Error: No se ha introducido un número")

    # Excepción estándar (la que ocurre cuando se introduce el tres).
    except Exception as e:
        print("Excepción: " + str(e))

    # Excepción de interrupción por teclado.
    except KeyboardInterrupt:
        print("Interrupción")
        sys.exit(1)

    # Excepción estándar.
    except:
        print("Excepción desconocida")
        sys.exit(1)

'''
Ejercicio: Cuando se intenta abrir un archivo, si el sistema no lo encuentra lanza una
excepción "IOError". Implementar un lector de archivo de texto que sea capaz de manejar
el caso en el que no encuentra el archivo que se desea abrir.
'''