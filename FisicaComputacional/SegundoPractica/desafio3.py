import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h=0.01

pos3 = [[0],[0],[0]]
velocidad3 = [[5],[2],[0]]
a3 = [2,-10,-1]

while True:
    pos3[0].append(pos3[0][-1] + velocidad3[0][-1]*h)
    pos3[1].append(pos3[1][-1] + velocidad3[1][-1]*h)
    pos3[2].append(pos3[2][-1] + velocidad3[2][-1]*h)

    velocidad3[0].append(velocidad3[0][-1] + a3[0]*h)
    velocidad3[1].append(velocidad3[1][-1] + a3[1]*h)
    velocidad3[2].append(velocidad3[2][-1] + a3[2]*h)

    if(pos3[1][-1] < 0):
        break

g3 = plt.axes(projection='3d')
g3.scatter3D(pos3[0],pos3[1],pos3[2])
g3.set_xlabel('espacio-x')
g3.set_ylabel('espacio-y')
g3.set_zlabel('espacio-z')
plt.title('Trayectoria 3')

plt.show()
