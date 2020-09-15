import matplotlib.pyplot as plt
import numpy as np

h=0.01
x=-3
y=-4
vx=-2
vy=0
ax=0
ay=0
px=[]
py=[]
pvx=[]
pvy=[]
pax=[]
pay=[]
pt = np.arange(0,5,h)

for t in pt:
    y=y+vy*h
    x=x+vx*h
    vy=vy+ay*h
    vx=vx+ax*h
    py.append(y)
    px.append(x)
    pvy.append(vy)
    pvx.append(vx)
    pax.append(ax)
    pay.append(ay)

plt.subplot(2,4,1)
plt.plot(pt,px)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('x-t')
plt.grid(True)

plt.subplot(2,4,2)
plt.plot(pt,py)    
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('y-t')
plt.grid(True)

plt.subplot(2,4,3)
plt.plot(pt,pvx)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('vx-t')
plt.grid(True)

plt.subplot(2,4,4)
plt.plot(pt,pvy)    
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('vy-t')
plt.grid(True)

plt.subplot(2,4,5)
plt.plot(pt,pax)    
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('ax-t')
plt.grid(True)

plt.subplot(2,4,6)
plt.plot(pt,pay)    
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('ay-t')
plt.grid(True)

plt.subplot(2,4,7)
plt.plot(px,pvx)    
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases X')
plt.grid(True)

plt.subplot(2,4,8)
plt.plot(py,pvy)    
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases Y')
plt.grid(True)

plt.show()