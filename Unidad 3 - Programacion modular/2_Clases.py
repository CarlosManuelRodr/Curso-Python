#Encoding: utf-8

'''
 Define la clase Puerta. Esta puerta tiene dos estados, abierta y cerrada, 
 y se cierra con una contraseña. Para abrila se necesita introducir la
 contraseña de nuevo.
'''

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


'''
 Esta función se encarga de averiguar el estado de las puertas. Como argumento
 se requieren dos objetos de la clase Puerta.
'''

def estado_puerta(puerta1, puerta2):
    if puerta1.m_abierta:
        print("La puerta 1 está abierta.")
    else:
        print("La puerta 1 está cerrada.")

    if puerta2.m_abierta:
        print("La puerta 2 está abierta.")
    else:
        print("La puerta 2 está cerrada.")


'''
 Crea dos objetos de la clase Puerta.
'''

mi_puerta1 = Puerta()
mi_puerta2 = Puerta()


'''
Menú para manipular la clase puerta.
'''

opcion = 0
while opcion != 3:
    estado_puerta(mi_puerta1, mi_puerta2)

    print("¿Qué puerta desea usar?")
    print("1 - Puerta 1")
    print("2 - Puerta 2")
    print("3 - Salir")
    opcion = int(input("Introduzca una opción: "))

    if opcion > 3 or opcion < 0:
        print("Error: Opción incorrecta")
        pass
    else:
        if opcion == 1:
            usar_puerta = mi_puerta1
        elif opcion == 2:
            usar_puerta = mi_puerta2
        else:
            break

        print("¿Qué desea hacer con la puerta?")
        print("1 - Abrirla")
        print("2 - Cerrarla")
        opcion_puerta = int(input("Introduzca una opción: "))

        if opcion_puerta == 1:
            if usar_puerta.m_abierta:
                print("Error: La puerta ya está abierta.")
            else:
                cont = int(input("Introduzca la contraseña: "))
                if usar_puerta.Abrir(cont):
                    print("La puerta se abrió.")
                else:
                    print("La puerta no se abrió.")
        elif opcion_puerta == 2:
            cont = int(input("Introduzca la contraseña: "))
            usar_puerta.Cerrar(cont)
            print("Puerta cerrada.")
        else:
            print("Opción incorrecta")
            pass