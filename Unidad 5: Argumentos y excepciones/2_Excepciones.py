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


    except ZeroDivisionError as err:
        print("Estúpido!:", err)

    except ValueError:
        print("Error: No se ha introducido un número")

    except Exception as e:
        print("Excepción: " + str(e))

    except KeyboardInterrupt:
        print("Interrupción")
        sys.exit(1)

    except:
        print("Excepción desconocida")
        sys.exit(1)