import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h = 0.01
t = 0
pos = [[10],[10],[10]]
velocidad = [[0],[0],[4]]
a = [0,-10,0]
aux = []

while True:
    pos[0].append(pos[0][-1] + velocidad[0][-1]*h)
    pos[1].append(pos[1][-1] + velocidad[1][-1]*h)
    pos[2].append(pos[2][-1] + velocidad[2][-1]*h)

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)
    velocidad[2].append(velocidad[2][-1] + a[2]*h)

    if(pos[1][-1] < 0):
        break

g1 = plt.axes(projection='3d')
g1.scatter3D(pos[0],pos[1],pos[2])
g1.set_xlabel('espacio-x')
g1.set_ylabel('espacio-y')
g1.set_zlabel('espacio-z')
plt.title('Trayectoria')

plt.show()