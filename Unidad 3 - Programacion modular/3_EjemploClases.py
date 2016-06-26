#Encoding: utf-8

class Puerta:
    def __init__(self):
        self.m_abierta = True
        self.m_contrasegna = 0

    def Abrir(self, contrasegna):
        if(contrasegna == self.m_contrasegna):
            self.m_abierta = True
            return True
        else:
            return False

    def Cerrar(self, contrasegna):
        self.m_abierta = False
        self.m_contrasegna = contrasegna


puerta_rara = Puerta()
puerta_rara.Cerrar(2398)

lista_puertas = []
lista_puertas.append(Puerta())
lista_puertas.append(Puerta())
lista_puertas.append(puerta_rara)

for puerta in lista_puertas:
    print(puerta.m_abierta)


'''
 Ejercicio 1: Crear varias clases que se llamarán Círculo, Cuadrado y Triángulo. Cada
 clase se debe construir con los parámetros de cada figura geométrica. La clase debe
 tener un método para calcular el área de cada una.


 Ejercicio 2: Crear una clase que se llame polígono. La clase debe poder aceptar un número
 arbitrario de puntos y luego poder calcular su área.
'''