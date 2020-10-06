import matplotlib.pyplot as plt
import numpy as np
import math

h = 0.001
r=8
m=5
pos = [[0],[-r],[0]]
velocidad = [[4],[0],[0]]
a = [0,2]
tiempo = 20
pt = np.arange(0, tiempo, h)

for i in pt:
    x = pos[0][-1]
    y = pos[1][-1]

    pos[0].append(x + velocidad[0][-1]*h)
    pos[1].append(y + velocidad[1][-1]*h)

    vx = velocidad[0][-1]
    vy = velocidad[1][-1]

    print("velocidad x = ",vx, " , ", "velocidad y = ", vy, "=", end ="" )
    print(math.sqrt(pow(vx,2)+pow(vy,2)), end = "\n")

    a = [-2 * x/r, -2 * y/r]

    velocidad[0].append(velocidad[0][-1] + a[0]*h)
    velocidad[1].append(velocidad[1][-1] + a[1]*h)

plt.xlim(-r-1,r+1)
plt.ylim(-r-1,r+1)
plt.plot(pos[0],pos[1])    
plt.xlabel('espacio-x')
plt.ylabel('espacio-y')
plt.title('y-x')
plt.grid(True)

plt.show()
