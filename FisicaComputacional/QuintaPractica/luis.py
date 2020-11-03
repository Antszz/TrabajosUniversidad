import matplotlib.pyplot as plt
import numpy as np
import math

h=0.01
t=400


R=5


pt=np.arange(0,t,h)
vx0=0

while(vx0<1):
    x=3
    y=4
    vx=vx0
    vy=0
    ax=0
    ay=0
    px=[0,x]
    py=[0,y]
   
    for t in pt:
        ax=-x/(x*2 + y2)*(1.5)
        ay=-y/(x*2 + y2)*(1.5)
        vx=vx+ax*h
        vy=vy+ay*h
        x=x+vx*h
        y=y+vy*h
        
        if x>=20:
            break
        if((x)*2 + (y)*2)<=R*R:
            break
        px.append(x)
        py.append(y)
    
        #pv.append([vx,vy])
        #pa.append([ax,ay])
    plt.plot(px,py)
    plt.grid(True)
    vx0+=0.05
plt.show()


'''
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