#Encoding: utf-8

from __future__ import division
from visual import *
from visual.controls import *
from math import *
import os

# Parámetros.
cps = 200        # Cuadros por segundo.
deltat = 0.005   # Intervalo temporal.
G = 1            # Constante de gravitación.

# Crea escena.
scene.width = 800
scene.height = 600
scene.autoscale = False

# Clases de cuerpos celestes.
class CuerpoCel(sphere):
    vel = [0,0,0]
    coord = [0,0,0]
    m = 1
    def __init__(self, coord=None, vel=None):
        if coord is None:
            coord = [0,0,0]
        else:
            self.coord = coord

        if vel is None:
            vel = [0,0,0]
        else:
            self.vel = vel

        sphere.__init__(self, pos=tuple(coord), coils=50, make_trail=True)
        self.vel = vel
        self.nombre = 'Cuerpo desconocido'
        self.trail_object.radius=0.05

    def Update(self):
        self.pos = tuple(self.coord)

class Tierra(CuerpoCel):
    def __init__(self, pos=None, vel=None):
        CuerpoCel.__init__(self, pos, vel)
        self.m = 10.0
        self.material = materials.BlueMarble
        self.radius = 1
        self.nombre = 'Tierra'
        self.trail_object.color = color.cyan

class Sol(CuerpoCel):
    def __init__(self, pos=None, vel=None):
        CuerpoCel.__init__(self, pos, vel)
        self.m = 150.0
        self.material = materials.emissive
        self.radius = 2
        self.color = color.yellow
        self.nombre = 'Sol'
        self.trail_object.color = color.yellow

class Satelite(CuerpoCel):
    def __init__(self, pos=None, vel=None):
        CuerpoCel.__init__(self, pos, vel)
        self.m = 40.0
        self.material = materials.rough
        self.radius = 1
        self.color = color.blue
        self.nombre = 'Satelite'
        self.trail_object.color = color.blue


# Crea objeto que contiene todos los cuerpos celestes de esta simulación.
tierra = Tierra(pos=[10.0, 7.0, 9.0], vel=[-1.0, -3.0, 4.0])
sol = Sol(pos=[0.0, 0.0, 0.0], vel=[-1.0, 0.0, 0.0])
satelite = Satelite(pos=[5.0, 5.0, 8.0], vel=[-4.0, 2.0, 2.0])
lista_cuerpos = [tierra, sol, satelite]

# Efectos.
Esfera = sphere(pos=(0, 0, 0), radius=50, color=color.black, opacity=0.3, material=materials.rough)
luz = local_light(pos=(0, 0, 0), color=color.yellow)

# Ejes de coordenadas.
eje1 = arrow(pos=(-6, 0, 0), axis=(1,0,0), color=color.red)
eje2 = arrow(pos=(-6, 0, 0), axis=(0,1,0), color=color.green)
eje3 = arrow(pos=(-6, 0, 0), axis=(0,0,1), color=color.blue)

# Controles.
centrar = lista_cuerpos[0]  # Por defecto centra el primer cuerpo.
def Vista(cuerpo):
    global centrar
    centrar = cuerpo
    
control = controls(title='Parametros', x=scene.width + 10, y=scene.y, width=300, height=300, range=50)
m1 = menu(pos=(-20,0), height=7, width=25, text='Vista')
for item in lista_cuerpos:
    m1.items.append((item.nombre, lambda item=item: Vista(item)))

while True:
    # Recorre toda la lista de cuerpos celestes.
    for i in lista_cuerpos:
        # Se obtiene una sublista sin el cuerpo actual.
        tmp = list(lista_cuerpos)
        tmp.remove(i)
        for j in tmp:
            # Calcula distancia.
            dcuad = 0
            for idx in range(0,3):
                dcuad += (i.coord[idx] - j.coord[idx])**2

            # Calcula cambio de velocidad por interacción con el otro cuerpo.
            for idx in range(0,3):
                i.vel[idx] -= deltat*((G*(i.coord[idx] - j.coord[idx])*j.m)/(dcuad**1.5))
        
        # Calcula el cambio de posición.
        for idx in range(0,3):
            i.coord[idx] += deltat*i.vel[idx]

        # Actualiza las posiciones de los objetos en la simulación.
        i.Update()

    scene.center = centrar.pos
    rate(cps)
