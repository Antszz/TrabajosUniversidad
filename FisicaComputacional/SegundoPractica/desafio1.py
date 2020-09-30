import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h=0.01

pos1 = [[0],[0],[0]]
velocidad1 = [[5],[2],[0]]
a1 = [2,-10,0]

while True:
    pos1[0].append(pos1[0][-1] + velocidad1[0][-1]*h)
    pos1[1].append(pos1[1][-1] + velocidad1[1][-1]*h)
    pos1[2].append(pos1[2][-1] + velocidad1[2][-1]*h)

    velocidad1[0].append(velocidad1[0][-1] + a1[0]*h)
    velocidad1[1].append(velocidad1[1][-1] + a1[1]*h)
    velocidad1[2].append(velocidad1[2][-1] + a1[2]*h)

    if(pos1[1][-1] < 0):
        break

g1 = plt.axes(projection='3d')
g1.scatter3D(pos1[0],pos1[1],pos1[2])
g1.set_xlabel('espacio-x')
g1.set_ylabel('espacio-y')
g1.set_zlabel('espacio-z')
plt.title('Trayectoria 1')

plt.show()
