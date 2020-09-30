def euler(espacio,velocidad,aceleracion,inicio=True):
    espacio= np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    aceleracion = np.array(aceleracion,dtype=np.float32)
    pe=[]
    pv=[]
    pa=[]
    a =1 if inicio else -1
    for t in pt:
        espacio+=(velocidad*h*a)
        velocidad+=(aceleracion*h*a)
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
    return npa(pe),npa(pv),npa(pa)

h = 0.1
exercise ="1.1.1"
time=10
espacio=[0,-30]
velocidad = [0,-30]
aceleracion = [0,-10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#draw_all(exercise)