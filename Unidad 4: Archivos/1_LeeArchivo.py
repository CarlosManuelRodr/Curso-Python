#Encoding: utf-8

import sys

if len(sys.argv) > 1:
    argumento = sys.argv[1]
    f = open(argumento, 'r')
    for linea in f:
        print(linea)
    f.close()

else:
    print("Número incorrecto de argumentos.")