from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

k = 0.1
m = 0.2
f0 = 0
c = 0.05
w = 0

h = 0.01
t = 40

ax = 0
x = 0
vx = -2

pos = []
velocidad = []
aceleracion = []

U = []
K = []
E = []

pt = np.arange(0,t,h)
ax = -k*x/m-c*vx/m+f0*np.cos(w*t)/m
vx = vx+ax*h/2


for t in pt:
    ax = -k*x/m-c*vx/m+f0*np.cos(w*t)/m
    vx = vx+ax*h
    x = x+vx*h

    pos.append(x)
    velocidad.append(vx)
    aceleracion.append(ax)

    U.append(k*(x*x)/2)
    K.append(m*(vx*vx)/2)
    E.append(u[-1]+K[-1])

    
plt.subplot(2,2,1)
plt.plot(pt,px)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('X-T')
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(pt,pv)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('V-T')
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(pt,pa)
plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.title('A-T')
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(px,pv)
plt.xlabel('velocidad')
plt.ylabel('espacio')
plt.title('espacio de fases')
plt.grid(True)

'''
plt.subplot(2,3,5)
plt.plot(px,pu,px,pk,px,pe)
plt.xlabel('velocidad')
plt.ylabel('espacio')
plt.title('espacio de fases')
plt.grid(True)
'''
plt.show()

fig = plt.figure()
ax=plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter3D(px,pv,pt)

plt.show()


plt.plot(px,pu,px,pk,px,pe)
plt.show()