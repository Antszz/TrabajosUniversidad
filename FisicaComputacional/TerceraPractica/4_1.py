import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h = 0.00001
r=8
m=5
pos = [[r],[0],[0]]
velocidad = [[0],[4],[0]]
a = [-2,0]
tiempo = 12.6
pt = np.arange(0, tiempo, h)

for i in pt:
    x = pos[0][-1]
    y = pos[1][-1]

    pos[0].append(x + velocidad[0][-1]*h)
    pos[1].append(y + velocidad[1][-1]*h)

    a = [-2 * x/r, -2 * y/r]

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)

rsimulado = np.sqrt(pow(pos[0][-1],2)+pow(pos[1][-1],2))

error = np.abs(rsimulado - r)/r*100

print(f'El error con un h de {h} despues de una vuelta es {error}')
plt.plot(pos[0],pos[1])    
plt.xlabel('espacio-x')
plt.ylabel('espacio-y')
plt.title('y-x')
plt.grid(True)

plt.show()
