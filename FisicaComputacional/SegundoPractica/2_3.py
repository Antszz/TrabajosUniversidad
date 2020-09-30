import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

h = 0.01
t = 0
pos = [[0],[3],[0]]
velocidad = [[2],[3],[5]]
a = [0,-10,0]
aux = []

while True:
    if velocidad[1][-1] >= 0:
        t += h
        aux = [pos[0][-1],pos[1][-1],pos[2][-1]]

    pos[0].append(pos[0][-1] + velocidad[0][-1]*h)
    pos[1].append(pos[1][-1] + velocidad[1][-1]*h)
    pos[2].append(pos[2][-1] + velocidad[2][-1]*h)

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)
    velocidad[2].append(velocidad[2][-1] + a[2]*h)

    if(pos[1][-1] < 0):
        break
aux = [round(aux[0],2),round(aux[1],2),round(aux[2],2)]

print(f"Tiempo en que la pelota llega a una altura máxima: {round(t,2)}segundos")
print(f"Coordenadas de mi altua máxima: {aux}")
print(f"El alcance vectorial es: {[round(pos[0][-1]-pos[0][0],2),round(pos[1][-1]-pos[1][0],2),round(pos[2][-1]-pos[2][0],2)]}")

g1 = plt.axes(projection='3d')
g1.scatter3D(pos[0],pos[1],pos[2])
g1.set_xlabel('espacio-x')
g1.set_ylabel('espacio-y')
g1.set_zlabel('espacio-z')
plt.title('Trayectoria')

plt.show()