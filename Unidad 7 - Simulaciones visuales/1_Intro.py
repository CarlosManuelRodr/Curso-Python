#Encoding: utf-8
# Importa módulo visual.
from visual import *

# Crea objeto "suelo" y "bola".
suelo = box (pos=(0,0,0), length=4, height=0.5, width=4, color=color.blue)
bola = sphere (pos=(0,4,0), radius=1, color=color.red)

# Asigna velocidasd y variables de simulación.
bola.velocity = vector(0,-1,0)
dt = 0.01
g = 9.81

# Loop principal.
while True:
	# Indica framerate. ¡En VPython 6 es imprescindible!
    rate(100)

    # Actualiza la posición de la bola.
    bola.pos = bola.pos + bola.velocity*dt
    if bola.y < bola.radius:
        bola.velocity.y = abs(bola.velocity.y)
    else:
        bola.velocity.y = bola.velocity.y - g*dt


'''
Ejercicio: Crear simulación de partícula (esfera) con movimiento senoidal.
'''