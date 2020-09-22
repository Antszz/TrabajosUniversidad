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


ax=plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.scatter3D(px,py,pz,c=pt)
plt.show()
