#Encoding: utf-8

from numpy import *
import matplotlib.pyplot as plt
import sys

def progress(now, total):
    progress = now/total
    barLength = 20
    status = ""
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rProgreso: [{0}] {1}%".format( "#"*block + "-"*(barLength-block), round(progress*100,2), status)
    sys.stdout.write(text)
    sys.stdout.flush()

def mandelbrot( h,w, maxit=20 ):
    y,x = ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + zeros(z.shape, dtype=int)

    for i in range(maxit):
        try:
            progress(i, maxit)
            z  = z**2 + c
            diverge = z*conj(z) > 2**2            # who is diverging
            div_now = diverge & (divtime==maxit)  # who is diverging now
            divtime[div_now] = i                  # note when
            z[diverge] = 2                        # avoid diverging too much
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario.")
            sys.exit(0)
        except:
            print("Excepción desconocida.")

    return divtime

plt.imshow(mandelbrot(500,500,30))
plt.show()