import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h=0.01

pos2 = [[0],[0],[0]]
velocidad2 = [[5],[2],[0]]
a2 = [-1,-10,0]

while True:
    pos2[0].append(pos2[0][-1] + velocidad2[0][-1]*h)
    pos2[1].append(pos2[1][-1] + velocidad2[1][-1]*h)
    pos2[2].append(pos2[2][-1] + velocidad2[2][-1]*h)

    velocidad2[0].append(velocidad2[0][-1] + a2[0]*h)
    velocidad2[1].append(velocidad2[1][-1] + a2[1]*h)
    velocidad2[2].append(velocidad2[2][-1] + a2[2]*h)

    if(pos2[1][-1] < 0):
        break

g2 = plt.axes(projection='3d')
g2.scatter3D(pos2[0],pos2[1],pos2[2])
g2.set_xlabel('espacio-x')
g2.set_ylabel('espacio-y')
g2.set_zlabel('espacio-z')
plt.title('Trayectoria 2')

plt.show()
