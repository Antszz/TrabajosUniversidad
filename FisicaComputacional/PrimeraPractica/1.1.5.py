import matplotlib.pyplot as plt
import numpy as np
h=0.01
x=0
vx=0
ax=0

pt = np.arange(0,2,h)
while x!=300:
    x=0
    vx=vx+1
    px=[]
    pv=[]
    pa=[]
    for t in pt:
        x=x+vx*h
        vx=vx+ax*h
        px.append(x)
        pv.append(vx)
        pa.append(ax)


print(pv[len(pv)-1])
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

