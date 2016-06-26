#Encoding: utf-8
import csv

# Lee archivo CSV.
try:
	f = open('ejemplo.csv', 'r')
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		print("Leyendo fila")
		for col in row:
			print(col)
	f.close()

except IOError:
	print("No se ha encontrado archivo CSV.")


# Escribe archivo CSV.
lista1 = [34, 525, 6250, 12, 99, 23]
lista2 = [2, 192093, 128, 1, 1]
f = open('escribir.csv', 'w')
writer = csv.writer(f, delimiter=',')
writer.writerow(lista1)
writer.writerow(lista2)
f.close()