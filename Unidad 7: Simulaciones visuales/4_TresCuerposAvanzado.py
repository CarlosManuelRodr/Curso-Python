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

# Clase de cuerpos celestes.
class CuerpoCel(sphere):
    vel = [0,0,0]
    coord = [0,0,0]
    m = 1
    def __init__(self, coord=[0, 0, 0], vel=[0, 0, 0], nombre='Desconocido', masa=1, radio=1, 
                 color=(1, 1, 1), material=materials.marble, color_trail=color.red):
        sphere.__init__(self, pos=tuple(coord), coils=50, make_trail=True)
        self.coord = coord
        self.vel = vel
        self.vel = vel
        self.nombre = nombre
        self.m = masa
        self.radius = radio
        self.color = color
        self.material = material
        self.trail_object.color = color_trail
        self.trail_object.radius=0.05

    def Update(self):
        self.pos = tuple(self.coord)

# Crea lista que contiene todos los cuerpos celestes de esta simulación.
tierra = CuerpoCel(coord=[10.0, 7.0, 9.0], vel=[-1.0, -3.0, 4.0], nombre='Tierra', masa=10, 
                   radio=1, color_trail=color.cyan, material=materials.BlueMarble)

sol = CuerpoCel(coord=[0.0, 0.0, 0.0], vel=[-1.0, 0.0, 0.0], nombre='Sol', masa=150, 
                radio=2, color=color.yellow, color_trail=color.yellow, material=materials.emissive)

satelite = CuerpoCel(coord=[5.0, 5.0, 8.0], vel=[-4.0, 2.0, 2.0], nombre='Satelite', masa=40, 
                     radio=1, color=color.blue, color_trail=color.blue, material=materials.rough)
lista_cuerpos = [tierra, sol, satelite]

# Efectos.
esfera = sphere(pos=(0, 0, 0), radius=50, color=color.black, opacity=0.3, material=materials.rough)
luz = local_light(pos=(0, 0, 0), color=color.yellow)

# Ejes de coordenadas.
eje1 = arrow(pos=(-6, 0, 0), axis=(1, 0, 0), color=color.red)
eje2 = arrow(pos=(-6, 0, 0), axis=(0, 1, 0), color=color.green)
eje3 = arrow(pos=(-6, 0, 0), axis=(0, 0, 1), color=color.blue)

# Controles.
centrar = lista_cuerpos[0]  # Por defecto centra el primer cuerpo.
def Vista(cuerpo):
    global centrar
    centrar = cuerpo
    
control = controls(title='Parametros', x=scene.width + 10, y=scene.y, width=300, height=300, range=50)
m1 = menu(pos=(-20, 0), height=7, width=25, text='Vista')
for item in lista_cuerpos:
    m1.items.append((item.nombre, lambda item=item: Vista(item)))

# Loop principal.
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

    # Actualiza posición de esfera decorativa y centro de escena.
    esfera.pos = scene.center = centrar.pos
    rate(cps)
