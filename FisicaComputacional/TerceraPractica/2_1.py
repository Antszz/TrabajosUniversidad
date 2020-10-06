import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

v = 50
angulo = np.deg2rad(60)
C = 0.5
m = 0.145
r = 0.0367
A = r*2
p = 1.2

h = 0.001
pos = [[0],[0]]
k = (1/2) * (C*A*p/m)
velocidad = [[v*np.cos(angulo)], [v*np.sin(angulo)]]
a = [-k*v*velocidad[0][0], -10-k*v*velocidad[1][0]]

pos2 = [[0],[0]]
k2 = 0
velocidad2 = [[v*np.cos(angulo)], [v*np.sin(angulo)]]
a2 = [-k2*v*velocidad2[0][0], -10-k2*v*velocidad2[1][0]]

print(np.sin(angulo))
while True:
    pos2[0].append(pos2[0][-1] + velocidad2[0][-1]*h)
    pos2[1].append(pos2[1][-1] + velocidad2[1][-1]*h)

    velocidad2[0].append(velocidad2[0][-1] + a2[0]*h)
    velocidad2[1].append(velocidad2[1][-1] + a2[1]*h)

    if(pos[1][-1] >= 0):
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