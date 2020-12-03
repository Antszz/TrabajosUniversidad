import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

fig, ax = plt.subplots()
redDot, = plt.plot([0], [0], 'ro')

h=0.1
t=1800

R=2
d=4

pt=np.arange(0,t,h)
lvx = np.arange(0,0.4,0.05)

ax = []
ay = []

cuerpo1 = plt.Circle((-d, 0), R,lw=1,alpha=0.5)
cuerpo2 = plt.Circle((d, 0),R,lw=1,alpha=0.5)

plt.gcf().gca().add_artist(cuerpo1)
plt.gcf().gca().add_artist(cuerpo2)

plt.xlim([-50,50])
plt.ylim([-50,50])

x=6
y=0
vx=0
vy=0
px=[x]
py=[y]

for vx0 in lvx:
    x = 20
    y = 30
    vx = vx0
    vy = 0
    px = [x]
    py = [y]

    for t in pt:
        x1 = x + d
        x2 = x - d
        x3 = x
        y2 = y - d2
        ax = -(x1)/((x1)*2+y2)(1.5)-(x2)/((x2)2+y2)(1.5)-x3/(x32+y22)*(1.5)
        ay = -y/((x1)*2+y2)(1.5)-(y/((x2)2+y2)(1.5))-y2/(x32+y22)*(1.5)
        vx = vx + ax*h;
        x = x + vx*h
        vy = vy + ay*h 
        y = y + vy*h
        
        if x>=70:
            break
        if y>=70:
            break
        if (((x1)*2 + (y)*2) <=R*R):
            break
        if (((x2)*2 + (y)*2) <=R*R):
            break
        if(((x3)*2+(y2)*2) <=R*R):
            break
        px.append(x)
        py.append(y)

    plt.plot(px,py)

plt.show()