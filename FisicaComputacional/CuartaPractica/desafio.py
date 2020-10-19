from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

k = 0.1
m = 0.2
c = 0.05
w = 0.3
f0 = 0.01
f1 = 0

h = 0.01
t = 100

ax = 0
ax1 = 0

x = -1
x1 = -1

vx = 1
vx1 = 1

pos = []
pos1 = []

velocidad = []
velocidad1 = []

aceleracion = []
aceleracion1 = []

ax = -k*x/m-c*vx/m+f0*np.cos(w*t)/m
vx = vx+ax*h/2

ax1 = -k*x1/m-c*vx1/m+f1*np.cos(w*t)/m
vx1 = vx1+ax1*h/2

pt=np.arange(0,t,h)

for t in pt:
    ax = -k*x/m-c*vx/m+f0*np.cos(w*t)/m
    vx = vx+ax*h
    x = x+vx*h
    
    ax1 = -k*x1/m-c*vx1/m+f1*np.cos(w*t)/m
    vx1 = vx1+ax1*h
    x1 = x1+vx1*h
    
   
    pos.append(x)
    velocidad.append(vx)
    aceleracion.append(ax)

    pos1.append(x1)
    velocidad1.append(vx1)
    aceleracion1.append(ax1)


    
plt.subplot(2,2,1)
plt.plot(pt,px,pt,px1)
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('X-T')
plt.grid(True)


plt.subplot(2,2,2)
plt.plot(pt,pv,pt,pv1)
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('V-T')
plt.grid(True)


plt.subplot(2,2,3)
plt.plot(pt,pa,pt,pa1)
plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.title('A-T')
plt.grid(True)


plt.subplot(2,2,4)
plt.plot(px,pv,px,pv1)
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


fig1 = plt.figure()
ax1=plt.axes(projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.scatter3D(px1,pv1,pt)

plt.show()