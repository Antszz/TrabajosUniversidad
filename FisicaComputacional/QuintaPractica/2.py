import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

fig, ax = plt.subplots()
redDot, = plt.plot([0], [0], 'ro')

h=0.1
t=1800

R=2
d=10

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

x=10
y=10
vx=0.3
vy=0
px=[x]
py=[y]

graficar, = plt.plot([], [])
x_datos, y_datos=[],[]

def animate(i):
    global x,y,vx,vy
    x1 = x + d
    x2 = x - d

    ax.append(-x1 / (x1**2 + y**2)**(1.5) - x2 / (x2**2 + y**2) ** 1.5)
    ay.append(-y / (x1**2+y**2)**(1.5) - y / (x2**2 + y**2) ** 1.5)
    
    vx = vx + ax[-1]*h;
    vy = vy + ay[-1]*h
    
    x = x + vx*h 
    y = y + vy*h
    redDot.set_data(x, y)
    if x >= 50:
        return redDot, graficar,
    if y >= 50:
        return redDot, graficar,
    if x1**2 + y**2 <= R**2:
        return redDot, graficar,
    if x2**2 + y**2 <= R**2:
        return redDot, graficar,
 
    x_datos.append(x)
    y_datos.append(y)
    graficar.set_data(x_datos, y_datos)
    return redDot, graficar,

myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0,t,h), \
                                      interval=10000, blit=True, repeat=False)

myAnimation.save('animation3.mp4', writer='ffmpeg', fps=960);