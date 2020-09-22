import matplotlib.pyplot as plt
import numpy as np
h=0.01
x=-5
vx=3
ax=0
px=[]
pv=[]
pa=[]
pt = np.arange(0,15,h)

for t in pt:
    if (t>=3 and t<8):
        vx=6
    if(t>=8 and t<10):
        vx=3
    if t>=10:
        vx=-2
    x=x+vx*h
    vx=vx+ax*h
    px.append(x)
    pv.append(vx)
    pa.append(ax)

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
plt.plot(pt,pa)    
plt.xlabel('tiempo')
plt.ylabel('aceleracion')
plt.title('a-t')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(px,pv)    
plt.xlabel('espacio')
plt.ylabel('velocidad')
plt.title('espacio de fases')
plt.grid(True)

plt.show()
