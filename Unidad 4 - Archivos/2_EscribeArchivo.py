#Encoding: utf-8

import sys

if len(sys.argv) > 1:
    argumento = sys.argv[1]
    f = open("archivo.txt", 'w')
    f.write(argumento)
    f.close()

else:
    print("Número incorrecto de argumentos.")


'''
Agregar función para guardar datos en texto al programa de la agenda.
'''