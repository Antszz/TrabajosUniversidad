import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h = 0.01
pos = [[0],[0],[0]]
velocidad = [[2],[3],[0]]
a = [0,-10,0]

while True:
    pos[0].append(pos[0][-1] + velocidad[0][-1]*h)
    pos[1].append(pos[1][-1] + velocidad[1][-1]*h)
    pos[2].append(pos[2][-1] + velocidad[2][-1]*h)

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)
    velocidad[2].append(velocidad[2][-1] + a[2]*h)

    if(pos[1][-1] < 0):
        break

plt.plot(pos[0],pos[1])    
plt.xlabel('espacio-x')
plt.ylabel('espacio-y')
plt.title('y-x')
plt.grid(True)

plt.show()
