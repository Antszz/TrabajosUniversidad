import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h = 0.01
r=8
m=5
pos = [[r],[0],[0]]
velocidad = [[0],[4],[0]]
a = [-2,0]
tiempo = 40
pt = np.arange(0, tiempo, h)

for i in pt:
    x = pos[0][-1]
    y = pos[1][-1]

    pos[0].append(x + velocidad[0][-1]*h)
    pos[1].append(y + velocidad[1][-1]*h)

    a = [-2 * x/r, -2 * y/r]

    v = np.sqrt(pow(velocidad[0][-1], 2) + pow(velocidad[1][-1],2))
    print(v*v/r)

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)

plt.plot(pos[0],pos[1])    
plt.xlabel('espacio-x')
plt.ylabel('espacio-y')
plt.title('y-x')
plt.grid(True)

plt.show()
