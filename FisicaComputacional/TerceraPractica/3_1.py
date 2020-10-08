import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

r=0.005
vl = 4/3*np.pi*r**3
C = 0.5
d = 1000
m = d*vl
r = 0.0367
A = np.pi*r**2
p = 1.2

h = 0.001
pos = [[0],[16]]
k = (1/2) * (C*A*p/m)
velocidad = [[14], [0]]
a = [0, -10]

while True:
    pos[0].append(pos[0][-1] + velocidad[0][-1]*h)
    pos[1].append(pos[1][-1] + velocidad[1][-1]*h)

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)

    v = math.sqrt(pow(velocidad[0][-1],2) + pow(velocidad[1][-1],2))
    a[0] = -k * v * velocidad[0][-1]
    a[1] = -10 -k * v * velocidad[1][-1]

    if(pos[1][-1] < 0):
        break

plt.plot(pos[0],pos[1])
plt.xlabel('espacio-x')
plt.ylabel('espacio-y')
plt.title('y-x')
plt.grid(True)

plt.show()