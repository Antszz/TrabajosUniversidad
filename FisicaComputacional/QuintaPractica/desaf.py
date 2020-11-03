import matplotlib.pyplot as plt
import numpy as np
import math

h=0.01
t=10000

R=5
d=20
d2=20

pt=np.arange(0,t,h)
lvx = np.arange(0,1,0.05)

ax = []
ay = []

cuerpo1 = plt.Circle((-d, 0), R,lw=1,alpha=0.4)
cuerpo2 = plt.Circle((d, 0),R,lw=1,alpha=0.4)
cuerpo3 = plt.Circle((0, d2), R,lw=1,alpha=0.4)

plt.gcf().gca().add_artist(cuerpo1)
plt.gcf().gca().add_artist(cuerpo2)
plt.gcf().gca().add_artist(cuerpo3)

plt.xlim([-70,70])
plt.ylim([-70,70])

for vx0 in lvx:
    x = 15
    y = 40
    vx = vx0
    vy = 0
    px = [x]
    py = [y]

    for t in pt:
        x1 = x+d
        x2 = x-d
        x3 = x
        y2 = y-d2
        
        ax.append(-x1 / (x1**2 + y**2)**(1.5) - (x2 / (x2**2 + y**2)**(1.5)) - x3/ (x3**2 + y2**2)**(1.5))
        ay.append(-y / (x1**2 + y**2)**(1.5) - (y / (x2**2 + y**2)**(1.5)) - y2 / (x3**2 + y2**2)**(1.5))
        
        vx = vx + ax[-1] * h
        vy = vy + ay[-1] * h
        
        x = x + vx * h 
        y = y + vy * h
        
        if x >= 70:
            break
        if y >= 70:
            break
        if x1**2 + y**2 <= R**2:
            break
        if x2**2 + y**2 <= R**2:
            break
        if x3**2 + y2**2 <= R**2:
            break
        px.append(x)
        py.append(y)
    
    plt.plot(px,py)

plt.show()




