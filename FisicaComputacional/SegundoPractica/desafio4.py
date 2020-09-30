import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h=0.01

pos4 = [[0],[0],[0]]
velocidad4 = [[5],[2],[0]]
a4 = [0,-10,0]

while True:
    pos4[0].append(pos4[0][-1] + velocidad4[0][-1]*h)
    pos4[1].append(pos4[1][-1] + velocidad4[1][-1]*h)
    pos4[2].append(pos4[2][-1] + velocidad4[2][-1]*h)

    velocidad4[0].append(velocidad4[0][-1] + a4[0]*h)
    velocidad4[1].append(velocidad4[1][-1] + a4[1]*h)
    velocidad4[2].append(velocidad4[2][-1] + a4[2]*h)

    if(pos4[1][-1] < 0):
        break

g4 = plt.axes(projection='3d')
g4.scatter3D(pos4[0],pos4[1],pos4[2])
g4.set_xlabel('espacio-x')
g4.set_ylabel('espacio-y')
g4.set_zlabel('espacio-z')
plt.title('Trayectoria 4')

plt.show()
