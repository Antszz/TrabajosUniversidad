u = [[0,60,60,60,0],[80,0,0,0,40],[80,0,0,0,40],[80,0,0,0,40],[80,0,0,0,40],[0,20,20,20,0]]
rmax = 0
for j in range (1,4):
    for i in range (4,0,-1):
        print(j+1,i,">>>>>>>>>>>")
        rij = (u[i][j-1]+u[i][j+1]+u[i+1][j]+u[i-1][j]-4*u[i][j])/4
        u[i][j] = u[i][j] + rij
        if( rmax <= abs(rij)):
            rmax = abs(rij)
        print("rij =",rij)
        print("u[i][j] =",u[i][j])
        print("rmax =",rmax)
        print(">>>>>>>>>>>>>>>")
        print()
print(u)