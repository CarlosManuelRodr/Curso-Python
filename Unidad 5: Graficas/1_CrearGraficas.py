#Encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.plot(x, y)
plt.title("Grafica pendeja")
plt.xlabel("El eje X es muy gay.")
plt.ylabel("El eje Y es muy hetero.")

plt.show()