#Encoding: utf-8
import argparse

# Se definen los argumentos opcionales.
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-n", "--numero", metavar='N', type=int, dest="varnumero", help="Guarda número", required=True)
parser.add_argument("-t", "--texto", metavar='TEXT', dest="vartexto", default="Nada", help="Guarda texto")
parser.add_argument("-o", "--opcion", help="Selecciona opcional", dest='opcion',action='store_true')

# Se leen los opcionales.
args = parser.parse_args()

# Escribe valores almacenados.
print("El número es: " + str(args.varnumero))
print("El texto es: " + args.vartexto)
print("Opcion: " + str(args.opcion))