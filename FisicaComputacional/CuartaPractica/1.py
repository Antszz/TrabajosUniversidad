import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h = 0.001
k = 0.1
m = 0.2

px = 2
pos = []

velo = 0
velocidad = []

aceleracion = []

tiempo = 50
pt = np.arange(0, tiempo, h)

U = []
K = []
E = []

for i in pt:
    pos.append(px)
    velocidad.append(velo)
    aceleracion.append((-k/m)*px)

    velo = velo + aceleracion[-1]*h
    px = px + velo*h
    
    U.append((1/2)*k*pos[-1]**2)
    K.append((1/2)*m*velocidad[-1]**2)
    E.append(U[-1]+K[-1])

"""
plt.subplot(2,2,1)
plt.plot(pos,pt)    
plt.xlabel('espacio-x')
plt.ylabel('tiempo')
plt.title('x - t')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(velocidad,pt)    
plt.ylabel('tiempo')
plt.xlabel('velocidad-x')
plt.title('x - t')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(aceleracion,pt)    
plt.ylabel('tiempo')
plt.xlabel('acelearacion-x')
plt.title('x - t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(velocidad,pos)    
plt.ylabel('espacio-x')
plt.xlabel('velocidad-x')
plt.title('x - t')
plt.grid(True)

plt.show()

plt.plot(U,pos)
plt.plot(E,pos)
plt.plot(K,pos)
plt.xlabel('E. elastica')
plt.ylabel('espacio-x')
plt.title('U,E,K - x')
plt.grid(True)

plt.show()

"""

g2 = plt.axes(projection='3d')
g2.scatter3D(velocidad,pos,pt)
g2.set_xlabel('v')
g2.set_ylabel('x')
g2.set_zlabel('t')
plt.title('v - x - t')

plt.show()
