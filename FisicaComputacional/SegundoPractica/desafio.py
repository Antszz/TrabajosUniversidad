import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h=0.01
pos1 = [[0],[0],[0]]
velocidad1 = [[5],[2],[0]]
a1 = [2,-10,0]

pos2 = [[0],[0],[0]]
velocidad2 = [[5],[2],[0]]
a2 = [-1,-10,0]

pos3 = [[0],[0],[0]]
velocidad3 = [[5],[2],[0]]
a3 = [2,-10,-1]

pos4 = [[0],[0],[0]]
velocidad4 = [[5],[2],[0]]
a4 = [0,-10,0]

flag1 = True
flag2 = True
flag3 = True
flag4 = False

while True:
    if(flag1):
        pos1[0].append(pos1[0][-1] + velocidad1[0][-1]*h)
        pos1[1].append(pos1[1][-1] + velocidad1[1][-1]*h)
        pos1[2].append(pos1[2][-1] + velocidad1[2][-1]*h)

        velocidad1[0].append(velocidad1[0][-1] + a1[0]*h)
        velocidad1[1].append(velocidad1[1][-1] + a1[1]*h)
        velocidad1[2].append(velocidad1[2][-1] + a1[2]*h)
    if(flag2):
        pos2[0].append(pos2[0][-1] + velocidad2[0][-1]*h)
        pos2[1].append(pos2[1][-1] + velocidad2[1][-1]*h)
        pos2[2].append(pos2[2][-1] + velocidad2[2][-1]*h)

        velocidad2[0].append(velocidad2[0][-1] + a2[0]*h)
        velocidad2[1].append(velocidad2[1][-1] + a2[1]*h)
        velocidad2[2].append(velocidad2[2][-1] + a2[2]*h)
    if(flag3):
        pos3[0].append(pos3[0][-1] + velocidad3[0][-1]*h)
        pos3[1].append(pos3[1][-1] + velocidad3[1][-1]*h)
        pos3[2].append(pos3[2][-1] + velocidad3[2][-1]*h)

        velocidad3[0].append(velocidad3[0][-1] + a3[0]*h)
        velocidad3[1].append(velocidad3[1][-1] + a3[1]*h)
        velocidad3[2].append(velocidad3[2][-1] + a3[2]*h)
    if(flag4):
        pos4[0].append(pos4[0][-1] + velocidad4[0][-1]*h)
        pos4[1].append(pos4[1][-1] + velocidad4[1][-1]*h)
        pos4[2].append(pos4[2][-1] + velocidad4[2][-1]*h)

        velocidad4[0].append(velocidad4[0][-1] + a4[0]*h)
        velocidad4[1].append(velocidad4[1][-1] + a4[1]*h)
        velocidad4[2].append(velocidad4[2][-1] + a4[2]*h)

    if(pos1[1][-1] < 0):
        flag1 = False
    if(pos2[1][-1] < 0):
        flag2 = False
    if(pos3[1][-1] < 0):
        flag3 = False
    if(pos4[1][-1] < 0):
        flag4 = False

    if not(flag1 or flag2 or flag3 or flag4):
    	break

plt.subplot(2,2,1)
g1 = plt.axes(projection='3d')
g1.scatter3D(pos1[0],pos1[1],pos1[2])
g1.set_xlabel('espacio-x')
g1.set_ylabel('espacio-y')
g1.set_zlabel('espacio-z')
plt.title('Trayectoria 1')
plt.grid(True)

plt.subplot(2,2,2)
g2 = plt.axes(projection='3d')
g2.scatter3D(pos2[0],pos2[1],pos2[2])
g2.set_xlabel('espacio-x')
g2.set_ylabel('espacio-y')
g2.set_zlabel('espacio-z')
plt.title('Trayectoria 2')
plt.grid(True)

plt.subplot(2,2,3)
g3 = plt.axes(projection='3d')
g3.scatter3D(pos3[0],pos3[1],pos3[2])
g3.set_xlabel('espacio-x')
g3.set_ylabel('espacio-y')
g3.set_zlabel('espacio-z')
plt.title('Trayectoria 3')
plt.grid(True)

plt.subplot(2,2,4)
g4 = plt.axes(projection='3d')
g4.scatter3D(pos4[0],pos4[1],pos4[2])
g4.set_xlabel('espacio-x')
g4.set_ylabel('espacio-y')
g4.set_zlabel('espacio-z')
plt.title('Trayectoria 4')
plt.grid(True)

plt.show()
