import matplotlib.pyplot as plt
import numpy as np
import math

h = 0.01
tiempo = 400
R = 2

pt = np.arange(0,tiempo,h)
lvx = np.arange(0,1,0.05)

ax = []
ay = []
vx = []
vy = []

cuerpo = plt.Circle((0, 0), R,lw=1,alpha=0.5)
plt.gcf().gca().add_artist(cuerpo)

for vx0 in lvx:
    x = 0
    y = 7
    vx = [vx0]
    vy = [0]
    px = [0,x]
    py = [0,y]
    for t in pt:
        ax.append(-x / (x**2 + y**2) ** (1.5))
        ay.append(-y / (x**2 + y**2) ** (1.5))
        vx.append(vx[-1] + ax[-1] * h)
        vy.append(vy[-1] + ay[-1] * h)
        x = x + vx[-1] * h
        y = y + vy[-1] * h
        if x >= 20:
            break
        if x**2 + y**2 <= R**2:
            break
        px.append(x)
        py.append(y)

    plt.plot(px,py)
plt.show()
