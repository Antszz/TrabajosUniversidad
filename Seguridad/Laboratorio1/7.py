archivo = open("HERALDOSNEGROS_pre.txt", 'r')
mensaje = archivo.read()
mensaje = mensaje.encode("utf-8")

print(mensaje)

f=open("HERALDOSNEGROS_pre.txt","w")
f.write(mensaje)
f.close()
