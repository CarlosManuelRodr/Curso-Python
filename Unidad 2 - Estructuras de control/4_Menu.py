#Encoding: utf-8

'''
 Se declaran las variables que utilizará el menú.
'''

nombre = ""
opcion = 0

'''
 El menú estará dentro de un While para repetirse hasta que
 se introduzca la opción de salir.
'''

while opcion != 3:
    print("Escribe una opción.")
    print("1 - Guardar nombre")
    print("2 - Escribir nombre")
    print("3 - Salir")
    opcion = int(input("Introduzca una opción: "))

    if opcion > 3 or opcion < 0:
        print("Error: Opción incorrecta")
        pass
    else:
        if opcion == 1:
            nombre = raw_input("Escribe el nombre: ")
            print("\n")
        elif opcion == 2:
            print("El nombre almacenado es: ")
            print(nombre)
            print("\n")
        else:
            break