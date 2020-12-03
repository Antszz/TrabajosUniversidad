import matplotlib.pyplot as plt
import numpy as np
import math

h=0.01
t=1000
R=2
d=6
pt=np.arange(0,t,h)
vx0=0
pla1 = plt.Circle((0, -3), R,lw=1,alpha=0.5)
pla2 = plt.Circle((0, 3),R,lw=1,alpha=0.5)
plt.gcf().gca().add_artist(pla1)
plt.gcf().gca().add_artist(pla2)

plt.xlim([-50,50])
plt.ylim([-50,50])
while(vx0<1):
    ##MASA1
    x=0
    y=0
    vx=vx0
    vy=0
    px=[x]
    py=[y]

    for t in pt:
        ##MASA1
        x1=x+d
        x2=x-d
        ax=-x1 / (x1**2 + y**2)**(1.5) - x2 / (x2**2 + y**2) ** 1.5
        ay=-y / (x1**2+y**2)**(1.5) - y / (x2**2 + y**2) ** 1.5
        vx = vx + ax*h
        x = x + vx*h
        vy= vy + ay*h 
        y = y + vy*h
        
        if x>=50:
            break
        if y>=50:
            break
        if x1**2 + y**2 <= R**2:
            break
        if x2**2 + y**2 <= R**2:
            break
        px.append(x)
        py.append(y)
    
    
        #pv.append([vx,vy])
        #pa.append([ax,ay])
    plt.plot(px,py)
    plt.grid(True)
    vx0+=0.1

plt.show('hold')
input()