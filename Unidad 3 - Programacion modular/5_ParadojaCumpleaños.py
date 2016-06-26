#Encoding: utf-8
import random

def verifica_coincidencia(personas):
	fechas = []
	for i in range(personas):
		fechas.append(random.randint(1, 365))

	coincidencias = 0
	i = 0
	j = 0
	while i < personas:
		while j < personas:
			if i != j:
				if fechas[i] == fechas[j]:
					coincidencias += 1
			j += 1
		i += 1

	if coincidencias > 0:
		return True
	else:
		return False

def realiza_experimento(personas, pruebas):

	coincidencias = 0.0
	for i in range(pruebas):
		if verifica_coincidencia(personas) == True:
			coincidencias += 1

	return coincidencias / float(pruebas)


print(realiza_experimento(100, 100))