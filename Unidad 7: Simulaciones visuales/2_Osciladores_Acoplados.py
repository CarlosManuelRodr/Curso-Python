#Encoding: utf-8
# Importa módulo visual.
from visual import *
import argparse

# Se definen los argumentos opcionales.
parser = argparse.ArgumentParser(description='Simula oscilador.')
parser.add_argument("--x1", metavar='N', type=float, dest="x1", help="Posición inicial x1", default=0)
parser.add_argument("--x2", metavar='N', type=float, help="Posición inicial x2", default=5)
parser.add_argument("--vx1", metavar='N', type=float, help="Posición inicial vx1", default=0)
parser.add_argument("--vx2", metavar='N', type=float, help="Posición inicial vx2", default=0)
parser.add_argument("--k1", metavar='N', type=float, help="Valor de k para resorte 1", default=1)
parser.add_argument("--k2", metavar='N', type=float, help="Valor de k para resorte 2", default=1)
parser.add_argument("--m1", metavar='N', type=float, help="Masa 1", default=1)
parser.add_argument("--m2", metavar='N', type=float, help="Masa 2", default=1)

# Se leen los opcionales.
args = parser.parse_args()

# Variables de la simulación.
x1 = args.x1
x2 = args.x2
vx1 = args.vx1
vx2 = args.vx2
k1 = args.k1
k2 = args.k2
m1 = args.m1
m2 = args.m2

# Variables internas.
t = 0
deltat = 0.01
refX1 = -10
refX2 = 10
refPlano = 27

# Ejes de coordenadas.
arrow(pos = (-33,15,-15), axis = (5,0,0), shatfwidth = 5, color = color.red)
arrow(pos = (-33,15,-15), axis = (0,5,0), shatfwidth = 5, color = color.green)
arrow(pos = (-33,15,-15), axis = (0,0,5), shatfwidth = 5, color = color.blue)
text(pos = (-26,15,-15), text = 'X', height = 3)
text(pos = (-33,20,-15), text = 'Y', height = 3)
text(pos = (-33,15,-10), text = 'Z', height = 3)

# Objetos.
planoH = box(pos=(3,-2,0), axis=(1,0,0), length=60, width=25, height=1, material=materials.wood)
planoV = box(pos=(-refPlano,4,0), axis=(0,1,0), length=13, width=25, height=1, material=materials.wood)
particula1 = sphere(pos=(refX1+x1,0,0), radius=2, color=color.blue)
particula2 = sphere(pos=(refX2+x2,0,0), radius=2, color=color.red)
resorte1 = helix(pos=(-refPlano, 0, 0), axis=(refX1+refPlano+x1,0,0), color=(128,128,128), radius=1, coils = 25, thickness=0.4)
resorte2 = helix(pos=(refX1+x1, 0, 0), axis=(refX2+x2-x1-refX1,0,0), color=(128,128,128), radius=1, coils = 25, thickness=0.4)
texto1 = text(pos = (refX1+x1,3,0), text = 'm1', height = 3)
texto2 = text(pos = (refX2+x2,3,0), text = 'm2', height = 3)

# Efectos (iluminación).
scene.ambient=0.7

# Gráfica
grafica = display(title = "Grafica", x=scene.x + scene.width + 8, y = scene.y, width = 400, height = 400, background = (255,255,255))
grafica.autoscale = False
curva1 = curve(display = grafica, color = color.blue, radius=0.05)
curva2 = curve(display = grafica, color = color.red, radius=0.05)

# Iterar indefinidamente.
while True:
    # Control de cuadros por segundo.
    rate(100)
    
    # Calcula posición de las masas por el método de Euler.
    vx1 += deltat*(-(k1/m1)*x1+(k2/m1)*(x2-x1))
    vx2 += deltat*(-(k2/m2)*(x2-x1))
    x1 += deltat*vx1
    x2 += deltat*vx2
    
    # Actualiza posiciones.
    particula1.pos = vector(refX1+x1,0,0)
    particula2.pos = vector(refX2+x2,0,0)
    texto1.pos = vector(refX1+x1,3,0)
    texto2.pos = vector(refX2+x2,3,0)
    resorte1.axis = vector(refX1+refPlano+x1,0,0)
    resorte2.pos = vector(refX1+x1, 0, 0)
    resorte2.axis = vector(refX2+x2-x1-refX1,0,0)
    
    # Añade punto a curva.
    curva1.append(pos = (t, x1))
    curva2.append(pos = (t, x2))
    grafica.center = vector(t, 0, 0)
    
    # Incrementa reloj.
    t += deltat


'''
Ejercicio: Crear simulación de oscilador forzado y amortiguado, estos parámetros
deben ser controlados por argumentos opcionales.
'''