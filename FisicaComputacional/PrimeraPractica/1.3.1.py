import matplotlib.pyplot as plt
import numpy as np
h=0.01
x=-3
y=-4
z=-5
vx=0
vy=2
vz=4
ax=0
ay=0
az=0
pt = np.arange(5,0,-h)
px=[]
py=[]
pz=[]
pv=[]

pa=[]
for t in pt:
    x=x-vx*h
    y=y-vy*h
    z=z-vz*h
    vx=vx-ax*h
    vy=vy-ay*h
    vz=vz-az*h
    px.append(x)
    py.append(y)
    pz.append(z)
    pv.append([vx,vy,vz])
    pa.append([ax,ay,az])

    
plt.subplot(3,2,1)
plt.plot(pt,px)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(3,2,2)
plt.plot(pt,py)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('y-t')
plt.grid(True)

plt.subplot(3,2,3)
plt.plot(pt,pz)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('z-t')
plt.grid(True)

plt.subplot(3,2,4)
plt.plot(pt,pv)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)


plt.show()
