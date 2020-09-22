import matplotlib.pyplot as plt
import numpy as np
h=0.01
x=3
y=-4
vx=1
vy=2
ax=0
ay=0
pt = np.arange(0,10,h)
px=[]
py=[]
pv=[]

pa=[]
for t in pt:
    x=x+vx*h
    y=y+vy*h
    vx=vx+ax*h
    vy=vy+ay*h
    px.append(x)
    py.append(y)
    pv.append([vx,vy])
    pa.append([ax,ay])

plt.subplot(2,2,1)
plt.plot(pt,px)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(pt,pv)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('v-t')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(pt,py)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('y-t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(px,py)    
plt.xlabel('x')
plt.ylabel('y')
plt.title('espacio de fases')
plt.grid(True)
plt.show()
